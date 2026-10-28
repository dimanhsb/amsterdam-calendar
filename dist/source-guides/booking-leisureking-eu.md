# booking.leisureking.eu source guide

## Luna quick start · checked 18 October 2026

Open the saved AHAC public booking module. In the ordinary browser it redirected to a generic secure-connection screen; stop there and report the widget access issue.

1. Open the public module.
2. If only the “Beveiligde verbinding” screen appears, stop.
3. Do not enter a booking flow or infer dates/prices from a blank widget.

Untested controls: Any filter, date picker, schedule link or booking control not explicitly recorded in the observations was not clicked during this audit.

Copyable prompt: “Using https://booking.leisureking.eu/bm/ab3fc530c18df81c3718b7129276caac?lang=NL, find individually dated public entries from {start_date} through {end_date}. Return only fields visibly stated: title, date, start/end, single-visit price, access and language. Mark missing values unknown. Keep missing date, price, access or language unknown. Stop after one bounded public-calendar attempt or at an account, login, booking, payment or security gate. Never infer an occurrence from recurrence.”


Saved evidence checked through 2026-10-18.

## Saved entry pages

- [AHAC — LeisureKing booking module](https://booking.leisureking.eu/bm/ab3fc530c18df81c3718b7129276caac?lang=NL) — organizer booking widget; checked 2026-10-18.
- [AHAC — Open Atelier public product calendar](https://booking.leisureking.eu/bm/ab3fc530c18df81c3718b7129276caac/assortiment/88905?lang=NL) — organizer booking widget; checked 2026-10-18.

## Evidence and route limits

Historical route unspecified in saved evidence. The URLs above are saved entry pages, not a verified navigation recipe.
Exact agenda navigation and selectors remain unverified unless a saved source observation states them.

## Recheck rules

- Use public, actual date-selectable pages for dated records. A recurring weekly schedule or opening hours is not an occurrence; never expand recurrence.
- Verify that a single visit is allowed for one person, the exact regular single-person price, and any eligibility conditions, class-booking requirements, rentals, or other extras. A gym day pass does not imply group-class admission.
- Keep unknown prices, class inclusion, audience rules, language, dates, and availability unknown. Keep women-only, intro-only, member-only, or other conditions explicit.
- Do not create accounts, book, pay, contact organizers, enter gated flows, or bypass access controls.
- Apply the current profile settings when selecting offerings.

## Verified Android Firefox route — 18 October 2026

The public AHAC Open Atelier product is [88905](https://booking.leisureking.eu/bm/ab3fc530c18df81c3718b7129276caac/assortiment/88905?lang=NL). Normal Firefox Android VIEW navigation rendered the date selector. Decline optional translation, scroll below the month/year header, select an actual date, and read the **blue selected date**, `Geselecteerd`, `Tijdsblokken`, `Vrij`, and `Tarieven / Regulier tarief` with quantity 1. `Probeer een andere datum` returns to the month picker; its chevron advances the month. Stop before adding to the cart.

Individually verified: 23 Oct 19:30–21:30; 25 Oct and 1/8/15/22 Nov 13:00–15:00. Regular tariff €59 each, before checkout. This yielded five new occurrences and promoted the existing 23 Oct lead. A tap intended for 29 Nov left 22 Nov selected: it yielded no additional event. Never use the intended tap or filename as proof.

October context, 25 Oct date/time/price, 23 Oct, November context, 1 Nov. Inventory is a dated observation, not a reservation. Start with the remaining individual dates next time; do not infer Sundays.
