# Meetup — public dated event source

Refreshed 21 October 2026. Public event detail pages worked in a normal desktop browser without signing in. This round proposes seven new dated records; the cumulative source report includes earlier Meetup research too.

## Luna quick start · public browser route

1. Start from a public group calendar or a topic search, e.g. [Amsterdam events](https://www.meetup.com/find/nl--amsterdam/) or [a tested discovery page](https://www.meetup.com/find/nl--amsterdam/python/). Search results can include unrelated recommendations; evaluate every event individually.
2. Open the actual `/GROUP/events/ID/` page. Remove `recId`, `searchId` and other tracking query parameters from stored links. Public English and `nl-nl` URLs may identify the same event: deduplicate by event ID and occurrence, not locale URL.
3. Read the visible browser title for the year, and the event header for date/time and timezone. Use Europe/Amsterdam as the browser timezone. Search snippets can be stale or show another viewer's timezone.
4. Read the full Details section and attendance/price card. Record venue, address, standalone access, price, joining method and explicitly stated spoken language. English page text alone is not evidence of English delivery.
5. Follow a public organiser ticket link for the real price and location. Do not RSVP, sign up, select tickets, register or pay. Keep any account requirement explicit. If dates conflict, hold the occurrence or explain the authoritative correction with evidence.
6. Reject private groups with member-only venues, generic recurrence, unavailable/cancelled events, or unverified save-the-dates. An explicitly dated occurrence in a repeating series is usable; never generate additional occurrences from the recurrence statement.

The privacy notice has a visible **Continue without accepting** action. Use it to decline optional tracking. T3 preview was explicitly unavailable due host AppArmor; normal desktop Chromium rendered the inspected public pages. This is not a guarantee that every Meetup group is public.

## Known traps from this round

- [Lithography · 24 October](https://www.meetup.com/nl-nl/inked-lines/events/316633363/): description says €50 per person / €90 for two; footer says Gratis. Keep the price conflict explicit and exclude it from free-price filtering.
- [Kooch Halloween · 30 October](https://www.meetup.com/koochcommunity/events/316865846/): footer Free and header end21:30 conflict with [linked official Luma tickets](https://luma.com/kooch-rqab). Luma gives DB55,19:30–23:00 and General€18.15. Member/earlybird/late tiers differ; drinks extra.
- [Public speaking · 7 November](https://www.meetup.com/nl-nl/storytelling-writing-workshops-amsterdam/events/316281495/): paid workshop; an unstated amount is not free.
- [Being Human · 14 November](https://www.meetup.com/nl-nl/the-passionate-philosophers/events/317013484/): Meetup RSVP does not reserve a place. The linked Hipsy page gives regular€25.80 (early€15.80, late€35.80) and explicitly English; Meetup’s€15 is not the current regular price.
- [Coaster & Jar Making · 20 November](https://www.meetup.com/nl-nl/amsterdam-creative-workshops/events/316634437/): individual workshop, amount shown on event card.
- [Swing social · 26 November](https://www.meetup.com/nl-nl/swing-dance-amsterdam/events/316211592/): “FREE ENTRY — donation based” wording must remain visible; whether a contribution is expected is not specified. Store as donation/unknown amount, rather than promising unconditional free admission.
- Processing Community Day has a13:00 overall window and13:30 programme start. It already exists in the calendar: annotate rather than duplicate.

## Copyable prompt

“Open {public_event_url} in a normal browser set to Europe/Amsterdam. Return only visible facts: exact event year/date/start/end/timezone, title, venue/address, price and mandatory extras, whether a solo first-timer can attend once, joining/account requirements, and explicitly stated spoken language. Read both Details and the price card, and follow any public organiser ticket link. Mark missing values unknown; flag contradictions. Do not infer English from webpage language or free entry from a generic RSVP label. Stop at private membership/login/security gates. Do not RSVP, register, message, book or pay. Match {start_date}–{end_date} and deduplicate against saved event IDs before proposing an addition.”

For ingestion use `scripts/ingest.py` and the `research/iterations/round-8-*.json` examples. See [calendar maintenance](calendar-maintenance.md) for past-date trimming and publication.
