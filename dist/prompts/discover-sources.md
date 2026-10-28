# Find and assess new Amsterdam activity sources

Find reusable public sources for the existing Amsterdam drop-in calendar. This is source discovery, not an instruction to invent dated events or schedule model calls.

1. Read `data/preferences.json`, `source-guides/priorities.md`, and the source inventory. Search locally first with `python3 scripts/source-queue.py --find <term>`. Include older held and idea/provider leads; preserve their uncertainty.
2. Prioritize public entry points for OBA Oosterdok, De Boomsspijker, walking tours, accessible dance and other independent social activities. Search in Dutch and English by provider, neighborhood, venue and activity; follow a directory listing to an organizer. Record discovery and organizer URLs separately. Avoid duplicate providers and closed or out-of-area sources.
3. Before model extraction, test permitted public structured data: iCalendar, RSS, official public APIs, JSON-LD, sitemaps and stable HTML. Use the existing collector's robots rules, rate limits, snapshot and run-history conventions. Do not guess endpoints, bypass restrictions, create accounts, RSVP, pay or contact organizers.
4. If a permitted deterministic route cannot supply the relevant facts, use Luna for one source with a short guide and the smallest relevant cached input. Escalate only unresolved evidence, conflicting facts or ordinary rendering gaps. Record unsuccessful routes and avoid describing a historical audit as a current test.
5. Save a structured proposal per source with the fields below. `verified` applies only to the route actually observed; unknowns remain unknown. Do not write event records until individually verified and reviewed through the importer.

```json
{
  "name": "Provider or directory",
  "domain": "example.org",
  "discoveryUrl": "https://example.org/",
  "organizerOrFeedUrl": null,
  "activityAndArea": "",
  "discoveredAt": "YYYY-MM-DD",
  "methodObserved": "unassessed",
  "codeRoute": "unassessed; proposed page/feed/API and access conditions",
  "lunaFallback": "unknown; what one small check should answer",
  "escalationReason": null,
  "robotsAndAccess": "not checked",
  "evidencePaths": [],
  "duplicateOf": null,
  "unknowns": [],
  "nextStep": ""
}
```

Add the proposal to a dated `research/source-discovery/` file, retain exact evidence and failed attempts, update the per-source guide, and refresh the source inventory and priority report. Events must meet the saved blacklist and preferred-time rules; distinguish one-off access from a course, free from tip-based or donation admission, and the spoken language from the webpage language.
