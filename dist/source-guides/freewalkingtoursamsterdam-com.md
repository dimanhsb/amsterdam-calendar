# Free Walking Tours Amsterdam

## Luna quick start · checked 18 October 2026

Open the Classic Tour page and inspect its published meeting times and fee model. Only use individually dated departures when the page displays dates.

1. Read the tour title and public departure schedule.
2. Copy exact dated departure time and meeting point if shown.
3. Keep tip-based/free status distinct from mandatory fees.
4. Stop if only recurring tour times appear.

Untested controls: Any filter, date picker, schedule link or booking control not explicitly recorded in the observations was not clicked during this audit.

Copyable prompt: “Using https://freewalkingtoursamsterdam.com/tours/free-classic-tour/, find individually dated public entries from {start_date} through {end_date}. Return only fields visibly stated: title, date, start/end, single-visit price, access and language. Mark missing values unknown. Keep missing date, price, access or language unknown. Stop after one bounded public-calendar attempt or at an account, login, booking, payment or security gate. Never infer an occurrence from recurrence.”


Official routes checked 18 October 2026:

- Classic tour: <https://freewalkingtoursamsterdam.com/tours/free-classic-tour/>
- Evening tour: <https://freewalkingtoursamsterdam.com/tours/free-evening-tour/>

The date picker on each official tour page renders the current month and individual departures. After the calendar loads, select only a date of interest; read the exact departure buttons and timezone label. On 24 October 2026, Classic displayed 10:30, 13:30 and 16:00; Evening displayed “No available departures on this date.” The Classic page was used to add only the 10:30 Saturday session. Do not click “Choose guests” if you only need event evidence.

Price is not simply free: the operator requires a €2 booking fee per person and says a guide tip is voluntary and separate. A reservation guarantees a place; the FAQ says walk-ins may be admitted if reserved guests do not show and space remains. The Classic and Evening pages explicitly identify English as tour language. The page says individual reservations are limited to six people; confirm remaining availability on the specific date.

The UI preview status was unavailable, so the public page was inspected in a separate headless desktop Chromium session. No login, guest selection, contact, booking or payment was attempted. If the widget is blank, record the selected date and blank/no-availability state; do not infer departures from the advertised tour time.


# freewalkingtoursamsterdam.com source guide

Saved evidence checked through 2026-10-18.

## Saved entry pages

- [Free Walking Tours Amsterdam FAQ · reservations and walk-ins](https://freewalkingtoursamsterdam.com/faq/) — official joining terms; checked 2026-10-18.
- [Free Walking Tours Amsterdam · Free Classic Tour](https://freewalkingtoursamsterdam.com/tours/free-classic-tour/) — official public tour and date-calendar page; checked 2026-10-18.
- [Free Walking Tours Amsterdam · Free Evening Tour](https://freewalkingtoursamsterdam.com/tours/free-evening-tour/) — official tour and public availability page; checked 2026-10-18.

## Evidence and route limits

Historical route unspecified in saved evidence. The URLs above are saved entry pages, not a verified navigation recipe.
Exact agenda navigation and selectors remain unverified unless a saved source observation states them.

## Recheck rules

- Use public, actual date-selectable pages for dated records. A recurring weekly schedule or opening hours is not an occurrence; never expand recurrence.
- Verify that a single visit is allowed for one person, the exact regular single-person price, and any eligibility conditions, class-booking requirements, rentals, or other extras. A gym day pass does not imply group-class admission.
- Keep unknown prices, class inclusion, audience rules, language, dates, and availability unknown. Keep women-only, intro-only, member-only, or other conditions explicit.
- Do not create accounts, book, pay, contact organizers, enter gated flows, or bypass access controls.
- Apply the current profile settings when selecting offerings.
