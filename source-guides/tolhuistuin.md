# Tolhuistuin event research guide

## Entry points and observed navigation

- Official agenda: <https://tolhuistuin.nl/agenda>
- Direct event page examples: [ONE FINE MESS](https://tolhuistuin.nl/evenementen/one-fine-mess-9), [English comedy opening night](https://tolhuistuin.nl/evenementen/its-getting-hot-in-here-comedy-opening-night-warming-up-festival), [Het Metabolisme van Verlies](https://tolhuistuin.nl/evenementen/ecologische-rouw-het-verlies-van-de-toekomst)
- Official address: <https://tolhuistuin.nl/contact>

Open the Agenda page and use its visible category and day filters or search field (“Zoeken: muziek, kunst, naam…”). Open each dated card and read the full event page. In this round, public Tolhuistuin pages loaded in a browser and gave exact dates, doors-open time, start/end where published, language, price, venue room, short activity description, and ticket link. Detail pages for Paradiso-partner concerts gave the partner name but no price or end time.

## Fields to capture

Record exact date and local start/end (Europe/Amsterdam), doors-open time separately from show start, venue room, address, language only when stated, audience/participation format, price, ticket provider, and registration requirements. An event page can give an exact start without an end; leave `end` null. Use the Tolhuistuin contact page for its street address, not guesswork.

## Ticket and access pitfalls

- “Met huisgenoot Paradiso” identifies a ticket partner; it does not state the ticket price or event end time. Keep those unknown unless a public partner page explicitly shows them. Do not proceed into checkout.
- “Gratis” is distinct from ticketed events. ONE FINE MESS is explicitly listed as free. Some pages mention PIN-only payments at the venue; this is not an admission fee.
- Doors-open and performance start are separate. Capture the program start as `start`; put doors-open in attendance notes.
- Event pages may give the language of the program, but do not infer language from an artist’s nationality or song genre. Age eligibility and beginner access are often unstated.
- Some listings are exhibitions or nightlife. Exclude general opening hours and events involving climbing, circus/acrobatics/aerial/pole, or AcroYoga. Record solo-social fit as an assessment, not an organizer claim.

## Extraction example

`It's Getting Hot in Here` → 2026-11-19, 20:30–22:30, Zonzij; doors 20:15; English-language stand-up comedy with an audience quiz/game round; €17.50. The event page states these fields directly. Audience interaction is a social-fit assessment; age eligibility is not stated.

## No-results and cheaper-model workflow

If the official agenda returns no matching event cards after date/category filters, record the checked filters and range, clear filters once, then inspect adjacent results before concluding no yield. A smaller agent can open the November 2026 event cards, keep only exact one-off dates within the horizon, read each official detail page, and compare normalized title/date pairs to `data/events.json` and prior research batches. Return the event URL and evidence for each field. Do not infer a recurrence occurrence from “every second Friday” alone, invent fees or end times, or assume spoken language, age, beginner suitability, booking access, or availability. Never call hidden/private endpoints or bypass a gate.
