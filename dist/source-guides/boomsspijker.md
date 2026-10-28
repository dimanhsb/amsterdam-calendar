# De Boomsspijker event research guide

## Entry points and proven route

- Official venue agenda: <https://huisvandebuurtdeboomsspijker.nl/agenda/kalender>
- Official venue activity/detail listings are hosted by WijkConnect. Example: <https://www.wijkconnect.com/amsterdam/organisaties/8345/huis-van-de-buurt-de-boomsspijker/agenda/26159/film-dineravond-buurtbewoners>
- Public category agenda used to verify a dated November occurrence: <https://www.wijkconnect.com/amsterdam/centrum-oost/agenda/film>

On the venue calendar use the visible month arrows, then inspect the event's title link. The calendar exposes a filter box, date period, event tags and audience categories (including “Volwassenen”). The dated film category page listed “Film & Dineravond buurtbewoners — Vr 13 nov 20:00”; its detail page independently states the second Friday monthly schedule and 20:00–22:00 duration.

The October calendar and detail pages loaded in a public browser. A direct November month query on the venue calendar returned an access-denied page; the public category agenda still displayed explicit November dates. Do not work around a gate. Search the public site by title or use its public category pages instead.

## Capture fields

Capture exact dated occurrence, start/end, venue and address, audience categories, one-off versus course/recurrence, whether a solo visit is welcomed, whether the activity is open inloop or signup/list required, contact/booking URL, fee and what it covers, event language, and date evidence. Mark unknown price or language as unknown. The venue is Recht Boomssloot 52, Amsterdam; verify event-specific details on each listing.

## Booking, recurrence, and fee pitfalls

- The calendar mixes adult, senior, youth, children, courses, recurring groups, and isolated events. Check the explicit “Wie” section; do not infer eligibility from a title.
- Do not expand a weekly class into multiple calendar recommendations. A visible recurrence is not proof that a newcomer can drop in or attend just once.
- Some social meals require an email and guest-list spot. For Film & Diner, the detail page says €15.50 per person and names the email address; do not assume that price covers a specific film or menu not yet published.
- A month calendar can be inaccessible while the corresponding public category page remains readable. Record this distinction and the route that supplied the exact date.
- Exclude recurring language courses, choir rehearsals, fitness classes, and anything involving circus/aerial/pole/acrobatics. Do not assume English access or beginner suitability.

## Extraction example

`Film & Dineravond buurtbewoners` → 2026-11-13 20:00–22:00, De Boomsspijker, Recht Boomssloot 52; venue detail page says adults/seniors, three-course dinner before a film, contact `dinerfilm@gmail.com` for guest-list placement, €15.50/person. The public Film category page explicitly lists Friday 13 Nov at 20:00. November’s exact film and menu were not stated.

## No-results and cheaper-model workflow

If the calendar month route is denied, stop retrying it. Search the venue's public category listings (Film, Eten, Cultuur, Ontmoeten, Reparatie) and inspect the event detail pages for in-range one-off dates. A smaller agent should return at most one record per distinct event/date, no weekly expansion, and include a page URL and short fact-to-source evidence. Dedupe on normalized title, venue, and local date against `data/events.json`. Do not guess date, fee, language, open access, or adult eligibility.

The 13 November film/dinner listing publishes 20:00–22:00. Confirm the preceding three-course dinner's arrival time when joining the guest list; no earlier meal start was verified.
