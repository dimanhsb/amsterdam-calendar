#!/usr/bin/env python3
"""Create missing public-source guides from saved source evidence; never overwrite manual guides."""
from __future__ import annotations
import ipaddress, json, pathlib, re, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
GUIDES = ROOT / 'source-guides'
SPECIAL = {
    'oba.nl': 'oba.md',
    'huisvandebuurtdeboomsspijker.nl': 'boomsspijker.md',
    'dezwijger.nl': 'pakhuisdezwijger.md',
    'debalie.nl': 'debalie.md',
    'spui25.nl': 'spui25.md',
    'framerframed.nl': 'framerframed.md',
    'tolhuistuin.nl': 'tolhuistuin.md',
    'hipsy.nl': 'hipsy.md',
}
BLACKLIST_DOMAIN_RULES = {
    'climbing': {'beestboulders.com', 'betaboulders.nl', 'boulderhalluchthaven.nl', 'monk.nl'},
    'circus-acrobatics': {'circuslab.amsterdam'},
}
METHOD_KEYS = ('browserMethod', 'researchMethod', 'method', 'navigation', 'route')
GUIDE_ONLY_SOURCES = [
    ('De Boomsspijker venue agenda', 'https://huisvandebuurtdeboomsspijker.nl/agenda/kalender'),
    ('Framer Framed agenda', 'https://framerframed.nl/agenda/'),
    ('SPUI25 November agenda', 'https://www.spui25.nl/agenda/location/spui25/start/2026/11'),
]

def load_sources():
    by_url = {}
    for source in json.loads((ROOT / 'data/sources.json').read_text()):
        by_url[source['url']] = source
    for path in sorted((ROOT / 'research/iterations').glob('round-*.json')):
        try:
            batch = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        for source in batch.get('sources', []):
            if source.get('url'):
                by_url[source['url']] = source
    # Discovery-only links need instructions too. They are leads, not verified
    # source observations, and must not acquire a made-up checked date.
    for idea in json.loads((ROOT / 'data/ideas.json').read_text()):
        urls = [idea.get('sourceUrl'), *idea.get('research', {}).get('sourceUrls', [])]
        for url in filter(None, urls):
            by_url.setdefault(url, {'url': url, 'title': idea['name'],
                                   'type': 'Idea discovery reference; not a verified extraction route'})
    catalog_path = ROOT / 'data/idea-catalog.json'
    if catalog_path.exists():
        for provider in json.loads(catalog_path.read_text()).get('providers', []):
            url = provider.get('url')
            if url:
                by_url.setdefault(url, {'url': url, 'title': provider['name'],
                                       'type': 'Potential provider; access and schedule unverified'})
    for title, url in GUIDE_ONLY_SOURCES:
        by_url.setdefault(url, {'url': url, 'title': title,
                               'type': 'Existing hand-written source guide; not a new verified observation'})
    # Preserve explicit audit attempts and held research leads, including those
    # never promoted into a canonical event or source record.
    def public_url(value):
        if not isinstance(value, str): return False
        p = urllib.parse.urlparse(value)
        host = (p.hostname or '').lower()
        if p.scheme not in ('http', 'https') or not host or p.username or p.password or host == 'localhost' or host.endswith(('.local', '.internal')): return False
        keys = {k.lower() for k, _ in urllib.parse.parse_qsl(p.query, keep_blank_values=True)}
        if keys.intersection({'token', 'access_token', 'api_key', 'key', 'secret', 'password', 'session', 'auth', 'code'}): return False
        try:
            if not ipaddress.ip_address(host).is_global: return False
        except ValueError: pass
        return True
    # Intake is explicit: public new-source proposals remain unverified leads.
    discovery_dir = ROOT / 'research/source-discovery'
    if discovery_dir.exists():
        for path in sorted(discovery_dir.glob('*.json')):
            try: document = json.loads(path.read_text())
            except (OSError, json.JSONDecodeError): continue
            proposals = document if isinstance(document, list) else document.get('proposals', [document]) if isinstance(document, dict) else []
            if not isinstance(proposals, list): continue
            for proposal in proposals:
                if not isinstance(proposal, dict): continue
                context = {'title': str(proposal.get('name') or 'New source proposal')[:180], 'methodObserved': str(proposal.get('methodObserved') or 'unassessed')[:100], 'nextStep': str(proposal.get('nextStep') or '')[:400], 'researchFile': str(path.relative_to(ROOT))}
                for field in ('discoveryUrl', 'organizerOrFeedUrl'):
                    url = proposal.get(field)
                    if not public_url(url): continue
                    record = by_url.setdefault(url, {'url': url, 'title': context['title'], 'type': 'New source proposal; route and events unverified'})
                    contexts = record.setdefault('discoveryContexts', [])
                    if context not in contexts: contexts.append(context)
    audit_path = ROOT / 'data/source-audit.json'
    if audit_path.exists():
        audit = json.loads(audit_path.read_text())
        for record in audit.get('sources', []):
            for attempt in record.get('attempts', []):
                url = attempt.get('url')
                if public_url(url):
                    by_url.setdefault(url, {'url': url, 'title': f"Historical audit: {record.get('domain', '')}", 'type': 'Historical audit attempt; not a configured feed', 'checkedAt': audit.get('checkedAt')})
    for path in sorted((ROOT / 'research').glob('round*/**/*.json')):
        try: batch = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError): continue
        if not isinstance(batch, dict): continue
        for key in ('held', 'heldLeads', 'heldFindings', 'findings'):
            records = batch.get(key, [])
            if not isinstance(records, list): continue
            for item in records:
                if not isinstance(item, dict): continue
                for field in ('url', 'sourceUrl', 'bookingUrl'):
                    url = item.get(field)
                    if not public_url(url): continue
                    title = str(item.get('title') or item.get('name') or 'Held research lead')[:180]
                    reason = str(item.get('reason') or item.get('details') or '')[:400]
                    context = {'title': title, 'reason': reason, 'researchFile': str(path.relative_to(ROOT))}
                    record = by_url.setdefault(url, {'url': url, 'title': title, 'type': 'Held research lead; not a verified event'})
                    contexts = record.setdefault('heldContexts', [])
                    if context not in contexts: contexts.append(context)
    domains = {}
    for source in by_url.values():
        host = (urllib.parse.urlparse(source.get('url', '')).hostname or '').lower().removeprefix('www.')
        if host:
            domains.setdefault(host, []).append(source)
    return domains

def filename(host):
    return SPECIAL.get(host, host.replace('.', '-') + '.md')

def blocked_only(rows):
    host = (urllib.parse.urlparse(rows[0].get('url', '')).hostname or '').lower().removeprefix('www.') if rows else ''
    # A broad directory is not excluded just because its only saved link is
    # climbing. Only known dedicated providers can receive a domain-wide skip.
    profile = json.loads((ROOT / 'data/preferences.json').read_text())
    return any(host in BLACKLIST_DOMAIN_RULES.get(rule, set()) for rule in profile.get('blacklist', []))

def evidence_method(rows):
    found = []
    for row in rows:
        ev = row.get('evidence', '')
        if isinstance(ev, dict):
            for k, v in ev.items():
                if k in METHOD_KEYS and v:
                    found.append(f"{k}: {str(v).strip()}")
        elif isinstance(ev, str):
            for key in METHOD_KEYS:
                match = re.search(rf'{re.escape(key)}\s*[:=]\s*([^.;]+)', ev, re.I)
                if match:
                    found.append(f'{key}: {match.group(1).strip()}')
    return list(dict.fromkeys(found))

def render(host, rows):
    rows = sorted(rows, key=lambda s: (s.get('title','').casefold(), s.get('url','')))
    checked = sorted({s.get('checkedAt','') for s in rows if s.get('checkedAt')})
    latest = checked[-1] if checked else 'not recorded'
    lines = [f'# {host} source guide', '', f"Saved evidence checked through {latest}.", '',
             '## Saved entry pages', '']
    for s in rows[:12]:
        label = s.get('title') or s.get('type') or host
        lines.append(f"- [{label}]({s['url']}) — {s.get('type','type not recorded')}; checked {s.get('checkedAt','date not recorded')}.")
    if len(rows) > 12:
        lines.append(f'- {len(rows)-12} additional saved URLs for this domain are in `data/sources.json` or the linked research batch; this short guide shows a sample.')
    lines += ['', '## Evidence and route limits', '']
    methods = evidence_method(rows)
    if methods:
        lines.append('Saved evidence explicitly records these route/method details:')
        lines.extend(f'- {m}' for m in methods[:5])
    else:
        lines.append('Historical route unspecified in saved evidence. The URLs above are saved entry pages, not a verified navigation recipe.')
    lines.append('Exact agenda navigation and selectors remain unverified unless a saved source observation states them.')
    lines += ['', '## Recheck rules', '',
              '- Use public, actual date-selectable pages for dated records. A recurring weekly schedule or opening hours is not an occurrence; never expand recurrence.',
              '- Verify that a single visit is allowed for one person, the exact regular single-person price, and any eligibility conditions, class-booking requirements, rentals, or other extras. A gym day pass does not imply group-class admission.',
              '- Keep unknown prices, class inclusion, audience rules, language, dates, and availability unknown. Keep women-only, intro-only, member-only, or other conditions explicit.',
              '- Do not create accounts, book, pay, contact organizers, enter gated flows, or bypass access controls.',
              '- Apply the current profile settings when selecting offerings.']
    return '\n'.join(lines) + '\n'

def main():
    GUIDES.mkdir(parents=True, exist_ok=True)
    created, skipped, preserved = [], [], []
    for host, rows in sorted(load_sources().items()):
        name = filename(host)
        path = GUIDES / name
        if blocked_only(rows):
            skipped.append(host)
            if not path.exists():path.write_text(f'# {host} — excluded source\n\nSkip this source under the saved climbing/acrobatics blacklist. Historical evidence is retained in `data/sources.json`; do not spend research time here unless the user changes the profile.\n')
            continue
        if path.exists():
            preserved.append(name)
            continue
        path.write_text(render(host, rows))
        created.append(name)
    print(f'created {len(created)}; preserved {len(preserved)} existing guides; skipped {len(skipped)} blacklist-only domains')
    if skipped:
        print('blacklist-only:', ', '.join(skipped))
    for name in created:
        print(name)

if __name__ == '__main__':
    main()
