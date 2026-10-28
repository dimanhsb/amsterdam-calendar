# Hipsy event research guide

## Luna quick start · checked 18 October 2026

Open the event page and select the single-date ticket only if it is visibly offered. This public page lists four Saturday sessions and a separate per-session price.

1. Read the individual workshop dates and start/end.
2. Copy the single-class price, not the series bundle.
3. Stop if only a package or account/checkout gate is shown.

Untested controls: Any filter, date picker, schedule link or booking control not explicitly recorded in the observations was not clicked during this audit.

Copyable prompt: “Using https://hipsy.nl/event/257835-moving-dialogues-contact-improvisation-workshop-steven-campos, find individually dated public entries from {start_date} through {end_date}. Return only fields visibly stated: title, date, start/end, single-visit price, access and language. Mark missing values unknown. Keep missing date, price, access or language unknown. Stop after one bounded public-calendar attempt or at an account, login, booking, payment or security gate. Never infer an occurrence from recurrence.”


## Entry routes

Use Hipsy event search as a discovery route, then open the exact canonical event URL without a `source=` tracking query before recording it. Useful search patterns observed in this pass:

- `site:hipsy.nl/event Amsterdam singing circle November 2026`
- `site:hipsy.nl/event Amsterdam drum circle November 2026`
- `site:hipsy.nl/event Amsterdam game night November 2026`
- `site:hipsy.nl/event Amsterdam connection games November 2026`

Examples checked directly:

- https://hipsy.nl/event/249752-ura-tsur-singing-circle-xl
- https://hipsy.nl/event/238493-nataraj-24-years-one-day-festival
- https://hipsy.nl/event/207276-drumcirkel
- https://hipsy.nl/event/236113-cozy-gamenight
- https://hipsy.nl/event/242605-playfight-introduction-circle

## Observed navigation and extraction

1. Search Hipsy for a format plus Amsterdam and the target month; use snippets only to discover candidates.
2. Open the canonical event page. The page header provides event date, listed hours, venue/address, and visible ticket categories. The event description often supplies the actual activity schedule, standalone status and participation language.
3. Compare the title/date/ID against canonical `data/events.json` and every existing round file before considering a record. Hipsy cards list related events; follow only exact individually dated links that could be useful. Do not create dates from “every Tuesday” or “monthly” copy.
4. Record organizer claims literally, then separately assess social fit. A shared activity may offer natural interaction without proving that people attend alone, that introductions happen, or that community continues.

Example extraction: Drumcirkel's exact event page lists Fri 13 Nov, 19:30–21:30, Plantage Muidergracht 39, 18+ and Dutch/English/German. Its prose states a €17 contribution and says reserve drums are available, while Hipsy's visible ticket total is €17.80. The event record preserves both amounts rather than silently reconciling them.

## Ticket and date pitfalls

- Hipsy ticket cards can show a price that differs from the organizer's contribution, likely due to platform charges. Report the displayed amount and the organizer's text separately where they conflict.
- “First tickets” may be an early tier rather than the current standard amount. A free “Waitlist” is not a free entry ticket. Leave the standard price unknown if a normal paid tier is not shown.
- Discount and super-discount tiers have conditions. State the regular ticket as standard and preserve discount eligibility in a note; do not call the lowest amount the usual price.
- Add-on meals, bundles and partner tickets are separate purchases. Do not combine them with the standard event ticket.
- Check the day name/date and the event body. If the header and body conflict, or search cards for the same ID show another date, report the mismatch and stop unless the exact page resolves it.
- Events that pass midnight need an end timestamp on the next calendar date. On 14 November 2026 Amsterdam uses CET (`+01:00`). Before DST ends on 25 October it uses CEST (`+02:00`).
- A Hipsy event page can be technically inaccessible or return a cache miss. Do not use that as evidence that the search snippet has been independently confirmed. Record the failed exact-page attempt and leave the item out until an official page can be read.

## Stopping rule

Only create a dated record when the exact official event page visibly establishes the occurrence date and start time, Amsterdam venue, and enough format detail to classify participation. Keep unknown address, language, end time, price or solo welcome explicit. Exclude out-of-city listings, recurring courses, application-only events with undisclosed location, and identity/age/partner restrictions that do not fit the requested audience. For weekly/monthly formats, include only a specifically listed standalone occurrence and never expand a cadence into a series of dates.

## Cheap-model replay

Open Hipsy search results only to discover candidate exact event pages. Compare Hipsy ID and date with canonical events and prior round JSON files, then inspect the exact page. Extract date, start/end, address, language, ticket types, organizer price wording, attendance requirements and interaction format. Keep `sourceUrls` as URL strings in event records and place `{title,url,type,evidence,checkedAt}` objects in the batch `sources` array. Write an `attempts` entry for each organizer/domain, including inaccessible pages and ambiguous prices or dates. Do not book, message organizers or enter an account.
