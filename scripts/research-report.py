#!/usr/bin/env python3
"""Build the website/idea research coverage report from the saved research data.

This script is intentionally read-only with respect to the canonical research
records. Run from anywhere; paths are resolved relative to this file.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
TZ = ZoneInfo("Europe/Amsterdam")
OUT_JSON = ROOT / "data/research-report.json"
OUT_MD = ROOT / "source-guides/REPORT.md"
MANUAL_GUIDES = {
    "oba.nl": "oba.md",
    "debomsspijker.nl": "boomsspijker.md",
    "boomsspijker.nl": "boomsspijker.md",
    "huisvandebuurtdeboomsspijker.nl": "boomsspijker.md",
    "pakhuisdezwijger.nl": "pakhuisdezwijger.md",
    "dezwijger.nl": "pakhuisdezwijger.md",
    "debalie.nl": "debalie.md",
    "spui25.nl": "spui25.md",
    "framerframed.nl": "framerframed.md",
    "tolhuistuin.nl": "tolhuistuin.md",
    "hipsy.nl": "hipsy.md",
}
BLACKLIST_PATTERNS = {
    "climbing": re.compile(r"\b(?:climb(?:ing)?|boulder(?:ing|s)?|bouldergym|klimmuur)\b", re.I),
    "circus-acrobatics": re.compile(r"\b(?:circus|acrobat(?:ic|ics)?|acro.?yoga|aerial|pole(?: dance| fitness)?|juggling|handstand|object.manipulation)\b", re.I),
}
UNAVAILABLE = {"cancelled", "sold-out", "waitlist", "conflict"}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def valid_url(url):
    if not isinstance(url, str):
        return False
    p = urlparse(url)
    return p.scheme in {"http", "https"} and bool(p.netloc)


def host(url):
    return (urlparse(url).hostname or "").lower().removeprefix("www.")


def guide_for(domain):
    if domain in MANUAL_GUIDES:
        return MANUAL_GUIDES[domain]
    slug = domain.removeprefix("www.").replace(".", "-")
    return re.sub(r"[^a-z0-9-]+", "-", slug) + ".md"


def event_primary(event):
    discovery = event.get("discoverySource")
    if valid_url(discovery):
        return discovery
    for url in event.get("sourceUrls") or []:
        if valid_url(url):
            return url
    return None


def local_dt(value):
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            return None
        return dt.astimezone(TZ)
    except (TypeError, ValueError):
        return None


def preferred(event, prefs):
    start = local_dt(event.get("start"))
    if not start:
        return False
    if prefs.get("weekends", True) and start.weekday() >= 5:
        return True
    morning_end = prefs.get("weekdayMorningEnd", "10:00")
    if start.strftime("%H:%M") >= prefs.get("weekdayEveningStart", "18:00"):
        return True
    if start.strftime("%H:%M") < morning_end:
        end = local_dt(event.get("end"))
        return bool(end and end.date() == start.date() and end > start and end.strftime("%H:%M") <= morning_end)
    return False


def blacklist_reason(item, prefs):
    if item.get("status") == "excluded":
        return "Previously declined"
    text = f"{item.get('title', item.get('name', ''))} {item.get('category', '')}"
    for rule in prefs.get("blacklist", []):
        pattern = BLACKLIST_PATTERNS.get(rule)
        if pattern and pattern.search(text):
            return {"climbing": "Climbing & bouldering", "circus-acrobatics": "Circus & acrobatics"}.get(rule, rule)
    for keyword in prefs.get("customKeywords", []):
        if keyword and keyword.casefold() in text.casefold():
            return f"Keyword: {keyword}"
    return None


def is_dated(e):
    return e.get("status") == "dated"


def exportable(e, reason):
    return bool(is_dated(e) and e.get("dateEvidence") and local_dt(e.get("start")) and not reason and e.get("availability") not in UNAVAILABLE)


def norm_venue(value):
    # Deliberately strict: no fuzzy aliases, street/location matching, or generic venue classes.
    value = (value or "").casefold().strip()
    value = re.sub(r"[^\w]+", " ", value, flags=re.UNICODE)
    return " ".join(value.split())


def event_urls(e):
    return {u for u in (e.get("sourceUrls") or []) if valid_url(u)} | ({e["discoverySource"]} if valid_url(e.get("discoverySource")) else set())


def idea_links(idea, events, offers, event_idea_links=None):
    explicit = []
    urls = []
    venues = []
    iid = idea.get("id")
    event_idea_links = event_idea_links or {}
    idea_urls = {u for u in [idea.get("sourceUrl"), *((idea.get("research") or {}).get("sourceUrls") or [])] if valid_url(u)}
    iname = norm_venue(idea.get("name"))
    for e in events:
        if not is_dated(e):
            continue
        if iid and (iid in (e.get("ideaIds") or []) or iid in event_idea_links.get(e.get("id"), [])):
            explicit.append(e)
        elif iname and iname == norm_venue(e.get("venue")):
            venues.append(e)
    offer_matches = []
    for o in offers:
        if iid and iid in (o.get("ideaIds") or []):
            offer_matches.append(o)
        elif iname and iname == norm_venue(o.get("venue")):
            offer_matches.append(o)
    # One event is counted once, with the strongest available evidence method.
    emap = {e["id"]: (e, "explicit ideaIds") for e in explicit}
    for e in urls:
        emap.setdefault(e["id"], (e, "exact source URL"))
    for e in venues:
        emap.setdefault(e["id"], (e, "exact normalized venue name"))
    return list(emap.values()), offer_matches


def observed_method(item):
    method = item.get("researchMethod")
    if method:
        return method
    evidence = item.get("evidence")
    if isinstance(evidence, dict):
        for key in ("researchMethod", "browserMethod", "method"):
            if evidence.get(key):
                return str(evidence[key])
    return "Unknown (historical provenance not recorded)"


def batch_round(batch, path):
    explicit = batch.get("researchRound")
    if explicit:
        return str(explicit)
    for event in batch.get("events") or []:
        if event.get("researchRound"):
            return str(event["researchRound"])
    match = re.match(r"round-(\d+)(?:-|$)", path.stem)
    return f"round-{match.group(1)}" if match else None


def normalize_attempt(attempt):
    website = attempt.get("website") or attempt.get("site") or attempt.get("source") or "Unknown"
    route = attempt.get("route") or attempt.get("routes")
    if isinstance(route, list):
        route = ", ".join(str(x) for x in route)
    method = attempt.get("method") or "Method not recorded"
    outcomes = []
    for key in ("result", "success", "worked", "outcome"):
        value = attempt.get(key)
        if value:
            outcomes.append(f"{key}: {json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else value}")
    for key in ("failureOrNoDataReason", "blockOrNoData", "failed", "failure", "stoppedBecause"):
        value = attempt.get(key)
        if value:
            outcomes.append(f"{key}: {json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else value}")
    if attempt.get("nextStep"):
        outcomes.append(f"next: {attempt['nextStep']}")
    result = "; ".join(str(x) for x in outcomes) or "No outcome recorded in attempt log."
    return {"website": str(website), "method": str(method) + (f" · route: {route}" if route else ""), "result": result}


def md_escape(v):
    return str(v if v is not None else "").replace("|", "\\|").replace("\n", " ")


def build():
    events = read_json(ROOT / "data/events.json")
    offers = read_json(ROOT / "data/offers.json")
    ideas = read_json(ROOT / "data/ideas.json")
    sources = read_json(ROOT / "data/sources.json")
    prefs = read_json(ROOT / "data/preferences.json")
    baseline = read_json(ROOT / "research/iterations/baseline.json")
    baseline_ids = set(baseline.get("datedIds", []))
    dated = [e for e in events if is_dated(e)]
    reasons = {e["id"]: blacklist_reason(e, prefs) for e in dated}
    allowed = [e for e in dated if not reasons[e["id"]]]
    pref = [e for e in allowed if preferred(e, prefs)]
    export = [e for e in dated if exportable(e, reasons[e["id"]])]
    new = [e for e in dated if e.get("id") not in baseline_ids]

    website_map = {}
    primary_by_id = {}
    for e in dated:
        url = event_primary(e)
        if not url:
            primary_by_id[e["id"]] = None
            continue
        d = host(url)
        primary_by_id[e["id"]] = d
        row = website_map.setdefault(d, {"domain": d, "entryUrl": url, "guide": guide_for(d), "primaryEvents": 0, "primaryPreferred": 0, "offers": 0, "methods": set()})
        row["primaryEvents"] += 1
        if not reasons[e["id"]] and preferred(e, prefs):
            row["primaryPreferred"] += 1
        row["methods"].add(observed_method(e))
    for o in offers:
        urls = [u for u in (o.get("sourceUrls") or []) if valid_url(u)]
        url = next((u for u in urls if valid_url(o.get("discoverySource")) and u == o.get("discoverySource")), None) or (o.get("discoverySource") if valid_url(o.get("discoverySource")) else (urls[0] if urls else None))
        if not url:
            continue
        d = host(url)
        row = website_map.setdefault(d, {"domain": d, "entryUrl": url, "guide": guide_for(d), "primaryEvents": 0, "primaryPreferred": 0, "offers": 0, "methods": set()})
        row["offers"] += 1
        row["methods"].add(observed_method(o))
    # Include checked sources with zero records so an unsuccessful route is visible.
    for source in sources:
        url=source.get('url')
        if valid_url(url):
            d=host(url)
            website_map.setdefault(d, {"domain":d,"entryUrl":url,"guide":guide_for(d),"primaryEvents":0,"primaryPreferred":0,"offers":0,"methods":set()})
    for domain, row in website_map.items():
        primary=[e for e in dated if primary_by_id.get(e['id'])==domain]
        row['newEvents']=sum(e['id'] not in baseline_ids for e in primary)
        row['newPreferred']=sum(e['id'] not in baseline_ids and not reasons[e['id']] and preferred(e,prefs) for e in primary)
        row['allowedEvents']=sum(not reasons[e['id']] for e in primary)
        row['supportingCitations']=sum(domain in {host(u) for u in event_urls(e)} for e in dated)
        row['methodCounts']={}
        for e in primary:
            m=observed_method(e);row['methodCounts'][m]=row['methodCounts'].get(m,0)+1
        if not row['methods']:row['methods'].add('No dated event or offer credited; see source guide / round attempts')
    websites = sorted(({**w, "methods": sorted(w["methods"])} for w in website_map.values()), key=lambda w: (-w["primaryEvents"], w["domain"]))

    idea_rows = []
    for i in ideas:
        links, offer_links = idea_links(i, events, offers)
        linked_events = [e for e, _ in links]
        is_allowed = [e for e in linked_events if not reasons.get(e["id"]) ]
        wdomains = sorted({primary_by_id.get(e["id"]) for e in linked_events if primary_by_id.get(e["id"])} | {host(u) for u in [i.get("sourceUrl"), *((i.get("research") or {}).get("sourceUrls") or [])] if valid_url(u)})
        methods = sorted({m for _, m in links})
        research = i.get("research") or {}
        step = research.get("nextStep") or ("Research a current primary calendar; no exact linked dated record yet." if not linked_events else "Recheck the organizer for changes and availability.")
        idea_blacklist = blacklist_reason(i, prefs)
        if idea_blacklist:
            idea_rows.append({"id": i.get("id"), "name": i.get("name", ""), "status": f"excluded · {idea_blacklist}", "events": 0, "preferredEvents": 0, "offers": 0, "websites": [], "linkMethod": ", ".join(methods) if methods else "No exact link", "nextStep": f"Excluded from active idea counts by the saved blacklist: {idea_blacklist}.", "rawEvents": len(linked_events), "rawOffers": len(offer_links)})
        else:
            idea_rows.append({"id": i.get("id"), "name": i.get("name", ""), "status": research.get("status") or i.get("status", "unknown"), "events": len(linked_events), "preferredEvents": sum(1 for e in is_allowed if preferred(e, prefs)), "offers": len(offer_links), "websites": wdomains, "linkMethod": ", ".join(methods) if methods else "No exact link", "nextStep": step})

    round_files = sorted((ROOT / "research/iterations").glob("round-*.json"))
    # Group all useful batch logs by actual research round; do not turn each source file into a pseudo-round.
    attempts_by_round = defaultdict(list)
    for path in round_files:
        batch = read_json(path)
        batch_events = batch.get("events") or []
        batch_sources = batch.get("sources") or []
        batch_attempts = batch.get("attempts") or []
        if not (batch_events or batch_sources or batch_attempts):
            continue
        rid = batch_round(batch, path)
        if rid:
            attempts_by_round[rid].extend(normalize_attempt(a) for a in batch_attempts)
    round_rows = []
    canonical_rounds = sorted({e.get("researchRound") for e in dated if e.get("researchRound")})
    for rid in canonical_rounds:
        rows = [e for e in dated if e.get("researchRound") == rid]
        new_rows = [e for e in rows if e.get("id") not in baseline_ids]
        round_rows.append({"id": rid, "newDated": len(new_rows), "preferredNew": sum(preferred(e, prefs) for e in new_rows if not reasons.get(e["id"])), "summary": f"Canonical records explicitly tagged {rid}; counts are derived from IDs absent from baseline.", "attempts": attempts_by_round.get(rid, [])})
    # Preserve zero-yield route logs when a round has attempts but no canonical dated record.
    for rid in sorted(set(attempts_by_round) - set(canonical_rounds)):
        round_rows.append({"id": rid, "newDated": 0, "preferredNew": 0, "summary": "Attempt log present, but no canonical dated event is explicitly tagged to this round.", "attempts": attempts_by_round[rid]})
    round_rows.sort(key=lambda r: (int(re.search(r"\d+", r["id"]).group()), r["id"]))

    summary = {
        "rawDated": len(dated),
        "allowedDated": len(allowed),
        "preferredDated": len(pref),
        "exportable": len(export),
        "blacklistedDated": len(dated) - len(allowed),
        "newDated": len(new),
        "newPreferred": sum(1 for e in new if not reasons[e["id"]] and preferred(e, prefs)),
        "roundCount": len(round_rows),
        "offers": sum(1 for o in offers if not blacklist_reason(o, prefs)),
        "ideas": len(ideas),
    }
    blacklisted = [{"id": e.get("id"), "title": e.get("title", ""), "date": (local_dt(e.get("start")).date().isoformat() if local_dt(e.get("start")) else None), "reason": reasons[e["id"]]} for e in dated if reasons[e["id"]]]
    report = {"checkedAt": read_json(ROOT / "data/meta.json").get("checkedAt"), "summary": summary, "websites": websites, "ideas": idea_rows, "rounds": round_rows, "blacklist": blacklisted}

    evening = prefs.get("weekdayEveningStart", "18:00")
    morning = prefs.get("weekdayMorningEnd", "10:00")
    md = ["# Research coverage report", "", f"Generated from canonical files · checked {report['checkedAt'] or 'date not recorded'} · Europe/Amsterdam.", "", f"Counts use the saved default preferences. A dated listing is a record with `status: dated`; allowed means it does not match the saved blacklist. Preferred means weekend, weekday start at or after {evening}, or weekday start before {morning} with a known, same-day end no later than {morning}. Unknown end times do not count as preferred. Exportable follows the app rule: exact dated record, date evidence, valid start, not blacklisted, and availability not cancelled/sold-out/waitlist/conflict.", "", f"Raw dated: **{summary['rawDated']}** · Allowed: **{summary['allowedDated']}** · Preferred: **{summary['preferredDated']}** · Exportable: **{summary['exportable']}** · Blacklisted dated: **{summary['blacklistedDated']}** · New vs baseline: **{summary['newDated']}** ({summary['newPreferred']} preferred) · Allowed undated options: **{summary['offers']}** · Ideas covered: **{summary['ideas']}** · Research rounds with attempt logs/provenance: **{summary['roundCount']}**.", "", "Dated-source counts assign each occurrence to exactly one primary website: a valid `discoverySource`, otherwise the first valid `sourceUrls` entry. Supporting citations are non-additive and do not receive extra event credit. Website counts may be compared with idea counts, but idea links can overlap across ideas. An idea count of zero means no linked verified record under the matching rules; it does not prove the venue has no relevant events.", "", "## Website yield", "", "| Website | Raw primary dated | New dated | Preferred | Raw drop-ins | Observed methods | Guide |", "|---|---:|---:|---:|---:|---|---|"]
    for w in websites:
        md.append(f"| [{md_escape(w['domain'])}]({w['entryUrl']}) | {w['primaryEvents']} | {w['newEvents']} | {w['primaryPreferred']} | {w['offers']} | {md_escape(', '.join(w['methods']))} | [{w['guide']}](../source-guides/{w['guide']}) |")
    md += ["", "`Unknown (historical provenance not recorded)` means the canonical event/offer evidence did not explicitly save a method. Later inspection of a website is not assigned retroactively to old records.", "", "## Blacklisted dated records", "", "These records remain in raw counts but are excluded from allowed/preferred/exportable counts.", "", "| Date | Event | Exclusion reason |", "|---|---|---|"]
    for row in blacklisted:
        md.append(f"| {row['date'] or 'Unknown'} | {md_escape(row['title'])} | {md_escape(row['reason'])} |")
    if not blacklisted:
        md.append("| — | None | — |")
    md += ["", "## Idea coverage", "", "Every idea is listed. Matching uses explicit `ideaIds`, exact normalized idea-name / event-venue equality, in that order; there is no fuzzy or domain-wide matching.", "", "| Idea | Status | Dated | Preferred | Drop-ins | Websites / link method | Next step |", "|---|---|---:|---:|---:|---:|---|---|"]
    for row in idea_rows:
        sites = ", ".join(row["websites"]) or row["linkMethod"]
        md.append(f"| {md_escape(row['name'])} | {md_escape(row['status'])} | {row['events']} | {row['preferredEvents']} | {row['offers']} | {md_escape(sites + (' · ' + row['linkMethod'] if row['websites'] and row['linkMethod'] != 'No exact link' else ''))} | {md_escape(row['nextStep'])} |")
    md += ["", "Idea totals overlap and must not be added to obtain unique event counts. Preferred idea counts exclude blacklisted linked events. A zero is absence of an exact verified link, not evidence that no activity exists.", "", "## Research rounds and attempts", ""]
    if not round_rows:
        md.append("No canonical event records have an explicit `researchRound` tag, and no iteration attempt logs were present.")
    else:
        for rr in round_rows:
            md += [f"### {rr['id']} · {rr['newDated']} new dates · {rr['preferredNew']} preferred", "", rr["summary"], ""]
            if rr["attempts"]:
                md += ["| Website | Method / route | Recorded outcome |", "|---|---|---|"]
                for a in rr["attempts"]:
                    md.append(f"| {md_escape(a['website'])} | {md_escape(a['method'])} | {md_escape(a['result'])} |")
                md.append("")
    md += ["Android app research was not used or credited. Attempt outcomes are taken from saved iteration logs; failed or zero-yield routes remain visible. Attempt logs without matching canonical `researchRound` provenance do not receive date counts.", ""]
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    write_json(OUT_JSON, report)
    return report


if __name__ == "__main__":
    r = build()
    print(json.dumps(r["summary"], ensure_ascii=False, sort_keys=True))
