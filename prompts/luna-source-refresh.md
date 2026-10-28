# Simple Luna event research prompt

Use one named source or a small related source group per agent. Save after every verified result. Parent reviews, deduplicates, builds the canonical event schema and publishes.

## Copyable brief

Research **{source_name}** for Amsterdam standalone adult activities during **{start_date}–{end_date}**, with priority on **{priority_dates}**. Read its saved guide and search existing event IDs before calling a finding new. Apply the current profile settings when relevant. Check single-visit conditions and special eligibility.

Use public search/fetch. At security/account/transaction gates, stop and record the actual limit. Do not sign in, RSVP, contact, book or pay. Do not infer a year from “upcoming” or copy weekly recurrence into future dates. An image filename, book-publication year or page-update year does not prove the event year.

Save **flat facts** with named fields, not a long positional constructor:

```json
{
  "recordType": "new_candidate_or_existing_refresh",
  "existingEventId": null,
  "title": "Exact activity title",
  "sourceUrl": "https://organizer.example/exact-event",
  "sourceMethod": "web-extraction",
  "checkedAt": "YYYY-MM-DD",
  "date": "YYYY-MM-DD",
  "startLocal": "HH:MM",
  "endLocal": null,
  "venue": "Exact branch or meeting venue",
  "address": null,
  "ordinaryPriceEUR": null,
  "priceKind": "unknown",
  "mandatoryExtras": "Unknown unless explicitly stated",
  "spokenLanguages": [],
  "singleVisitConditions": "What the source actually says",
  "availability": "unchecked",
  "dateEvidence": "Actual displayed full year/date and time",
  "priceEvidence": "Observed ordinary price; distinguish restricted or collection-wide prices",
  "languageEvidence": "Explicit spoken delivery or participant requirements",
  "uncertainties": [],
  "evidencePath": "your-owned-evidence-file-if-created"
}
```

For a refresh, retain the original ID and instant and describe each freshly verified fact. If a field was not rechecked, say so. A known source URL is not proof of a fresh price. Keep regular ticket cost separate from early-bird, member, under-30 and introductory tiers. A collection-wide “from” amount is not the verified price of a specific session. Free workshop admission with unresolved required museum entry has an unknown total.

Save `attempts`, `candidates`, `refreshes`, `ideas` and `held` sections and a short source-steps MD. Output counts distinguish genuinely new occurrences from corroborations, corrections and undated leads. Validate that the JSON parses, but do not describe parsing alone as full schema or evidence validation.

## Local runner troubleshooting

If an authorized read fails with `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`, use the execution tool's explicit escalation mechanism where available. Do not treat a local sandbox initialization failure as a website failure. Do not alter host security or replace the model/tool with another system. If escalation is unavailable or rejected, save the exact limitation through a permitted write tool and continue public research that does not need the shell. A failed shell alone does not prevent all public web research.

## Parent conversion and validation

Use dictionary keys when converting facts into `scripts/ingest.py` records. Check URL strings, numeric-or-null prices, boolean `from`, ISO language-code arrays and real evidence paths. Deduplicate by the actual occurrence, including translated URLs, venue aliases and organizer/Meetup copies. Never change a published instant automatically. Use the ingestion dry run, then apply reviewed full updates with `--allow-updates`. Build and run the existing data checker before publication.
