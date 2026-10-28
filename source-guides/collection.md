# Source collection and review

This pipeline collects public source material with ordinary Python and no model calls. It does not create or update calendar events. Review is needed before any candidate enters the existing importer.

## What is saved

- `data/collector-sources.json` is the explicit registry of enabled collection entry points and their adapters. A recorded evidence URL is not automatically an enabled collector.
- `data/collection-runs.json` records each attempted source, outcome, HTTP status where known, counts, date window, hash and concise public candidate links. Run history is retained.
- `.collector-cache/runs/<run-id>/` holds the original public HTML, candidate JSON including article excerpts, and the run record. `.collector-cache/` is ignored by Git and is not included in the Site. The cache lives on the machine that ran collection; a published status is not proof the local raw file exists on another machine.
- `data/collection-status.json` is generated from the source-guide inventory, saved research, historical audit attempts, structured held leads, public `research/source-discovery/*.json` proposals, and run history. It lists saved domains and references, including ideas and provider leads; the Site shows a compact status and links. A historic browser or search result is evidence of a past attempt, not proof that a repeatable collector exists.

## Run the collector

```bash
python3 scripts/collect-sources.py --start-date 2026-10-28 --end-date 2026-11-30
python3 scripts/collect-sources.py --source station-west-music --start-date 2026-10-28 --end-date 2026-11-30
python3 scripts/build.py
node scripts/check.mjs
```

The default is all enabled entries and today through 30 days ahead in Amsterdam time. The collector checks public `robots.txt`, enforces its crawl delay across runs, uses timeouts and a response-size limit, and stops on access errors without bypassing them. A long crawl delay is recorded as `deferred_rate_limit`; retry later. No accounts, browser sessions or credentials are used. Adding a new website requires a reviewed registry entry and an adapter, followed by a real run. No scheduler or live refresh is configured.

`success` means the public page was fetched and the adapter matched at least one candidate; it does **not** mean dates, prices, attendance rules, places or the event's continued existence have been verified. `no_matches` is a fetched page with no adapter matches and may indicate a changed page layout. `robots_disallowed`, `robots_unavailable`, `http_error`, `fetch_error`, `parser_error`, `unexpected_content` and `deferred_rate_limit` are distinct outcomes. Previous successes remain in run history if a later attempt fails; the status page labels and shows candidates from the last successful attempt. Raw cache files have no automatic expiry and can be deleted locally when no longer needed.

## Source priority and low-cost handoff

The [priority and discovery guide](priorities.md) orders configured code collectors and code feasibility assessments before Luna fallback, with a separate queue for harder or access-limited cases. The queues may overlap: a historical Luna spot check does not establish that code cannot work. `scripts/source-queue.py` prints these queues, searches saved leads locally, and generates compact source-specific Luna briefs without making model or network calls. `--reparse-run` reuses a local hash-checked snapshot without refetching it, while recording its original fetch time.

## Source-specific outputs

- Station West: the calendar adapter groups date-specific event links and their displayed title, date, time and price text. The original HTML and every candidate are saved locally; date filtering never removes the raw page. Verify the detail page, language, single-visit eligibility, availability and time preference.
- Buurtkamer Corantijn: the WordPress adapter extracts article titles, URLs, **publication** dates and excerpts. A publication date is not an event date. Read the article to find a real occurrence and verify its details.
- Pakhuis de Zwijger and De Boomsspijker (WijkConnect): adapters extract programme or activity leads from their agenda cards; textual schedules or recurrence are not expanded into dated events. The current successful extractions were reparsed from cached pages.
- OBA: an agenda-link adapter is configured but not yet verified; the 28 October robots request returned HTTP 429. Observe backoff and do not bypass the rate limit.

## Turn leads into calendar records

1. Inspect the current run's `*.candidates.json` and original `.html`, starting with dates in the user's requested window and relevant ideas. Existing guide and audit links are listed in **More → Collection status**.
2. Use deterministic source-specific extraction where it is reliable. For ambiguous prose, dynamic pages or gated content, use the existing short source-check prompt and, where appropriate, an authorized browser/model. Do not assume that every unconfigured source requires a model.
3. Confirm exact dates, Amsterdam timezone, venue, spoken language, price, single-visit access, availability and blacklist/time preferences. Keep missing details unknown. Check existing event IDs and source URLs for duplicates.
4. Save a batch using `source-guides/batch-template.json`, preview with `python3 scripts/ingest.py path/to/batch.json`, review the result, then apply. Build and publish normally. A successful fetch, model observation, or candidate count alone is not a verified event or automatic import.

The website inventory includes evidence pages, research batch links, explicit audit-attempt URLs, structured held-lead URLs, idea and provider URLs, and guide-only sources. Held reasons remain labeled; free-text leads without a structured URL may still need manual review. Some are individual event citations rather than recurring feeds. The 18 October audit is historical and incomplete for later-added domains; **not assessed** is not a failure.
