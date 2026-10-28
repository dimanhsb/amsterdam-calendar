# Source priority and discovery

The operating order is **deterministic collection → Luna → harder review or rendering**. A source can appear in more than one queue because a historical Luna spot check does not prove code cannot handle it. Rate limits, robots rules and access controls always apply; using a browser or a different model is not a way around a restriction.

## 1. Code first

Run the configured public entry points using `scripts/collect-sources.py`. A successful extraction means code found candidate material, not that events were verified. If the latest attempt fails, retain the last good snapshot and obey backoff. Do not immediately escalate a transient timeout. Inspect public iCalendar/RSS feeds, APIs with permitted public access, JSON-LD, sitemaps and stable HTML before assigning an unconfigured site to model research.

The source queue is built from the saved source inventory, the current collector registry and run history, and the 18 October Luna audit. Explicit user priorities such as OBA, De Boomsspijker, Meetup, ClassPass, walks and Balfolk sort ahead of general sources within each queue. Historical event yield is only a secondary clue: it includes past events and may include duplicates; it is not a live success rate or a forecast.

## 2. Luna fallback

The Luna queue contains **candidates**, identified from usable or partial historical Luna-assisted checks. First make or review a permitted deterministic assessment. When code cannot reliably extract the needed information, give Luna one source and a small cached excerpt or a specific source page, plus `prompts/luna-source-refresh.md`. Record the actual method, date, access outcome, exact evidence and uncertainties. A past success does not guarantee current availability or prove all pages on a website work.

## 3. Harder or access-limited cases

Escalate unresolved date, price, eligibility or duplicate conflicts to a stronger review only after the cheaper route. Use an ordinary browser for a legitimate rendering gap and the already authorized bounded Android/Hermes route only where applicable. An account gate, denial, 429, or robots prohibition requires waiting, a permitted alternate source, or an authorized access path; it is not solved by trying a stronger model or bypassing the restriction. Historical blocked/unavailable records are leads for investigation, not proof an event exists or that Astra is required.

## Repeatable commands

```bash
python3 scripts/source-queue.py --queue deterministic
python3 scripts/source-queue.py --queue code_assessment --limit 20
python3 scripts/source-queue.py --queue luna --limit 20
python3 scripts/source-queue.py --queue harder --limit 20
python3 scripts/source-queue.py --find "balfolk" --limit 20
python3 scripts/source-queue.py --brief meetup.com --start-date 2026-10-28 --end-date 2026-11-02
```

These commands read local data and do not invoke a model or make network requests. Refresh the lists with `python3 scripts/build.py` after a collection run. To reprocess a saved raw snapshot without another website request:

```bash
python3 scripts/collect-sources.py --source pakhuis-agenda --reparse-run 20261028T083025097604Z --start-date 2026-10-28 --end-date 2026-11-30
```

A cached reparse is labeled with the original fetch time, not the reparse time, and does not prove the page is still current. See [collection and review](collection.md) for the cache, run history and importer boundary.

## Finding new sources

Use [the source discovery prompt](../prompts/discover-sources.md) and the discovery methods shown in Collection status. Start with saved ideas, providers and held leads before spending tokens on broad discovery. For a new provider, retain its public entry URL, how it was found, expected activity, relevant area, proposed code route, robots/access result, last check, model fallback and open questions. Proposals remain research leads until individually verified. Add a per-source guide and, when reproducible, a collector adapter; keep all failed attempts rather than silently dropping the lead.
