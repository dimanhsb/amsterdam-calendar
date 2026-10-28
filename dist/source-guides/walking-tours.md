# Walking-tour research guide

Use this guide for Amsterdam guided walking tours. Read each operator’s actual public listing, not a city directory or search snippet. Keep a walk undated unless an official date picker or organizer event page shows an exact date and departure. For a date-picker listing, select the date and record only the displayed departures; do not proceed into guest details, checkout, or booking.

For each source, record the official title, exact start and meeting point, duration if stated, public-versus-private joining terms, explicit spoken tour language, mandatory per-person fee, separate voluntary tip, booking requirement, availability wording, and evidence URL. A Dutch or English webpage does not establish the spoken language. A “free tour” with expected voluntary gratuity is `tip-based`, not `free`. A mandatory reservation fee plus voluntary tip remains `tip-based` with the required amount and the gratuity stated separately. Record whether booking guarantees a place and whether walk-ins are only conditional on no-shows or spare capacity. For a private group rate, do not imply that it is a public per-person offer.

## Verified routes

- [Free Walking Tours Amsterdam](freewalkingtoursamsterdam-com.md) — exact public calendar dates are selectable on the tour detail page.
- [FreeDam Tours](freedamtours-com.md) — overview and FAQ give daily time bands, English delivery and voluntary-tip/booking conditions; linked FareHarbor calendar did not render in web extraction during this pass.
- [Stadswandelkantoor](stadswandelkantoor-nl.md) — Open Rondleidingen page lists per-person offers, but its checked form showed no individual dates.

Gilde Amsterdam/Mee in Mokum was screened out for this preference: its official joining rule says solo customers walk only with their own party and are not added to another group. Existing IVN event pages were audited for language; retain unknown event languages unless explicitly stated.

## Cheap-model workflow

1. Search only official operator domains for `Amsterdam walking tour` plus a date or theme, then open the organizer’s own detail/agenda page.
2. Check existing event IDs before extracting a date. For each desired weekend/evening date, use the page’s visible date picker and collect only departures it displays for that date.
3. Confirm solo public joining from explicit booking rules. Mark private-only tours as such; do not treat a private per-group quote as a public join price.
4. Capture language only when the source says the tour is conducted in that language. Keep `languages: []` when language is unstated.
5. Separate fixed fee, mandatory booking fee, voluntary tips and suggested tip amounts. Do not use the organizer’s “free” label to erase a compulsory booking fee or expected gratuity.
6. If a widget fails to load or a selected date has no departures, record the exact route, method, result and next useful check. A zero-result date does not prove all dates are unavailable.
