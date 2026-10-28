# OBA event research guide

## Entry points and proven route

- Official agenda landing page: <https://oba.nl/nl/agenda>
- Official full agenda: <https://oba.nl/nl/agenda/volledige-agenda>
- Oosterdok event example and date list: <https://oba.nl/nl/agenda/open-podium-met-jos-van-hest-65aa9e1d-5f14-4f53-931b-b5b70c613961>
- Full agenda filter observed in a browser: `https://oba.nl/nl/agenda/volledige-agenda?Wanneer=d_thismonth&page=6&query=Oosterdok`

Use the full agenda page's visible “Waar” location filter to select OBA Oosterdok and set the desired date window. It exposes a searchable list with title, exact date, start/end, venue room, event type, and a short description. Open each result's official detail page and read it before capturing details. Example: searching the calendar for `Oosterdok`, then opening “Open Podium met Jos van Hest,” showed two forthcoming 2026 dates, 31 Oct and 28 Nov, 14:00–16:00.

The OBA page opener can return 403 while a public browser loads the same page successfully. On this run T3 preview reported `available:false`; an isolated public Playwright page returned HTTP 200 for official OBA pages. Use an ordinary browser session, no login. Do not try hidden APIs or bypass access controls.

## Capture fields

For each occurrence capture: exact date, start and end (and Europe/Amsterdam UTC offset), venue/location and room, event type, activity description, age restrictions, spoken/written language, whether audience can attend solo, signup or ticket route, stated fee, membership requirements, and remaining-capacity status only if visibly stated. Record unknowns as unknown. OBA event pages may distinguish regular price and reduced OBA-member price; do not use a membership rate as the default.

## Date, booking, and fee pitfalls

- The main agenda filter may show only a page of results; paginate or narrow dates rather than assuming the first page is complete.
- Detail pages can show a recurring schedule plus several individual dates. Capture only explicit dates inside the requested horizon and dedupe against existing event data.
- Some OBA programs require a ticket while others say “Aanmelden is niet nodig.” Audience attendance and performing/presenting are different: Open Podium does not require audience signup, but readers should email ahead and perform only their own Dutch-language work.
- Do not treat membership benefits as a free public event; distinguish free, paid, member-discount, donation, and unknown.
- OBA pages list children’s events and recurring services alongside adult events; check age/category text and exclude generic opening hours, exhibitions, youth events, and services.

## Extraction example

`Open Podium · OBA Oosterdok` → 2026-10-31 14:00–16:00, OBA Forum, Oosterdokskade 143; audience signup not needed, fee unstated; prospective readers email the organizer, texts must be self-written and in Dutch. A separate 2026-11-28 occurrence is explicitly listed. Audience language was not stated, so do not promise English support.

## No-results and cheaper-model workflow

If filtering yields no suitable items, record the checked date range and filters, inspect adjacent result pages once, then stop. A smaller agent can do the next pass cheaply: open the full agenda, filter to OBA Oosterdok and 19 Oct–30 Nov 2026, inspect only event detail pages that fall in that window, capture the fields above, and compare normalized title/date pairs against `data/events.json`. Do not infer language, age, drop-in access, price, dates from a weekday rule, or capacity. Return only source URLs and concise evidence for each claim.

## Pagination observed in round 2

On the official full-agenda page, search for `Oosterdok` in the visible search field. The result list has buttons labelled `Ga naar pagina 2`, etc. Click those controls rather than guessing a month query. The observed public URL pattern after using the control was `https://oba.nl/nl/agenda/volledige-agenda?query=Oosterdok&page=2` (increment the page number only after observing/clicking the corresponding button). In the checked October–November 2026 search, pages 1–10 contained entries through Saturday 28 November; page 11 started in December and page 12 showed March 2027. The visible date radios offered “Morgen” and “Volgende week”; an assumed `Wanneer=d_nextmonth` query returned no entries, so it must not be treated as evidence of an empty November.

When a card repeats across adjacent pages, dedupe by canonical event URL and local date. Inspect every in-range event detail: the list mixes adult gatherings with service appointments, canceled sessions, youth items, exhibitions, and silent study. For identical title/description cards at different times, preserve the exact published slots and flag possible duplicate sessions for review instead of combining their times.
