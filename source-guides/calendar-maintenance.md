# Calendar updates and retention

Updated 20 October 2026 · version 0.9.0

## Updating

1. Read the source-specific guide and verify actual dated occurrences, prices, spoken language and joining conditions. Keep original evidence in `data/events.json` and `research/` so a later run can recognise duplicates and audit source yields.
2. Update coverage dates in `data/meta.json` when researching a new period. Never invent dates from an undated recurring schedule.
3. Run `python3 scripts/build.py`, then `node scripts/check.mjs`.
4. Check day navigation and offline loading when changing app code. Publish with the Sites source helper and preserve the existing private audience.

## Past events

The build automatically excludes dated events whose Amsterdam end date has passed (start date when no end is known). An overnight event is retained until its end date passes. Leads with a past proposed date are excluded too. Today is kept in full, allowing planning and avoiding guesses about unknown end times.

This removes the entire expired event record from `dist/data.json`; it is not merely hidden by CSS. In between publications, the browser applies the same cutoff each time the view renders, after midnight and when the installed app returns to the foreground. Past dates are excluded from filtered exports and saved counts.

Canonical research in `data/events.json`, `data/sources.json` and `research/` remains the local historical archive. It is not copied into the published event payload. Source and idea knowledge is retained because it helps future research. Research report counts are historical totals, labelled separately from the live calendar.

Use `CALENDAR_AS_OF=2026-11-01 python3 scripts/build.py` only to test a future cutoff. Rebuild without the override before publishing. The build records `publishedAsOf` and `archivedPastCount` in live metadata. The checker verifies the exact live subset against the retained research; historical research targets still use the full canonical data.

No scheduled refresh is configured. Each publication trims the payload; the browser continues hiding dates that expire after that publication. Once coverage ends, it shows no verified listings rather than reviving expired ones.

## PWA and cache

The manifest supplies standalone display and 192/512 icons. The service worker caches only an explicit allowlist of same-origin app assets and the latest event payload. Booking links, authentication redirects, failed responses and unrelated pages are never cached. Network responses remain authoritative; cached data is used when a request fails offline.

Every build hashes the app assets into a new cache identity. New versions show an Update available button; accepting it activates the new worker and reloads. Activation removes previous app caches, replacing old event payloads on that device. Browser storage may be cleared or evicted by the operating system; offline availability requires at least one complete online load.

On Android Chrome, use the browser menu → Install app / Add to Home screen. An in-app Install app action appears under More when the browser offers it. On iOS Safari, use Share → Add to Home Screen. Browser installation and the existing private Site sign-in remain browser-controlled.

Implementation references: [MDN installability](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable), [MDN offline operation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation).

### Private-site installation regression (0.9.1)

A private Site must use `<link rel="manifest" ... crossorigin="use-credentials">`. Without this, Chrome omits the session cookie even on a same-origin manifest fetch; the authenticated page works while installation fails. Public/local preview alone cannot establish installability. [MDN documents this requirement](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest).

`node scripts/check-installability.mjs` checks the built app behind a real cookie gate in a fresh, non-incognito Chromium profile. It must report zero installation errors. Use an existing Playwright installation via `CALENDAR_PLAYWRIGHT_MODULE` and, if needed, `CALENDAR_CHROMIUM_EXECUTABLE`. The fixture uses an ephemeral local port and synthetic test cookie, then removes its temporary browser profile. It neither signs into ChatGPT nor changes Site access. On 20 October 2026 the uncorrected app reproduced `manifest-parsing-or-network-error` and missing name/display/icon errors; the corrected app passed.

### Refreshing an audited source guide

The 18October source audit is historical evidence: do not rewrite its original results or changed flags after editing a guide. Record later guide revisions in `research/source-audit/guide-followups.json`, keyed by domain, with `checkedAt`, SHA-256 of the final guide bytes, a reason and concise `quickStart` steps. Keep the guide's `Luna quick start` heading near the top and reusable `{start_date}` / `{end_date}` placeholders. The build validates the follow-up fingerprint while preserving historical audit totals. Round8 provides examples for Meetup and ClassPass.
