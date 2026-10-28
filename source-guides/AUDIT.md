# Luna source-guide audit

Checked 2026-10-18 with `gpt-6-luna`.

113 websites reviewed: 108 live public-page attempts and 5 guide-only blacklist exclusions. 51 guides needed easier instructions; 53 guides revised; 18 routes retested.

Live outcomes: 49 usable, 40 partial, 4 blocked, 15 unavailable. 0 prompt issues remain without a guide revision.

Snapshot of the 18 October inventory of 113 websites; later sources are outside this audit. One or more public-page spot checks per allowed website, not an exhaustive check of every page or event. Web extraction can return cached content; a check made today does not establish page freshness. Usable means at least one evidence packet was extracted; partial means important fields or navigation remain unresolved. Blocked means a gate prevented access. Unavailable means no useful packet or only a stale/out-of-range entry was reached; neither proves the website has no events. Guide-only exclusions were not browsed. Android Firefox recommendations were not tested in this audit. No calendar dates, prices or availability were changed by this audit. Later guide edits are recorded separately in guideFollowups; historical audit counts remain unchanged.

## How to reuse this audit

Open the source guide and use its short Luna quick start with a fresh date window. Work on one source at a time. Keep failed access separate from unclear instructions; do not send a model around the same blocked route repeatedly. The live observations below are examples of what was visible on the audit date, not current event availability.

[JSON audit](source-audit.json) · [Source workflow](README.md) · [Website event yield](REPORT.md)

## All source assessments

| Website / guide | Original prompt | Guide revised | Live result | Best tested method | Issue / next step |
| --- | --- | --- | --- | --- | --- |
| [activiteiten.amsterdam.nl](activiteiten-amsterdam-nl.md) | easy | No | usable | web-extraction | Direct saved detail pages expose the title, occurrence date/time, description, price, audience and location in one short page. Use the saved direct event URL and copy only explicitly displayed fields. |
| [adc.trainin.app](adc-trainin-app.md) | needs_simplification | Yes | unavailable | desktop-browser | The original guide had no short route/copy prompt. The public schedule widget loaded with title ADC but an empty body in the ordinary browser; no date or class fields were readable. This is a rendering limitation, not a security denial. Use the FAQ only for displayed single-class/level facts; leave class dates unavailable until the public schedule widget renders. |
| [agalab.nl](agalab-nl.md) | easy | No | usable | web-extraction | Direct workshop page exposed a dated 21 Nov session and price; route is simple. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [amsterdam-dance-event.nl](amsterdam-dance-event-nl.md) | easy | No | usable | web-extraction | The saved event page puts title, exact date/time, venue, target audience and cash price together in the main content. Use the saved event page and preserve the stated audience and cash-only price. |
| [amsterdam.knnv.nl](amsterdam-knnv-nl.md) | needs_simplification | Yes | usable | desktop-browser | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Direct event page is understandable once the visible “Datum & tijd” section is identified. The detail page exposes one complete dated walk packet; use it and keep fee unknown because none is stated. |
| [amsterdam.nl](amsterdam-nl.md) | needs_simplification | Yes | partial | web-extraction | Price page is direct, but exact swim/class times are on a separate Rooster link; the guide did not explain this split. The tariff is verified, but the Rooster page exposed no session rows and the city-site browser presented an automated-traffic block; use the official live pool timetable later or choose a venue with a readable dated roster. |
| [amsterdambookclub.com](amsterdambookclub-com.md) | easy | No | usable | web-extraction | Homepage directly displays its English-language format, solo attendance welcome, next discussion date and RSVP path. Use the homepage for format and RSVP details; follow its Meetup link only to read public dated listings. |
| [amsterdamdancecentre.nl](amsterdamdancecentre-nl.md) | needs_simplification | Yes | partial | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. FAQ yields single-class access/price and directs to online schedule, but schedule widget rendered blank in ordinary browser. The FAQ supports single-class price and level; wait for the public schedule widget to render before adding class dates. |
| [amsterdamhouseofartsandcrafts.com](amsterdamhouseofartsandcrafts-com.md) | needs_simplification | Yes | partial | web-extraction | Organizer page gives a price and recurring weekly hours, while dated availability requires a separate calendar view; the guide had no working route between them. Use the tested I amsterdam listing’s month controls and copy an actual dated slot; the organizer page itself states €59 and recurring hours but does not provide dates. |
| [amsterdammuseum.nl](amsterdammuseum-nl.md) | easy | No | usable | web-extraction | The event page exposes the Saturday date list, time, venue and price in plain text; the page's workshop-to-date mapping is incomplete for some dates. Copy only displayed dates and general time; leave date-specific technique unknown where the page does not map it. |
| [amsterdice.nl](amsterdice-nl.md) | needs_simplification | Yes | partial | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Newcomer page is clear about solo access and €10 entry, but the saved page itself did not show an individual date; follow agenda link. Follow the page’s agenda link for a dated Sunday entry; this newcomer page alone provides hours, solo access and entry terms. |
| [andreas.amsterdam](andreas-amsterdam.md) | easy | No | partial | web-extraction | Direct event detail is readable; exact start is present but price and end are not. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [api.uva.nl](api-uva-nl.md) | easy | No | usable | web-extraction | The event and registration pages are separate but linked and plainly state the schedule, weather condition, language, walk-in rule and registration opening window. For future occurrences, check the event page and its linked registration page; do not infer dates from a recurring pattern. |
| [atelierkleie.wordpress.com](atelierkleie-wordpress-com.md) | needs_simplification | Yes | usable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Dated schedule, beginner suitability and single-session price are all on one page. The page lists November dates and single-session pricing; verify availability separately before treating a session as open. |
| [atelieropen.nl](atelieropen-nl.md) | easy | No | partial | web-extraction | The saved workshops page directly exposed workshop format and cost, but no actual future date in the readable section. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [balfolkamsterdam.nl](balfolkamsterdam-nl.md) | easy | No | usable | web-extraction | The saved November social page opens directly to event date/time, ticket prices, beginner welcome, and access details. The agenda URL separately returned a cache miss. Use the saved November event detail directly if the agenda index does not load. |
| [baristacompany.com](baristacompany-com.md) | needs_simplification | Yes | unavailable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Homepage is hospitality service/event catering, not a public Amsterdam Academy course calendar; no single-seat class listed. No public Academy class calendar is present on the homepage; keep this saved lead unavailable unless an actual open class listing appears. |
| [beestboulders.com](beestboulders-com.md) | not_applicable | No | excluded | not-tested-excluded | Not included in the historical audit; guide-only review, no live activity research.  |
| [betaboulders.nl](betaboulders-nl.md) | not_applicable | No | excluded | not-tested-excluded | Not included in the historical audit; guide-only review.  |
| [bimhuis.nl](bimhuis-nl.md) | needs_simplification | Yes | usable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Dated event detail exposes title, date, hours and free entry directly. Use the dated event detail as the occurrence source; language and participant conditions remain unstated. |
| [boogieland.nl](boogieland-nl.md) | easy | No | partial | desktop-browser | Visible homepage is easy to read but only reports a September beginner-course promotion, with no date or price. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [boogieland.virtuagym.com](boogieland-virtuagym-com.md) | easy | No | unavailable | web-extraction | The public Virtuagym portal redirects to an explicit 'Portal not available / This system is no longer available' notice; this is source availability, not prompt difficulty. Treat the saved checkout/catalog route as retired; do not infer current prices or sessions from it. |
| [booking.leisureking.eu](booking-leisureking-eu.md) | needs_simplification | Yes | unavailable | desktop-browser | The original guide had no compact extraction/stop prompt. The ordinary-browser module redirected to a generic secure-connection screen with no products or dated entries; this was not enough to confirm a security denial. The browser module displayed only a generic secure-connection screen; leave the product calendar unavailable and do not infer entries. |
| [boomchicago.nl](boomchicago-nl.md) | easy | No | partial | desktop-browser | Initial extraction returned title only; visible browser retry showed a €30 two-hour Saturday taster with no experience required, but no exact taster date. Use the Academy class detail or booking listing to find a dated beginner-level taster; current page establishes €30 and two-hour taster but no exact occurrence. |
| [boulderhalluchthaven.nl](boulderhalluchthaven-nl.md) | not_applicable | No | excluded | not-tested-excluded | Not included in the historical audit; guide-only review.  |
| [buurtteamamsterdam.nl](buurtteamamsterdam-nl.md) | needs_simplification | Yes | usable | desktop-browser | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Series page shows actual date entries; no complex query required. Use the displayed series entries for dates and times; price and access terms were not established on the tested page. |
| [cameranu.nl](cameranu-nl.md) | easy | No | blocked | desktop-browser | Initial public-page attempt reached the saved event URL; visible browser retry stopped at Cloudflare security verification, so event fields were inaccessible. Stop at the Cloudflare security verification page; do not bypass it. Revisit only through a normal public page if access becomes available. |
| [circuslab.amsterdam](circuslab-amsterdam.md) | not_applicable | No | excluded | not-tested-excluded | Excluded by the active circus/juggling blacklist; guide-only review completed with no activity research.  |
| [classpass.com](classpass-com.md) | needs_simplification | Yes | unavailable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Page rendered a schedule but it was stale (Oct 6, already past); current future schedule was not established. The visible schedule was dated 6 October, already past; wait for future dates to load, and keep credit units separate from euros. |
| [clubcuisine.nl](clubcuisine-nl.md) | needs_simplification | Yes | usable | web-extraction | The calendar opened on September and October 2026 and ended with “Geen evenementen gevonden”; the guide did not state how to move to the target month. Open the November cards on the calendar and verify their own detail pages for per-person price and exact address before recommending a class. |
| [crea.nl](crea-nl.md) | needs_simplification | Yes | usable | web-extraction | The existing guide gave only the homepage and terms page, with no route to public event listings. The live route is homepage → Agenda → BASH calendar; the CREA guide now records this short path and a stop rule for multi-week courses. Use the BASH calendar route, then open the dated event detail where it is linked before relying on missing price or access information. |
| [dagjeweg.nl](dagjeweg-nl.md) | needs_simplification | Yes | unavailable | web-extraction | The saved guide incorrectly marked the whole DagjeWeg domain excluded because its one saved listing is climbing. The live homepage is a broad directory with Amsterdam/date filters; an allowed museum detail returned a Cloudflare challenge, so no dated eligible activity was captured. The homepage supports directory browsing, but the allowed H’ART listing hit a Cloudflare challenge; stop at that gate and leave event dates unavailable. |
| [debalie.nl](debalie.md) | easy | No | partial | web-extraction | The event detail directly supplied subject and speaker; event date is encoded in canonical slug and no price was exposed. The existing guide already gives a short working route. The public event page gave speakers/topic but did not display a date or ticket price; verify a date on De Balie’s dated programme listing before using it. |
| [deceuvel.nl](deceuvel-nl.md) | easy | No | usable | web-extraction | The saved event detail places title, date/time, free admission, and location in the first screen of page text. Use the saved event page; retain the stated end time and note that the route is still to be announced. |
| [delokatie.org](delokatie-org.md) | needs_simplification | Yes | unavailable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Homepage describes thrift/reuse and supported work; no public dated workshop or event found. The homepage contains reuse/work-experience information but no public dated workshop; keep it unavailable for event capture. |
| [derooijfotografie.nl](derooijfotografie-nl.md) | easy | No | usable | web-extraction | The direct course page exposes dated availability, and says the in-range November course is full. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [desteekamsterdam.com](desteekamsterdam-com.md) | easy | No | partial | web-extraction | The homepage's seasonal promotion is stale and is not a dated visible-mending circle. A current beginner upcycling course page gives its duration and languages but asks the visitor to choose a preferred date/time in the booking flow; no dated occurrence or public price appeared on the page. This is a schedule/price evidence gap, not a wording failure. Keep this as an undated discovery lead; do not treat the rolling course or stale promotion as a dated one-off event. |
| [dezwijger.nl](pakhuisdezwijger.md) | easy | No | partial | web-extraction | Month agenda renders current entries; first visible entries were October. Saved month-specific route/detail instructions remain useful for November and need no change. Open a November month route and detail only for a candidate with an exact date/time; the live base agenda showed October entries. |
| [eastboundgym.nl](eastboundgym-nl.md) | easy | No | partial | desktop-browser | Direct price page is readable in a public browser; single class is €16.50 but no dated schedule appears here. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [easylaughs.nl](easylaughs-nl.md) | easy | No | usable | web-extraction | Saved dated workshop detail pages directly expose event date/time, price, venue, language, and booking requirement. Use an individual saved workshop page and copy its explicitly listed ticket and language terms. |
| [equalyoga.com](equalyoga-com.md) | needs_simplification | Yes | unavailable | web-extraction | The original guide had only the saved booking URL and generic recheck rules. Live extraction showed Amsterdam studio choices but no dated class rows, price or single-visit terms; the public calendar was not clicked. Studio links are visible, but calendar selection and single-class terms remain untested; do not create dated entries from this page. |
| [eventbrite.com](eventbrite-com.md) | needs_simplification | Yes | partial | desktop-browser | The saved booking URL redirects to a public multiple-date pottery event; selecting a displayed date is necessary to capture a real occurrence. The public multiple-date page gives €79.83 and venue, but Check availability did not reveal dates; use only if the public date selector later exposes a dated slot, otherwise skip as unverified. |
| [eventbrite.nl](eventbrite-nl.md) | easy | No | usable | desktop-browser | The Eventbrite page did not render through normal web extraction (Cache miss), but the documented headless Chromium browser fallback rendered the ordinary public page and evidence fields. This is an extraction-route limitation, not a prompt problem or access denial. If web extraction returns Cache miss, use the ordinary visible browser route and stop before registration or checkout. |
| [fablab.waag.org](fablab-waag-org.md) | needs_simplification | Yes | unavailable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Fab Academy page states 2026 registration is closed; course is not a single drop-in event. Registration for Fab Academy 2026 is closed and the program is a course; do not use it as a single-visit listing. |
| [femmegym.nl](femmegym-nl.md) | easy | No | partial | desktop-browser | Club page gives venue identity and class types; no actual class date or single-visit access price appears in this page. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [framerframed.nl](framerframed.md) | easy | Yes | partial | desktop-browser | Agenda is readable and gives a dated workshop, but the observed workshop is explicitly for Black women with ADHD and/or autism; audience fit is restricted and event price was not stated. Exhibition date spans are not occurrence dates. Use the agenda only when its stated audience matches; check the workshop detail for price and registration terms. Do not turn exhibition date spans into event occurrences. |
| [freedamtours.com](freedamtours-com.md) | easy | No | partial | desktop-browser | The official homepage and FAQ provide schedule, language, access, group limits and tip-based terms, but only as recurring departures. The linked FareHarbor web extract returned an unrendered template; the ordinary browser showed the tour overview but no exact dated session, so no date was inferred. Keep the tour as a recurring offer until an exact date appears on a usable public calendar; preserve tip-based price wording. |
| [freewalkingtoursamsterdam.com](freewalkingtoursamsterdam-com.md) | needs_simplification | Yes | partial | web-extraction | Original guide lacked a short field-copy prompt. Live tour detail states the €2 booking fee, voluntary separate tip, English language, 2-hour duration and Dam Square start; the public date calendar remained on “Loading dates…”, so no departure was verified. Keep date/time unknown while the departures calendar says “Loading dates”; record the €2 fee, voluntary tip, English and Dam Square only. |
| [gildeamsterdam.nl](gildeamsterdam-nl.md) | easy | No | unavailable | desktop-browser | Initial extraction returned only a title; visible browser retry showed 2–2.5-hour walks only for the people booking together, with no open-group dated session. Skip for solo attendance unless Gilde publishes an open-group dated walk; the observed walks are private bookings for the people who book together. |
| [heartandsoulstudio.nl](heartandsoulstudio-nl.md) | needs_simplification | Yes | usable | desktop-browser | The date cards do not render in ordinary web extraction and show only 'Loading days…'. The saved guide led with a long historical Android/screenshot procedure. A live ordinary browser rendered Upcoming Sessions after scrolling, so the new quick start gives that short route and a rule not to infer the year from the yearless cards. Use the public service page in a regular browser to read Upcoming Sessions; do not add a year that the live cards omit. |
| [hetgroeneveld.amsterdam](hetgroeneveld-amsterdam.md) | needs_simplification | Yes | usable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Dated page gives event, time, price and address directly; prompt only needed route/copy fields. The dated page has a complete craft-session packet; do not extend it from weekly recurrence alone. |
| [hetgymlokaal.nl](hetgymlokaal-nl.md) | easy | No | partial | desktop-browser | Initial extraction returned only the title and browser showed a cookie overlay; after choosing visible “Decline all”, the public page showed a €17.50 single-class/fitness credit but no dated class session. Use the pass page for the €17.50 single class/fitness-entry price; a separate public class roster is still needed for an exact date and time. |
| [hipsy.eu](hipsy-eu.md) | easy | No | partial | web-extraction | The saved Dance Playground page exposes its date, time, venue and languages without sign-in, but the ticket button shows €13.30 while the description states €12.50 plus €1.15 Hipsy fees; preserve the discrepancy instead of selecting one total. Other hoopdance leads in the guide were not opened during this spot check, so their eligibility is unassessed. Keep both displayed price expressions; assess any other hoopdance lead on its own merits before considering it. |
| [hipsy.nl](hipsy.md) | needs_simplification | Yes | usable | desktop-browser | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Browser rendered event series and per-session ticket, though public extraction service could not open Hipsy. Use the individual €26.80 session price and stated date/time; keep the €95.80 series price separate. |
| [huisvandebuurtdeboomsspijker.nl](boomsspijker.md) | easy | No | blocked | web-extraction | The official October calendar loaded and exposes filters/date controls, but requesting November returned an explicit insufficient-rights page. Alternate public WijkConnect category and detail URLs returned extraction cache misses, not successful evidence. Treat the target-month route as blocked; do not infer or bypass it. Retry the official public November calendar on a later audit or use an independently accessible public category listing; keep event facts unknown meanwhile. |
| [iamsterdam.com](iamsterdam-com.md) | needs_simplification | Yes | usable | desktop-browser | Month controls and “Meer data” are necessary to expose future dated slots; the guide previously listed URLs without an observed navigation recipe. Use month controls and “Meer data” on the official listing, then copy the actual dated slot and stated price/access details. |
| [ivn.nl](ivn-nl.md) | easy | No | usable | web-extraction | The saved organizer event page clearly displays the exact date/time, free admission, mandatory registration, location, and adult audience; spoken language is not stated. Use the exact organizer event page; keep spoken language unstated despite Dutch page copy. |
| [jaapeden.nl](jaapeden-nl.md) | needs_simplification | Yes | partial | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Pricing page shows single public skate ticket, but not individually dated public skating sessions. The public single-entry rate is €10.60 before skate rental; use public opening times for dated sessions and keep rates separate. |
| [jiadamahjong.com](jiadamahjong-com.md) | easy | No | unavailable | web-extraction | The direct product page is a past September event; no matching future date is given by this saved URL. Use the organizer’s current events listing to find a new dated Mahjong session inside the requested horizon; the saved 19 September event is past and should not be reused. |
| [kantlijn.org](kantlijn-org.md) | easy | No | partial | web-extraction | The homepage is easy to read and confirms free weekly writing workshops and walk-in access, but it only gives recurring weekdays, not individually dated occurrences. Do not expand those recurrences into dates. Use the homepage for format and newcomer access only; find a separate dated listing before proposing an occurrence. |
| [keramiekatelier.nl](keramiekatelier-nl.md) | needs_simplification | Yes | unavailable | desktop-browser | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Old domain redirects to current studio course page; homepage advertises multi-class courses, no one-off public dated session. The domain redirects to a ten-class course page; no one-off dated session is published there. |
| [kookfabriek.nl](kookfabriek-nl.md) | needs_simplification | Yes | usable | web-extraction | Homepage describes group bookings for 8–250 people, but separately links to public masterclasses that welcome solo visitors; the guide did not distinguish these routes. Use the Masterclasses calendar and copy the actual Amsterdam date/time; the observed one-off classes list €99 and welcome solo attendees. |
| [luma.com](luma-com.md) | easy | No | partial | web-extraction | The official Luma event detail directly exposes date/time, venue, event structure, solo welcome, and ticket categories, but the listed ticket prices were not rendered in the public page output. Use the saved event page for date/time and eligibility; leave ticket amount unstated when no amount is displayed. |
| [mangoinapot.com](mangoinapot-com.md) | needs_simplification | Yes | usable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Dated event calendar exposes exact dates/times; details require one event link for price. The calendar provides individual dates/times; open a detail only when a specific session price or access term is needed. |
| [maqam-amsterdam.nl](maqam-amsterdam-nl.md) | needs_simplification | Yes | usable | desktop-browser | The saved Warda detail is for November 2025; the guide needs an explicit stale-page check and route to the current program. Follow Programma to the current MAJAM entry and copy its displayed event details; confirm performer lineup on the page before publishing it. |
| [meetup.com](meetup-com.md) | easy | No | usable | desktop-browser | Web extraction could not access two public Meetup pages (one returned inaccessible and another Cache miss), but ordinary browser loading of the saved Oct 24 event succeeded with a public event detail and no sign-in. This is an extraction limitation, not a prompt failure. When web extraction cannot open a Meetup event, use an ordinary public browser page and stop before Join/RSVP. |
| [mezrab.nl](mezrab-nl.md) | needs_simplification | Yes | partial | web-extraction | The original guide had no short copy prompt; the live month list exposes dates/times, but this audit did not open event details for price/access/language. The November list exposes dated titles and starts; event details for price/access/language were not opened. |
| [mkateliers.nl](mkateliers-nl.md) | easy | No | unavailable | desktop-browser | Initial extraction showed only the catalogue header; visible browser retry showed recurring Friday 09:30–12:30 ceramics in eight-lesson blocks, requiring prior clay experience, and no one-off beginner session. Skip this catalogue for a solo beginner event: it lists multi-lesson ceramics courses requiring prior clay experience, not dated one-off sessions. |
| [monk.nl](monk-nl.md) | not_applicable | No | excluded | not-tested-excluded | Not included in the historical audit; guide-only review completed without opening activity pages.  |
| [movementsyoga.com](movementsyoga-com.md) | needs_simplification | Yes | partial | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Price page has no dated session; schedule requires separate public route/branch selection. Record €25 as the one-class price; a dated occurrence was not shown on the tested pricing page. |
| [museumnacht.amsterdam](museumnacht-amsterdam.md) | easy | No | usable | desktop-browser | The programme page is directly readable in the browser; program details are clear but price is not shown. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [muziekgebouw.nl](muziekgebouw-nl.md) | easy | No | usable | web-extraction | The organizer listing places title, exact occurrence time, adult audience and ticket price together in the main event content. Use the saved event detail and preserve the displayed last-tickets status. |
| [oba.nl](oba.md) | easy | No | partial | desktop-browser | Existing guide already documents OBA search filters and event-detail route. Browser succeeded after direct extraction failed. The detail lists future dates, times, English instruction and required email registration; price was not stated. |
| [olvminor.nl](olvminor-nl.md) | easy | No | unavailable | desktop-browser | The saved homepage explains beginner suitability but its current listed dates start in January 2027, beyond the audit horizon. Recheck only when the organizer posts dates in the target horizon; the currently visible January/February 2027 listings are outside this audit range. |
| [ottavi.nl](ottavi-nl.md) | easy | No | usable | web-extraction | The public cooking-studio agenda is a long but plainly structured list: each dated event shows its exact start time, title, per-person price and live availability before the description. Read the date/title/time/price/availability fields above each description and do not treat gift cards as event prices. |
| [oudekerk.nl](oudekerk-nl.md) | needs_simplification | Yes | usable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Homepage displays dated public programs; open one individual entry for details. Use a dated program detail for event admission; daily museum opening hours are not event occurrences. |
| [overdebrug-oostenburg.nl](overdebrug-oostenburg-nl.md) | easy | No | usable | web-extraction | Direct event detail exposes the date, start/end, price, and beginner/solo suitability. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [parkrun.co.nl](parkrun-co-nl.md) | easy | No | blocked | desktop-browser | Saved event page was directly attempted, but the public site returned HTTP 403 in the ordinary browser; no event fields rendered. This is an access denial, not a guide wording problem. Retry the same public page on a later audit; do not infer a weekly occurrence from the park run name. |
| [peterpan.nl](peterpan-nl.md) | needs_simplification | Yes | partial | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Page confirms open individual workshops and English-speaking chefs, but no dates/price in current page extract. The page confirms open individual workshops and English-speaking chefs; no dated workshop or price was shown. |
| [pretix.eu](pretix-eu.md) | easy | No | usable | desktop-browser | The public ticket page loaded in browser fallback and clearly marks every free slot fully booked with waiting lists. The page supplies the exact free slots and fully-booked/waitlist status; no further extraction route is needed unless checking for later released capacity. |
| [repaircafe.amsterdam](repaircafe-amsterdam.md) | needs_simplification | Yes | usable | web-extraction | The saved venue card's Next time field was stale and contradicted the current dated Agenda rows. The guide lacked route and source-priority instructions for agenda date/time, venue scope/address, and FAQ costs. Use the current Agenda row as the occurrence source, and keep any conflicting venue-card date out of extracted event data. |
| [sambaschoolfidelinas.nl](sambaschoolfidelinas-nl.md) | needs_simplification | Yes | usable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Beginner page puts dated entries and single-visit price together. The beginner page gives upcoming dates and €15 per class; solo attendance and beginner level are explicit. |
| [shop.brandmeesters.nl](shop-brandmeesters-nl.md) | easy | No | usable | web-extraction | The direct booking detail page exposes exact date/time, price, language, and stock without checkout. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [simoneheijloo.nl](simoneheijloo-nl.md) | needs_simplification | Yes | usable | web-extraction | The same page contains a current October–November Dates & Fee schedule and an older June block with conflicting prices. The guide did not tell Luna which dated block to trust. Keep only dates explicitly enumerated in the current block; retain the conflicting old fee as a warning, not an alternative current price. |
| [singsing.nl](singsing-nl.md) | needs_simplification | Yes | partial | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Page confirms walk-in open karaoke and recurring hours; no dated special event or public entry price. The page confirms open walk-in karaoke and hours; no dated special night or public admission price is listed. |
| [smaakcultuur.nl](smaakcultuur-nl.md) | easy | No | usable | web-extraction | The direct workshop page shows the November occurrence and exact price/time; no further navigation is needed. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [sobamsterdam.nl](sobamsterdam-nl.md) | easy | No | partial | web-extraction | The public page gives recurring Friday hours and participation terms, but no individually dated target-window occurrence or price. Do not generate dates from the weekly schedule. Wait for an individually dated public listing before treating it as a target-window occurrence. |
| [soozamsterdam.nl](soozamsterdam-nl.md) | needs_simplification | Yes | partial | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Volunteer page allows one-off helping but provides no dates; it is not a public meal listing. The site permits one-off volunteering but gives no shift dates; treat the kitchen role as volunteering, not meal access. |
| [sportcity.nl](sportcity-nl.md) | needs_simplification | Yes | partial | web-extraction | The saved Zumba explainer has no exact session; the page links to a separate club/date roster and says group classes require membership. The public Waterlooplein roster loaded only its current Week 42 (12–18 Oct); no target-horizon session was exposed. Stop unless a public future-week control appears, and preserve membership requirement. |
| [sportclubmatch.nl](sportclubmatch-nl.md) | needs_simplification | Yes | partial | web-extraction | The saved URL is a Pilates page although the source title says Zumba Gold. It shows recurring hours and several price types, so the guide needed to prevent activity substitution and date inference. Do not treat recurring class times as dated events or attribute the Pilates prices to Zumba Gold. |
| [spui25.nl](spui25.md) | easy | No | partial | web-extraction | Existing guide gives a direct month URL, clear extraction steps and stop rule. Live agenda showed several dated entries, but visible starts at 17:00 do not meet the requested weekday time window; event prices were absent. The November agenda has dates and starts, but observed 17:00 weekday events fall outside the requested time window; price was not stated. |
| [stadswandelkantoor.nl](stadswandelkantoor-nl.md) | easy | No | partial | web-extraction | Detailed saved guide already notes open-tour signup, €17.50 and no public individual dates; current page confirms this. The catalogue gives tour prices but no dated departure; keep the offer undated until a specific start appears. |
| [station-west.amsterdam](station-west-amsterdam.md) | easy | No | partial | web-extraction | Official calendar lists dated sessions and prices directly; the first current entries were 16–19 Oct, so target dates require scanning farther down. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [stcamsterdam.nl](stcamsterdam-nl.md) | needs_simplification | Yes | usable | web-extraction | Guide listed many individual shifts but had no route to the live dated calendar. Following the site’s Event calendar link exposed dates/statuses, then the individual page supplied eligibility and language. Use the calendar as occurrence source and the individual shift page for eligibility/language; do not enter signup. |
| [stretchandfold.nl](stretchandfold-nl.md) | needs_simplification | Yes | usable | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Calendar exposes dated events; detailed page needed for single-visit cost/access. Use calendar rows for title/date/time; event price and beginner access were not opened on this audit. |
| [studio-koekoek.com](studio-koekoek-com.md) | easy | Yes | usable | web-extraction | Catalog opened directly and the saved guide already has working sort/list steps; extracted response did not include card details in this attempt. Catalog browser view returned 403; use the public product detail route when the catalog or saved card supplies it, then verify exact date, stock and beginner fit without adding to cart. |
| [studio191.nl](studio191-nl.md) | needs_simplification | Yes | partial | desktop-browser | Text extraction omitted the schedule rows; an ordinary visible browser rendered the weekly timetable. The visible week was Oct 18–24 and the captured event detail was on Oct 18, so this attempt did not verify a future target-window occurrence. Guide now says to wait for the browser schedule and stop when requested dates are not shown. For future weeks, use only a visibly confirmed date before claiming a target-window class; do not infer from recurrence. |
| [theartcafe.nl](theartcafe-nl.md) | needs_simplification | Yes | usable | web-extraction | Original guide had no compact field-copy prompt. Live calendar displays an individually dated November event and its time/price; detail route is not required for this observed packet. The live calendar provides 13 Nov, 19:30–22:00 and €40; language was not stated. |
| [theatersport.nl](theatersport-nl.md) | easy | No | usable | desktop-browser | Initial extraction returned title only; visible browser retry showed 24 Nov 20:45–22:30, €10 + €0.25, Polanentheater, all experience levels. Use the public event detail; confirm availability there if needed. It explicitly invites people to try all experience levels. |
| [theclayroomamsterdam.com](theclayroomamsterdam-com.md) | easy | No | partial | web-extraction | Direct workshop page lists Sunday 22 November 13:30–16:00, €75, available spots, beginner-friendly 2.5-hour workshop, English instruction, and materials/firing included; the page does not display the year beside the date, so the specific 2026 occurrence is unverified. Confirm the year from a current dated page before treating the November date as a specific 2026 occurrence. |
| [toastmasters.org](toastmasters-org.md) | needs_simplification | Yes | partial | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Club profile gives recurring meeting schedule and free guest terms, but no instance date; address is listed. The profile supports free guest visits and recurring Friday time; an individually dated meeting was not shown. |
| [tolhuistuin.nl](tolhuistuin.md) | easy | No | usable | desktop-browser | Initial extraction returned title only; visible browser retry showed ONE FINE MESS on 13 Nov, doors 18:30, 19:00–23:59, free, English, IJzaal. Use the event detail for this date and verify availability on the public event page when needed; no account or purchase is needed to extract these fields. |
| [tomgoldhand.com](tomgoldhand-com.md) | easy | No | usable | web-extraction | The saved course page clearly enumerates dates and fees, but it is a 14-class course with limited single-class spots and signup/downpayment requirements; do not present it as an unrestricted drop-in. Keep course commitment and limited single-class availability explicit; do not infer availability from the listed dates. |
| [upclubstudios.com](upclubstudios-com.md) | needs_simplification | Yes | partial | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Home page confirms formats and intro deal but no dated class schedule or standalone single class price. The homepage supports workout formats and a two-workout €19 intro offer; current dated classes and single-class price remain unknown. |
| [volkssterrenwachtamsterdam.nl](volkssterrenwachtamsterdam-nl.md) | easy | No | usable | desktop-browser | Browser fallback reads a current exact event page; advance registration is stated, while price/language are not. Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose. |
| [volksuniversiteitamsterdam.nl](volksuniversiteitamsterdam-nl.md) | needs_simplification | Yes | usable | web-extraction | The saved link opened a broad catalogue without navigation guidance. Opening a concrete course detail exposed status, fee, duration, location, and exact course dates; the new quick start directs Luna to an individual detail page and flags multi-session commitment. Use the homepage-to-course-card route when a copied course URL is inaccessible; preserve the multi-session commitment explicitly. |
| [vondelgym.nl](vondelgym-nl.md) | needs_simplification | Yes | partial | web-extraction | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Zuid page gives €19.50 day pass and explicit schedule link, but no dated class; day pass inclusion must be verified. The Zuid page gives a €19.50 day pass; the class schedule was not inspected, so dated class admission remains unknown. |
| [vrijeacademie.nl](vrijeacademie-nl.md) | easy | No | usable | desktop-browser | Initial extraction returned title only; visible retry after rejecting optional cookies showed 15 Nov 14:00–17:00, €89, materials included and nearly full/waitlist; booking asks for an account, which was not entered. Use the cyanotype workshop page for the dated price and waitlist status; do not continue into account creation or booking. |
| [waag.org](waag-org.md) | easy | No | unavailable | web-extraction | The saved FabLab project page has a closed project duration ending 1 January 2025; the Open Wetlab page describes an ongoing research programme but no public drop-in calendar or target-window public session. This is source availability, not a prompt issue. Wait for an individually dated public session or posted open hours; do not treat the legacy project page as current access. |
| [wijkconnect.com](wijkconnect-com.md) | needs_simplification | Yes | usable | desktop-browser | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Ordinary browser succeeded after web extraction error; detail provides recurrence/time/price but calendar confirms exact date. Pair the November calendar date with the detail’s 20:00–22:00 time, €15.50 price and guest-list email. |
| [wildernisamsterdam.nl](wildernisamsterdam-nl.md) | easy | No | usable | desktop-browser | Initial extraction returned title only; visible retry after declining optional cookies showed an English €78 Terrarium on 17 Nov, doors 18:45/start 19:00, plus a Kokedama listing with no stated start time. Use the Terrarium detail for exact start time; its listing is English at €78. Kokedama has a walk-in window but no explicit start time, so do not infer one. |
| [yagoy.nl](yagoy-nl.md) | needs_simplification | Yes | partial | desktop-browser | Homepage extraction lists pass prices but hides class rows behind the schedule widget. A visible browser rendered the de Pijp weekly timetable; the displayed week was Oct 18–24 and only the Oct 18 sessions were inspected, so no later target-window occurrence is asserted. Only claim classes whose exact date is visible and whose displayed status is not closed/full. |
| [zumba.com](zumba-com.md) | needs_simplification | Yes | blocked | desktop-browser | The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Browser returned HTTP 403 Cloudflare “Just a moment” security verification; stop at challenge. Web extraction cache miss is not the security block. The detail returned Cloudflare HTTP 403; stop at the challenge and keep the class unverified. |

## Observed evidence and repeat checks

### activiteiten.amsterdam.nl

[Guide](activiteiten-amsterdam-nl.md) · usable · difficulty: low · retested: no

Direct saved detail pages expose the title, occurrence date/time, description, price, audience and location in one short page.

1. [web-extraction](https://activiteiten.amsterdam.nl/activiteiten/2026/11/maak-festival-duurzame-thuismarkt/): Opened municipal event detail; title, date/time, free admission, activity description, audience and location were visible. Evidence: title: MAAK HET ZELF-festival & Duurzame Thuismarkt; date: 2026-11-08; time: 12:00–16:00; price: Free; access: All ages; event description and location visible.

Next step: Use the saved direct event URL and copy only explicitly displayed fields.

### adc.trainin.app

[Guide](adc-trainin-app.md) · unavailable · difficulty: high · retested: no

The original guide had no short route/copy prompt. The public schedule widget loaded with title ADC but an empty body in the ordinary browser; no date or class fields were readable. This is a rendering limitation, not a security denial.

1. [web-extraction](https://adc.trainin.app/widget/schedule): URL inaccessible via web extraction; ordinary browser then loaded an empty widget body. Evidence: No event/access fields extracted. Error: Web extraction tool could not access this widget URL.
2. [desktop-browser](https://adc.trainin.app/widget/schedule): HTTP 200, title ADC, body empty; no fields extractable Evidence: No event/access fields extracted.

Next step: Use the FAQ only for displayed single-class/level facts; leave class dates unavailable until the public schedule widget renders.

### agalab.nl

[Guide](agalab-nl.md) · usable · difficulty: low · retested: no

Direct workshop page exposed a dated 21 Nov session and price; route is simple.

1. [web-extraction](https://agalab.nl/en/painting-plants-2/): The organizer page directly displayed the Nov 21 workshop, 10:00–17:00, €200, max six and email registration. Evidence: title: Screenprinting with Natural Inks; date: 21 November 2026; time: 10:00–17:00; price: €200; access: Registration by email; max 6.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### amsterdam-dance-event.nl

[Guide](amsterdam-dance-event-nl.md) · usable · difficulty: low · retested: no

The saved event page puts title, exact date/time, venue, target audience and cash price together in the main content.

1. [web-extraction](https://www.amsterdam-dance-event.nl/en/program/2026/pink-dance-sunday-afternoon-ballroom-latin/2830540/): Opened ADE detail page; displayed the event facts and admission terms. Evidence: title: Pink Dance – Ballroom, Latin & Freestyle Dance for LGBTQ+ 50+; date: 2026-10-25; time: 14:00–17:00; price: €5 cash; drinks extra; access: Beginners and experienced dancers welcome; LGBTQ+ 50+ community and friends.

Next step: Use the saved event page and preserve the stated audience and cash-only price.

### amsterdam.knnv.nl

[Guide](amsterdam-knnv-nl.md) · usable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Direct event page is understandable once the visible “Datum & tijd” section is identified.

1. [web-extraction](https://amsterdam.knnv.nl/agenda/fotowandeling-diemerbos/): Live page fetch failed in the web extraction tool. Evidence: No event/access fields extracted. Error: Failed to fetch: web extraction cache miss; retried in ordinary browser.
2. [desktop-browser](https://amsterdam.knnv.nl/agenda/fotowandeling-diemerbos/): Rendered dated event; 20 Nov 2026, 10:00; 2–3h; House of the Bird; max 10; phone camera sufficient; no fee stated Evidence: title: Fotowandeling Diemerbos; date: 20 November 2026; time: 10:00; duration 2–3 hours; access: Registration by email; max 10 participants.

Next step: The detail page exposes one complete dated walk packet; use it and keep fee unknown because none is stated.

### amsterdam.nl

[Guide](amsterdam-nl.md) · partial · difficulty: medium · retested: yes

Price page is direct, but exact swim/class times are on a separate Rooster link; the guide did not explain this split.

1. [web-extraction](https://www.amsterdam.nl/noorderparkbad/prijzen-noorderparkbad/): The live tariff page exposed swim and Aquasport single prices, required swim pass scope, and linked the current Rooster; no dated session was visible on this price page. Evidence: title: Noorderparkbad prices; price: Single swim €6.40; Aquasport 45-minute class €9.60; swim pass €5.80 for lessons and multi-visit cards.
2. [web-extraction](https://www.amsterdam.nl/noorderparkbad/rooster/): Followed the official Rooster link from the price page; live timetable page opened as “Zwembadrooster” but no session rows were exposed. A later ordinary browser view showed the city site automated-traffic block; no bypass attempted. Evidence: title: Zwembadrooster; price: Source price page: single swim €6.40; Aquasport 45 min €9.60; access: Current session rows not exposed; browser retry blocked by city-site automated traffic protection.

Next step: The tariff is verified, but the Rooster page exposed no session rows and the city-site browser presented an automated-traffic block; use the official live pool timetable later or choose a venue with a readable dated roster.

### amsterdambookclub.com

[Guide](amsterdambookclub-com.md) · usable · difficulty: low · retested: no

Homepage directly displays its English-language format, solo attendance welcome, next discussion date and RSVP path.

1. [web-extraction](https://www.amsterdambookclub.com/): Opened organizer homepage; current book, next discussion date, English language and Meetup RSVP link were visible. Evidence: title: Amsterdam Book Club discussion: The Devotion of Suspect X; date: 2026-10-25; language: English; access: Solo attendance welcome; RSVP required to reserve a place.

Next step: Use the homepage for format and RSVP details; follow its Meetup link only to read public dated listings.

### amsterdamdancecentre.nl

[Guide](amsterdamdancecentre-nl.md) · partial · difficulty: medium · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. FAQ yields single-class access/price and directs to online schedule, but schedule widget rendered blank in ordinary browser.

1. [web-extraction](https://amsterdamdancecentre.nl/faq-adult-division/): FAQ shows single class €22.50, PIN only, online booking optional; Basic is absolute beginner; no date on FAQ Evidence: title: Amsterdam Dance Centre adult FAQ; price: €22.50 per single class; access: Walk-in signup allowed; PIN only; advance booking optional.
2. [web-extraction](https://amsterdamdancecentre.nl/adults/): Adults page links Schedule and embeds ADC widget; no dated entries in extraction Evidence: title: Adult schedule page.

Next step: The FAQ supports single-class price and level; wait for the public schedule widget to render before adding class dates.

### amsterdamhouseofartsandcrafts.com

[Guide](amsterdamhouseofartsandcrafts-com.md) · partial · difficulty: medium · retested: yes

Organizer page gives a price and recurring weekly hours, while dated availability requires a separate calendar view; the guide had no working route between them.

1. [web-extraction](https://www.amsterdamhouseofartsandcrafts.com/nl/workshops/open-atelier): The organizer page displayed €59, two hours, beginner suitability, materials, and recurring hours but not dated booking slots; the linked city listing exposes month controls and dated cards. Evidence: title: Open Atelier; time: Wed/Fri 19:30–21:30; Sun 13:00–15:00 (stated recurring hours); price: €59; access: Beginners welcome; materials included.
2. [desktop-browser](https://www.iamsterdam.com/uit/agenda/attracties-en-bezienswaardigheden/tours/open-atelier-creatief-maken-in-amsterdam): Rejected optional cookies with the visible Deny choice, then selected November; dated table showed Sun 1 Nov 13:00–15:00, Wed 4 Nov 19:30–21:30, Fri 6 Nov 19:30–21:30 and a visible “Laat meer zien” control. Evidence: title: Open Atelier: Creatief maken in Amsterdam; date: 1, 4 and 6 November 2026; time: Sun 13:00–15:00; Wed/Fri 19:30–21:30; price: €59; access: No experience required; materials included; venue Oude Schans 21.

Next step: Use the tested I amsterdam listing’s month controls and copy an actual dated slot; the organizer page itself states €59 and recurring hours but does not provide dates.

### amsterdammuseum.nl

[Guide](amsterdammuseum-nl.md) · usable · difficulty: low · retested: no

The event page exposes the Saturday date list, time, venue and price in plain text; the page's workshop-to-date mapping is incomplete for some dates.

1. [web-extraction](https://www.amsterdammuseum.nl/publieksprogramma/the-art-cafe-workshops/275890): Opened museum programme page; dates, general time and price visible. The two technique lists do not map every displayed November date to a technique. Evidence: title: The Art Café Workshops; date: 2026-11-14, 2026-11-21, 2026-11-28; time: 14:00–16:00; price: €12.50; access: Everyone welcome, including first-time participants; venue Amsterdam in Motion, Pazzanistraat 19.

Next step: Copy only displayed dates and general time; leave date-specific technique unknown where the page does not map it.

### amsterdice.nl

[Guide](amsterdice-nl.md) · partial · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Newcomer page is clear about solo access and €10 entry, but the saved page itself did not show an individual date; follow agenda link.

1. [web-extraction](https://www.amsterdice.nl/evenementen/): Event info says Sunday 13:00–22:00, drop-in, solo welcome, €10 for two coins; exact dates via agenda link Evidence: title: Amsterdice events; time: Sunday 13:00–22:00; price: €10 for two coins; access: Solo visitors welcome; drop in any time.

Next step: Follow the page’s agenda link for a dated Sunday entry; this newcomer page alone provides hours, solo access and entry terms.

### andreas.amsterdam

[Guide](andreas-amsterdam.md) · partial · difficulty: low · retested: no

Direct event detail is readable; exact start is present but price and end are not.

1. [web-extraction](https://andreas.amsterdam/e/evt-ceuvel-adev-in-amsterdam-noord-dans-mee): The live event page displayed the title, Saturday 24 Oct 2026 at 13:00, De Ceuvel address, and a ticket link; end time and price were absent. Evidence: title: ADEV in Amsterdam-Noord: dans mee!; date: 24 October 2026; time: 13:00; access: Ticket link points to De Ceuvel; price not shown.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### api.uva.nl

[Guide](api-uva-nl.md) · usable · difficulty: low · retested: no

The event and registration pages are separate but linked and plainly state the schedule, weather condition, language, walk-in rule and registration opening window.

1. [web-extraction](https://api.uva.nl/nl/content/evenementen/2026/10/nacht-van-de-nacht.html): Opened event page; event facts and optional registration/walk-in access were visible. Evidence: title: Nacht van de Nacht; date: 2026-10-24; time: 20:00–23:59; hourly tours start 20:00–00:00; language: Dutch- and English-speaking astronomers are present; access: Registration optional but guarantees a place; walk-ins may enter if space remains; clear-sky dependent.
2. [web-extraction](https://api.uva.nl/nl/publieksactiviteiten/sterrenkijkavonden/aanmelden/aanmelden.html): Opened registration guidance; the current Oct 24 registration link was displayed and page states registration links appear one week before each event. Evidence: title: UvA public stargazing registration; date: Current listing: 2026-10-24; access: Public Pretix registration link; no email registration.

Next step: For future occurrences, check the event page and its linked registration page; do not infer dates from a recurring pattern.

### atelierkleie.wordpress.com

[Guide](atelierkleie-wordpress-com.md) · usable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Dated schedule, beginner suitability and single-session price are all on one page.

1. [web-extraction](https://atelierkleie.wordpress.com/workshops/): Nov 6, 18:00–20:00; beginner suitable; single two-hour session €78 Evidence: title: Introduction to Pottery Techniques; date: 6 November 2026; time: 18:00–20:00; price: €78 for one 2-hour session; access: Beginner suitable; single session allowed.

Next step: The page lists November dates and single-session pricing; verify availability separately before treating a session as open.

### atelieropen.nl

[Guide](atelieropen-nl.md) · partial · difficulty: low · retested: no

The saved workshops page directly exposed workshop format and cost, but no actual future date in the readable section.

1. [web-extraction](https://www.atelieropen.nl/workshops/): The workshops page displayed a four-hour lino workshop for €75 with two to five participants and no experience requirement; no dated slot was exposed in the page text read. Evidence: title: Atelier Open Workshops; price: €75; access: Lino workshop, 4 hours, 2–5 participants; no drawing experience required.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### balfolkamsterdam.nl

[Guide](balfolkamsterdam-nl.md) · usable · difficulty: low · retested: no

The saved November social page opens directly to event date/time, ticket prices, beginner welcome, and access details. The agenda URL separately returned a cache miss.

1. [web-extraction](https://balfolkamsterdam.nl/balfolk-social-november): Opened the saved November event detail; date/time, price, beginner workshop and solo/no-partner access statement visible. Evidence: title: Balfolk Social in de Mezrab met Zephyr Combo en Duo Baftig; date: 2026-11-15; time: 16:15–22:00; price: €18.50 presale / €20 door; access: Open community; no prior dance experience or fixed partner needed; beginner workshop included.
2. [web-extraction](https://www.balfolkamsterdam.nl/agenda): Live fetch returned Cache miss; no page content was extracted. Evidence: No event/access fields extracted. Error: Cache miss

Next step: Use the saved November event detail directly if the agenda index does not load.

### baristacompany.com

[Guide](baristacompany-com.md) · unavailable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Homepage is hospitality service/event catering, not a public Amsterdam Academy course calendar; no single-seat class listed.

1. [web-extraction](https://www.baristacompany.com/): Homepage offers barista service and machine rental; no public Academy schedule Evidence: title: Barista Company.

Next step: No public Academy class calendar is present on the homepage; keep this saved lead unavailable unless an actual open class listing appears.

### beestboulders.com

[Guide](beestboulders-com.md) · excluded · difficulty: low · retested: no

Not included in the historical audit; guide-only review, no live activity research.

Guide-only review; no live visit under the saved activity blacklist.

Next step:

### betaboulders.nl

[Guide](betaboulders-nl.md) · excluded · difficulty: low · retested: no

Not included in the historical audit; guide-only review.

Guide-only review; no live visit under the saved activity blacklist.

Next step:

### bimhuis.nl

[Guide](bimhuis-nl.md) · usable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Dated event detail exposes title, date, hours and free entry directly.

1. [web-extraction](https://www.bimhuis.nl/en/calendar/tuesday-jam-291): Tuesday Jam, 24 Nov 2026; cafe opens 21:30; event 22:00–00:30; free Evidence: title: Tuesday Jam; date: 24 November 2026; time: 22:00–00:30; price: Free.

Next step: Use the dated event detail as the occurrence source; language and participant conditions remain unstated.

### boogieland.nl

[Guide](boogieland-nl.md) · partial · difficulty: low · retested: no

Visible homepage is easy to read but only reports a September beginner-course promotion, with no date or price.

1. [web-extraction](https://boogieland.nl/): Live page opened but normal extraction returned title only; browser fallback used. Evidence: title: Boogieland.
2. [desktop-browser](https://boogieland.nl/): Browser fallback loaded the public homepage. It promoted a four-lesson beginner basics course but exposed no upcoming exact date, time, or price in the read portion. Evidence: title: Boogieland homepage; access: Four-lesson beginner boxing basics course promoted; booking system migration announced.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### boogieland.virtuagym.com

[Guide](boogieland-virtuagym-com.md) · unavailable · difficulty: low · retested: no

The public Virtuagym portal redirects to an explicit 'Portal not available / This system is no longer available' notice; this is source availability, not prompt difficulty.

1. [web-extraction](https://boogieland.virtuagym.com/webshop): Redirected to inactive portal notice; no catalog or lesson information available. Evidence: No event/access fields extracted. Error: Portal not available; system no longer available

Next step: Treat the saved checkout/catalog route as retired; do not infer current prices or sessions from it.

### booking.leisureking.eu

[Guide](booking-leisureking-eu.md) · unavailable · difficulty: high · retested: no

The original guide had no compact extraction/stop prompt. The ordinary-browser module redirected to a generic secure-connection screen with no products or dated entries; this was not enough to confirm a security denial.

1. [web-extraction](https://booking.leisureking.eu/bm/ab3fc530c18df81c3718b7129276caac?lang=NL): Live page fetch failed in the web extraction tool. Evidence: No event/access fields extracted. Error: Web extraction returned internal error; ordinary-browser attempt followed the widget redirect.
2. [desktop-browser](https://booking.leisureking.eu/bm/ab3fc530c18df81c3718b7129276caac?lang=NL): HTTP 200 redirected to /assortiment; body only “Beveiligde verbinding”; no schedule data Evidence: No event/access fields extracted.

Next step: The browser module displayed only a generic secure-connection screen; leave the product calendar unavailable and do not infer entries.

### boomchicago.nl

[Guide](boomchicago-nl.md) · partial · difficulty: medium · retested: no

Initial extraction returned title only; visible browser retry showed a €30 two-hour Saturday taster with no experience required, but no exact taster date.

1. [web-extraction](https://boomchicago.nl/academy/): Visible Academy page body showed an Improv Taster Class, Saturday duration 2h, €30, no experience required and fee credit. It also showed term 5 Oct–12 Dec; no exact taster date. Evidence: title: Boom Chicago Improv Taster Class; price: €30; access: Two-hour Saturday taster; no experience required; fee credited toward full course; exact date not exposed.
2. [desktop-browser](https://boomchicago.nl/academy/): Visible public Academy page read in browser; title-only extraction was incomplete. Evidence: title: Boom Chicago Academy; date: Term 5 October–12 December 2026; taster exact date not stated; price: Taster €30; access: Two-hour Saturday taster; no experience needed; credit toward course.

Next step: Use the Academy class detail or booking listing to find a dated beginner-level taster; current page establishes €30 and two-hour taster but no exact occurrence.

### boulderhalluchthaven.nl

[Guide](boulderhalluchthaven-nl.md) · excluded · difficulty: low · retested: no

Not included in the historical audit; guide-only review.

Guide-only review; no live visit under the saved activity blacklist.

Next step:

### buurtteamamsterdam.nl

[Guide](buurtteamamsterdam-nl.md) · usable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Series page shows actual date entries; no complex query required.

1. [web-extraction](https://www.buurtteamamsterdam.nl/serie/groepswandeling-in-de-natuur-amstelpark/): Live page fetch failed in the web extraction tool. Evidence: No event/access fields extracted. Error: Failed to fetch: web extraction cache miss; ordinary browser rendered the dated activity list.
2. [desktop-browser](https://www.buurtteamamsterdam.nl/serie/groepswandeling-in-de-natuur-amstelpark/): Rendered dated list 21/28 Oct and 4/11/18/25 Nov 2026, each 10:30–12:00 Evidence: title: Groepswandeling in de natuur, Amstelpark; date: 21 and 28 Oct; 4, 11, 18, 25 Nov 2026; time: 10:30–12:00.

Next step: Use the displayed series entries for dates and times; price and access terms were not established on the tested page.

### cameranu.nl

[Guide](cameranu-nl.md) · blocked · difficulty: low · retested: no

Initial public-page attempt reached the saved event URL; visible browser retry stopped at Cloudflare security verification, so event fields were inaccessible.

1. [desktop-browser](https://www.cameranu.nl/events/1287-photowalk-analoge-fotografie-met-fred-sansone-engelstalig): Ordinary browser displayed a Cloudflare “Performing security verification” challenge (Ray ID shown); no event content was accessible and no bypass was attempted. Evidence: No event/access fields extracted. Error: Cloudflare security verification blocked visible page content.

Next step: Stop at the Cloudflare security verification page; do not bypass it. Revisit only through a normal public page if access becomes available.

### circuslab.amsterdam

[Guide](circuslab-amsterdam.md) · excluded · difficulty: low · retested: no

Excluded by the active circus/juggling blacklist; guide-only review completed with no activity research.

Guide-only review; no live visit under the saved activity blacklist.

Next step:

### classpass.com

[Guide](classpass-com.md) · unavailable · difficulty: medium · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Page rendered a schedule but it was stale (Oct 6, already past); current future schedule was not established.

1. [web-extraction](https://classpass.com/studios/upclub-row-and-ride-amsterdam): Schedule excerpt is Tue Oct 6 with class names/times, an already-past date; pricing link shown but price not extracted Evidence: title: Upclub ROW & RIDE; date: 6 October (past on audit date); time: 17:00, 17:30, 18:00, 18:30, 19:00, 20:00.

Next step: The visible schedule was dated 6 October, already past; wait for future dates to load, and keep credit units separate from euros.

### clubcuisine.nl

[Guide](clubcuisine-nl.md) · usable · difficulty: medium · retested: yes

The calendar opened on September and October 2026 and ended with “Geen evenementen gevonden”; the guide did not state how to move to the target month.

1. [web-extraction](https://clubcuisine.nl/events/): The public event calendar displayed September and October entries and a no-events message, not the November entries described in saved evidence. Its period controls need to be operated before judging the target range. Evidence: title: Club Cuisine Events calendar; date: September/October 2026 visible in default view; time: Sep/Oct class times shown; target months not exposed; access: Calendar controls are visible; no November event shown in this view.
2. [desktop-browser](https://clubcuisine.nl/events/): Changed the visible month/year selectors to November 2026; calendar rendered Italian class Nov 2 18:00–22:00, Asian class Nov 3 18:00–22:00, and Tapas class Nov 7 17:00–21:00 at Sint Antoniesbreestraat 46. Evidence: title: Club Cuisine November class calendar; date: 2, 3 and 7 November 2026; time: 18:00–22:00 (Nov 2/3); 17:00–21:00 (Nov 7); access: One-time open-registration beginner classes; address Sint Antoniesbreestraat 46.

Next step: Open the November cards on the calendar and verify their own detail pages for per-person price and exact address before recommending a class.

### crea.nl

[Guide](crea-nl.md) · usable · difficulty: medium · retested: yes

The existing guide gave only the homepage and terms page, with no route to public event listings. The live route is homepage → Agenda → BASH calendar; the CREA guide now records this short path and a stop rule for multi-week courses.

1. [web-extraction](https://www.crea.nl/): Homepage exposed Agenda; Agenda page linked the public BASH event calendar, which displayed October event titles/date/times and free entry for Cotton Jazz on Oct 24 and Oct 31. Evidence: title: Cotton Jazz On Tour - CREA café; date: 2026-10-24; 2026-10-31; time: 16:30–19:30; price: Free; access: Public BASH calendar; event detail link is available.
2. [web-extraction](https://creaamsterdam.bash.social/): Retested the public calendar entry from the new quick start; the October listings and free-entry note rendered again. Evidence: title: Cotton Jazz On Tour - CREA café; date: 2026-10-24; 2026-10-31; time: 16:30–19:30; price: Free.

Next step: Use the BASH calendar route, then open the dated event detail where it is linked before relying on missing price or access information.

### dagjeweg.nl

[Guide](dagjeweg-nl.md) · unavailable · difficulty: low · retested: no

The saved guide incorrectly marked the whole DagjeWeg domain excluded because its one saved listing is climbing. The live homepage is a broad directory with Amsterdam/date filters; an allowed museum detail returned a Cloudflare challenge, so no dated eligible activity was captured.

1. [web-extraction](https://www.dagjeweg.nl/tip/9296/De-Klimmuur-Amsterdam-Centraal): Saved entry opened; it describes climbing and bouldering. Evidence: title: De Klimmuur Amsterdam Centraal; access: Climbing/bouldering; excluded.
2. [web-extraction](https://www.dagjeweg.nl/): Live directory homepage lists an Amsterdam museum tip and shows location/date filters; no dated allowed event packet captured. Evidence: title: Dagje uit tips and bezienswaardigheden.
3. [web-extraction](https://www.dagjeweg.nl/tip/1152/H%27ART-Museum): Live listing fetch failed with a cache miss before ordinary-browser retry. Evidence: No event/access fields extracted. Error: Web extraction cache miss; ordinary browser then returned Cloudflare HTTP 403.
4. [desktop-browser](https://www.dagjeweg.nl/tip/1152/H%27ART-Museum): Allowed Amsterdam H’ART Museum listing attempt returned HTTP 403 Cloudflare verification; no listing fields readable. Evidence: No event/access fields extracted. Error: Cloudflare HTTP 403 security challenge on this listing URL.

Next step: The homepage supports directory browsing, but the allowed H’ART listing hit a Cloudflare challenge; stop at that gate and leave event dates unavailable.

### debalie.nl

[Guide](debalie.md) · partial · difficulty: low · retested: no

The event detail directly supplied subject and speaker; event date is encoded in canonical slug and no price was exposed. The existing guide already gives a short working route.

1. [web-extraction](https://debalie.nl/programma/arnon-grunberg-meets-adania-shibli-05-11-2026/): Live event page named speakers and subject; date is present in URL slug only, not displayed page evidence; price not exposed. Evidence: title: Arnon Grunberg meets Adania Shibli; access: Literary conversation; ticket price and displayed date not exposed; 5-11-2026 appears only in the canonical URL slug.

Next step: The public event page gave speakers/topic but did not display a date or ticket price; verify a date on De Balie’s dated programme listing before using it.

### deceuvel.nl

[Guide](deceuvel-nl.md) · usable · difficulty: low · retested: no

The saved event detail places title, date/time, free admission, and location in the first screen of page text.

1. [web-extraction](https://deceuvel.nl/nl/event/adev-in-amsterdam-noord-dans-mee/): Opened event detail; displayed title, date, start/end, free entry and Amsterdam-Noord location. Evidence: title: ADEV in Amsterdam-Noord: dans mee!; date: 2026-10-24; time: 13:00–00:00; price: Free; access: Public event; route through Amsterdam-Noord to be announced.

Next step: Use the saved event page; retain the stated end time and note that the route is still to be announced.

### delokatie.org

[Guide](delokatie-org.md) · unavailable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Homepage describes thrift/reuse and supported work; no public dated workshop or event found.

1. [web-extraction](https://www.delokatie.org/): Homepage lists shop, recycling and work-experience services; no event calendar Evidence: title: De Lokatie homepage.

Next step: The homepage contains reuse/work-experience information but no public dated workshop; keep it unavailable for event capture.

### derooijfotografie.nl

[Guide](derooijfotografie-nl.md) · usable · difficulty: low · retested: no

The direct course page exposes dated availability, and says the in-range November course is full.

1. [web-extraction](https://www.derooijfotografie.nl/fotocursus/fotografie-cursus-amsterdam/): The public course page displayed Nov 21 10:00–16:00, €125 incl. VAT, beginner suitability, and full/waitlist status. Evidence: title: Fotografie Cursus Basis Amsterdam; date: 21 November 2026; time: 10:00–16:00; price: €125 incl. VAT; access: Sold out; waitlist offered.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### desteekamsterdam.com

[Guide](desteekamsterdam-com.md) · partial · difficulty: medium · retested: no

The homepage's seasonal promotion is stale and is not a dated visible-mending circle. A current beginner upcycling course page gives its duration and languages but asks the visitor to choose a preferred date/time in the booking flow; no dated occurrence or public price appeared on the page. This is a schedule/price evidence gap, not a wording failure.

1. [web-extraction](https://desteekamsterdam.com/nl/): Opened homepage; it links workshops and courses, but its prominently shown clothing swap is dated Sep 26 and not current. Evidence: title: De Steek Amsterdam — sewing café, workshops and sustainable fabric shop; access: Public workshops/course catalog linked from the homepage.
2. [web-extraction](https://desteekamsterdam.com/nl/product/beginner-upcycling-cursus/): Opened beginner course detail; it offers four two-hour lessons, English/Dutch instruction, and requires choosing a preferred date/time. No price or dated occurrence was displayed. Evidence: title: Beginnerscursus: upcycling; time: Four lessons of two hours each; date/time chosen by participant; language: English and Dutch; access: Beginner course; public page says choose desired date/time.

Next step: Keep this as an undated discovery lead; do not treat the rolling course or stale promotion as a dated one-off event.

### dezwijger.nl

[Guide](pakhuisdezwijger.md) · partial · difficulty: low · retested: no

Month agenda renders current entries; first visible entries were October. Saved month-specific route/detail instructions remain useful for November and need no change.

1. [web-extraction](https://dezwijger.nl/agenda): Agenda lists dated cards; visible example Shaping safe queer spaces, 22 Oct 19:30, English; base agenda shows months through Nov 2026 Evidence: title: Shaping safe queer spaces; date: 22 October 2026; time: 19:30.

Next step: Open a November month route and detail only for a candidate with an exact date/time; the live base agenda showed October entries.

### eastboundgym.nl

[Guide](eastboundgym-nl.md) · partial · difficulty: low · retested: no

Direct price page is readable in a public browser; single class is €16.50 but no dated schedule appears here.

1. [web-extraction](https://eastboundgym.nl/en/word-lid): Live open returned page title but no readable body; browser fallback used. Evidence: title: Become a member | Eastbound Gym.
2. [desktop-browser](https://eastboundgym.nl/en/word-lid): Browser fallback showed the public rates page and single-lesson / intro-package prices; no exact dated class occurrence appeared on this page. Evidence: title: Become a member | Eastbound Gym; price: Single lesson from €16.50; 3-class intro package €29.50.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### easylaughs.nl

[Guide](easylaughs-nl.md) · usable · difficulty: low · retested: no

Saved dated workshop detail pages directly expose event date/time, price, venue, language, and booking requirement.

1. [web-extraction](https://www.easylaughs.nl/event-info/workshop-my-favourite-things): Opened dated workshop page; title, date/time, venue, ticket price, English delivery, and online booking requirement visible. Evidence: title: WORKSHOP - My Favourite Things; date: 2026-11-01; time: 12:00–14:00; price: €15 incl. VAT; language: English; access: Online booking required; limited spaces; solo status unstated.

Next step: Use an individual saved workshop page and copy its explicitly listed ticket and language terms.

### equalyoga.com

[Guide](equalyoga-com.md) · unavailable · difficulty: medium · retested: no

The original guide had only the saved booking URL and generic recheck rules. Live extraction showed Amsterdam studio choices but no dated class rows, price or single-visit terms; the public calendar was not clicked.

1. [web-extraction](https://www.equalyoga.com/reserve/): Public page lists Amsterdam studios and class types; no date/time rows in extracted view Evidence: No event/access fields extracted.

Next step: Studio links are visible, but calendar selection and single-class terms remain untested; do not create dated entries from this page.

### eventbrite.com

[Guide](eventbrite-com.md) · partial · difficulty: medium · retested: yes

The saved booking URL redirects to a public multiple-date pottery event; selecting a displayed date is necessary to capture a real occurrence.

1. [web-extraction](https://www.eventbrite.com/e/1981431356526?aff=oddtdtcreator): Live open returned an internal fetch error; tried T3 preview, which reported host AppArmor unsupported, then used installed browser fallback. Evidence: No event/access fields extracted. Error: Web extraction internal error; T3 preview unsupported on host.
2. [desktop-browser](https://www.eventbrite.com/e/1981431356526?aff=oddtdtcreator): The browser opened the Eventbrite page after a .com to .nl redirect and displayed the event title, Atelier Kleie venue, and “Multiple dates”; exact date/price were not captured. Evidence: title: Pottery TASTER group workshop; access: Atelier Kleie, Amsterdam; multiple dates; beginner one-session format; per-person pricing stated, amount/date not captured in visible excerpt.
3. [desktop-browser](https://www.eventbrite.com/e/1981431356526?aff=oddtdtcreator): Clicked the visible Check availability control. It did not expose individual date options or a dated session; stopped without entering checkout. Public detail showed €79.83, Atelier Kleie, Amsterdam, and a two-hour beginner taster. Evidence: title: Pottery TASTER group workshop; price: €79.83 per person; access: Atelier Kleie, Amsterdam; multiple dates; beginner one-session format; date and start time not surfaced.

Next step: The public multiple-date page gives €79.83 and venue, but Check availability did not reveal dates; use only if the public date selector later exposes a dated slot, otherwise skip as unverified.

### eventbrite.nl

[Guide](eventbrite-nl.md) · usable · difficulty: low · retested: no

The Eventbrite page did not render through normal web extraction (Cache miss), but the documented headless Chromium browser fallback rendered the ordinary public page and evidence fields. This is an extraction-route limitation, not a prompt problem or access denial.

1. [web-extraction](https://www.eventbrite.nl/e/amsterdams-expat-board-games-sunday-tickets-2003292799691): Fetch returned Cache miss; no event content was extracted. Evidence: No event/access fields extracted. Error: Cache miss
2. [desktop-browser](https://www.eventbrite.nl/e/amsterdams-expat-board-games-sunday-tickets-2003292799691): Documented Chromium fallback loaded public event page (HTTP 200); observed event details without entering checkout. Evidence: title: Amsterdam's Expat Board Games Sunday; date: 2026-11-01; time: 17:00–20:00; price: Free ticket or €2 supporter ticket; event asks guests to order a drink; access: Everyone welcome; solo guests welcome; registration link displayed.

Next step: If web extraction returns Cache miss, use the ordinary visible browser route and stop before registration or checkout.

### fablab.waag.org

[Guide](fablab-waag-org.md) · unavailable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Fab Academy page states 2026 registration is closed; course is not a single drop-in event.

1. [web-extraction](https://fablab.waag.org/Fabacademy/fabacademy2026/): Page navigation states registration for Fab Academy 2026 is closed Evidence: title: Fabacademy2026; access: Registration closed.

Next step: Registration for Fab Academy 2026 is closed and the program is a course; do not use it as a single-visit listing.

### femmegym.nl

[Guide](femmegym-nl.md) · partial · difficulty: low · retested: no

Club page gives venue identity and class types; no actual class date or single-visit access price appears in this page.

1. [web-extraction](https://www.femmegym.nl/femmegym-de-smederij/): Live open returned page title but no readable body; browser fallback used. Evidence: title: FemmeGym de Smederij.
2. [desktop-browser](https://www.femmegym.nl/femmegym-de-smederij/): Browser fallback loaded the club page with venue address, opening hours, and group-class types. The page did not expose a dated class or drop-in price in the excerpt. Evidence: title: FemmeGym de Smederij; access: Group classes include Zumba, HIIT, Pilates and yoga; address 2de Oosterparkstraat 83.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### framerframed.nl

[Guide](framerframed.md) · partial · difficulty: low · retested: no

Agenda is readable and gives a dated workshop, but the observed workshop is explicitly for Black women with ADHD and/or autism; audience fit is restricted and event price was not stated. Exhibition date spans are not occurrence dates.

1. [desktop-browser](https://framerframed.nl/agenda/): Visible agenda page showed “Workshop: Fragments of Time Otherwise”, 1 Nov 2026 13:00–15:00, collage making for Black women with ADHD and/or autism. Exhibition spans also listed; not treated as single sessions. Price not stated. Evidence: title: Workshop: Fragments of Time Otherwise; date: 1 November 2026; time: 13:00–15:00; access: Collage workshop for Black women with ADHD and/or autism; price not stated.

Next step: Use the agenda only when its stated audience matches; check the workshop detail for price and registration terms. Do not turn exhibition date spans into event occurrences.

### freedamtours.com

[Guide](freedamtours-com.md) · partial · difficulty: medium · retested: no

The official homepage and FAQ provide schedule, language, access, group limits and tip-based terms, but only as recurring departures. The linked FareHarbor web extract returned an unrendered template; the ordinary browser showed the tour overview but no exact dated session, so no date was inferred.

1. [web-extraction](https://freedamtours.com/): Opened official homepage/FAQ; public tour types, daily departure times, duration, English language, reservation rule and tip-based pricing terms were visible. Evidence: title: Absolutely Amsterdam: Your introduction to Amsterdam’s history, culture & modern life; time: 10:30 and 14:00 daily; 17:30 Sunday–Friday; about 2.5 hours; price: Tip-based; voluntary tips, €15–€25 described as common; language: English; access: Reservation needed to guarantee a place; maximum five people per free tour booking.
2. [web-extraction](https://fareharbor.com/embeds/book/freedamtours/?full-items=yes): The linked booking page returned a broken template with an explicit 'FareHarbor did not load properly' / no-assets message; no calendar data extracted. Evidence: No event/access fields extracted. Error: Broken rendered template: no-assets
3. [desktop-browser](https://fareharbor.com/embeds/book/freedamtours/?full-items=yes): Browser rendered the public tour overview and detail (tip-based, English, Beursplein meeting point, about 2.5 hours), but exposed no dated availability before a further booking step. Evidence: title: ABSOLUTELY AMSTERDAM The #1 Best Rated Walking Tour in Amsterdam; time: Around 2.5 hours; no dated session displayed; price: Tip-based; no fixed ticket price displayed; language: English; access: Beursplein meeting point; public tour listing.

Next step: Keep the tour as a recurring offer until an exact date appears on a usable public calendar; preserve tip-based price wording.

### freewalkingtoursamsterdam.com

[Guide](freewalkingtoursamsterdam-com.md) · partial · difficulty: medium · retested: no

Original guide lacked a short field-copy prompt. Live tour detail states the €2 booking fee, voluntary separate tip, English language, 2-hour duration and Dam Square start; the public date calendar remained on “Loading dates…”, so no departure was verified.

1. [web-extraction](https://freewalkingtoursamsterdam.com/tours/free-classic-tour/): Live tour detail gives access/price/language/duration/meeting point; calendar control showed “Loading dates…” and no dated departure. Evidence: title: The Free Classic Tour Of Amsterdam; price: €2 booking fee per person; voluntary guide tip separate; language: English; access: Public tour; booking calendar dates did not load.

Next step: Keep date/time unknown while the departures calendar says “Loading dates”; record the €2 fee, voluntary tip, English and Dam Square only.

### gildeamsterdam.nl

[Guide](gildeamsterdam-nl.md) · unavailable · difficulty: low · retested: no

Initial extraction returned only a title; visible browser retry showed 2–2.5-hour walks only for the people booking together, with no open-group dated session.

1. [desktop-browser](https://gildeamsterdam.nl/wandelingen/): Visible public walking page body describes guided routes, approximately 2–2.5h, available only for the people who book together; no public dated open group. Evidence: title: Gilde Amsterdam guided walks; time: Guided walks last about 2–2.5 hours; access: Only with the people who book together; no public open-group dated session found.

Next step: Skip for solo attendance unless Gilde publishes an open-group dated walk; the observed walks are private bookings for the people who book together.

### heartandsoulstudio.nl

[Guide](heartandsoulstudio-nl.md) · usable · difficulty: medium · retested: yes

The date cards do not render in ordinary web extraction and show only 'Loading days…'. The saved guide led with a long historical Android/screenshot procedure. A live ordinary browser rendered Upcoming Sessions after scrolling, so the new quick start gives that short route and a rule not to infer the year from the yearless cards.

1. [web-extraction](https://www.heartandsoulstudio.nl/classes): Opened class catalog; Cozy Cup price €85 and other services visible, but date widgets remained at 'Loading days…'. Evidence: title: The Cozy Cup – Autumn Mug Workshop; price: €85; access: Beginner classes listed; date widget loading.
2. [web-extraction](https://www.heartandsoulstudio.nl/service-page/the-cozy-cup-autumn-mug-workshop): Page extraction failed without readable event content; ordinary browser route needed. Evidence: No event/access fields extracted. Error: Internal Error / no event content extracted
3. [desktop-browser](https://www.heartandsoulstudio.nl/service-page/the-cozy-cup-autumn-mug-workshop): Browser rendered Upcoming Sessions after the description; observed two cards and the price/material/pickup details. Evidence: title: The Cozy Cup – Autumn Mug Workshop; date: Sunday, Oct 25; Friday, Nov 6 (year omitted on session cards); time: 10:30 AM; 6:00 PM; price: €85; access: Beginner welcome, no experience needed; Hemonystraat 54H; clay/tools/glaze/firing included; finished work requires later pickup.
4. [desktop-browser](https://www.heartandsoulstudio.nl/service-page/the-cozy-cup-autumn-mug-workshop): Retested the new quick-start route; Upcoming Sessions again showed Oct 25 at 10:30 AM and Nov 6 at 6:00 PM, each 2h30 at Hemonystraat 54H. Evidence: date: Sunday, Oct 25; Friday, Nov 6 (year omitted); time: 10:30 AM; 6:00 PM.

Next step: Use the public service page in a regular browser to read Upcoming Sessions; do not add a year that the live cards omit.

### hetgroeneveld.amsterdam

[Guide](hetgroeneveld-amsterdam.md) · usable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Dated page gives event, time, price and address directly; prompt only needed route/copy fields.

1. [web-extraction](https://hetgroeneveld.amsterdam/en/event/kulture-kitchen-kraft-korner/2026-10-20/): Kulture Kitchen Kraft Korner, 20 Oct 2026 13:00–18:00, free, needlecraft, no experience needed, address Evidence: title: Kulture Kitchen Kraft Korner; date: 20 October 2026; time: 13:00–18:00; price: Free; access: No experience needed; supplies/advice provided.

Next step: The dated page has a complete craft-session packet; do not extend it from weekly recurrence alone.

### hetgymlokaal.nl

[Guide](hetgymlokaal-nl.md) · partial · difficulty: medium · retested: no

Initial extraction returned only the title and browser showed a cookie overlay; after choosing visible “Decline all”, the public page showed a €17.50 single-class/fitness credit but no dated class session.

1. [web-extraction](https://www.hetgymlokaal.nl/en/credits/): Live open returned page title but no readable body; browser fallback displayed a cookie-consent overlay. Evidence: title: Passes & Credits | Het Gymlokaal.
2. [desktop-browser](https://www.hetgymlokaal.nl/en/credits/): After choosing visible “Decline all” on the ordinary cookie modal, browser showed a single class/fitness credit at €17.50, valid one month at West and Noord. No dated session on this page. Evidence: title: Passes & Credits | Het Gymlokaal; price: Single class/fitness credit €17.50; access: One group class or fitness entry; valid one month at West and Noord; West/Noord addresses listed.

Next step: Use the pass page for the €17.50 single class/fitness-entry price; a separate public class roster is still needed for an exact date and time.

### hipsy.eu

[Guide](hipsy-eu.md) · partial · difficulty: medium · retested: no

The saved Dance Playground page exposes its date, time, venue and languages without sign-in, but the ticket button shows €13.30 while the description states €12.50 plus €1.15 Hipsy fees; preserve the discrepancy instead of selecting one total. Other hoopdance leads in the guide were not opened during this spot check, so their eligibility is unassessed.

1. [web-extraction](https://hipsy.eu/event/251312-dance-playground?source=EventPage): Opened public event detail; date/time, venue, ticket terms and spoken languages visible without entering the sign-in or ticket flow. Evidence: title: Dance Playground; date: 2026-10-21; time: 19:00–20:30; price: Displayed ticket €13.30; description says €12.50 + €1.15 fee (conflicting total); language: English and Dutch; access: Open to everyone; arrival at street door by 18:55; Overtoom 301.

Next step: Keep both displayed price expressions; assess any other hoopdance lead on its own merits before considering it.

### hipsy.nl

[Guide](hipsy.md) · usable · difficulty: medium · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Browser rendered event series and per-session ticket, though public extraction service could not open Hipsy.

1. [web-extraction](https://hipsy.nl/event/257835-moving-dialogues-contact-improvisation-workshop-steven-campos): Live page fetch failed in the web extraction tool. Evidence: No event/access fields extracted. Error: URL inaccessible to web extraction; ordinary browser rendered public event details.
2. [desktop-browser](https://hipsy.nl/event/257835-moving-dialogues-contact-improvisation-workshop-steven-campos): Rendered four Saturday sessions Nov 7/14/21/28, 16:30–18:00; single session €26.80; series €95.80 Evidence: title: Moving Dialogues | Contact Improvisation Workshop | Steven Campos; date: 7, 14, 21, 28 November 2026; time: 16:30–18:00; price: €26.80 per single class; €95.80 series.

Next step: Use the individual €26.80 session price and stated date/time; keep the €95.80 series price separate.

### huisvandebuurtdeboomsspijker.nl

[Guide](boomsspijker.md) · blocked · difficulty: medium · retested: no

The official October calendar loaded and exposes filters/date controls, but requesting November returned an explicit insufficient-rights page. Alternate public WijkConnect category and detail URLs returned extraction cache misses, not successful evidence. Treat the target-month route as blocked; do not infer or bypass it.

1. [web-extraction](https://huisvandebuurtdeboomsspijker.nl/agenda/kalender): Live venue calendar rendered 65 agenda items, October 2026 view, category/audience filters, and calendar controls. Evidence: title: De Boomsspijker Agenda; date: October 2026 calendar displayed; sample listings include Oct 1 onward; time: Visible October items include listed start times such as 09:30, 12:45, 13:00 and 18:00; access: Public calendar page; filters include adults, seniors, youth, wheelchair accessible and activity categories..
2. [desktop-browser](https://huisvandebuurtdeboomsspijker.nl/agenda/kalender?maand=2026-11): Visible browser returned a page titled ‘Pagina is afgeschermd’ and text ‘Je hebt helaas onvoldoende rechten.’ Evidence: No event/access fields extracted. Error: Explicit insufficient-rights denial for the November month route.
3. [web-extraction](https://www.wijkconnect.com/amsterdam/centrum-oost/agenda/film): Failed to fetch public Film category page (cache miss). Evidence: No event/access fields extracted. Error: Extraction cache miss; this is not evidence of a security block.
4. [web-extraction](https://www.wijkconnect.com/amsterdam/organisaties/8345/huis-van-de-buurt-de-boomsspijker/agenda/26159/film-dineravond-buurtbewoners): Failed to fetch public event detail page (cache miss). Evidence: No event/access fields extracted. Error: Extraction cache miss; no event fields rendered.

Next step: Retry the official public November calendar on a later audit or use an independently accessible public category listing; keep event facts unknown meanwhile.

### iamsterdam.com

[Guide](iamsterdam-com.md) · usable · difficulty: medium · retested: yes

Month controls and “Meer data” are necessary to expose future dated slots; the guide previously listed URLs without an observed navigation recipe.

1. [web-extraction](https://www.iamsterdam.com/uit/agenda/attracties-en-bezienswaardigheden/tours/open-atelier-creatief-maken-in-amsterdam): The city listing displayed €59, two-hour format, beginner access, and Oct 18/21/23 dates; month buttons and “Meer data” are visible for more dates. Evidence: title: Open Atelier: Creatief maken in Amsterdam; date: 18, 21 and 23 October 2026 visible; future months available via controls; time: 13:00–15:00 / 19:30–21:30; price: €59; access: No experience required; materials included.
2. [desktop-browser](https://www.iamsterdam.com/uit/agenda/attracties-en-bezienswaardigheden/tours/open-atelier-creatief-maken-in-amsterdam): Rejected optional cookies using visible Deny; clicked November month control. Table showed Nov 1, 4 and 6 sessions; details include €59, 2h, materials, no experience required, Oude Schans 21. Evidence: title: Open Atelier: Creatief maken in Amsterdam; date: 1, 4 and 6 November 2026; time: Sun 13:00–15:00; Wed/Fri 19:30–21:30; price: €59; access: No experience required; materials included; Oude Schans 21.

Next step: Use month controls and “Meer data” on the official listing, then copy the actual dated slot and stated price/access details.

### ivn.nl

[Guide](ivn-nl.md) · usable · difficulty: low · retested: no

The saved organizer event page clearly displays the exact date/time, free admission, mandatory registration, location, and adult audience; spoken language is not stated.

1. [web-extraction](https://www.ivn.nl/afdeling/amsterdam/natuuractiviteiten/herfstwandeling-in-het-beatrixpark-bijzondere-en-zeldzame-bomen-zaden-en-vruchten-2/): Opened organizer event detail; displayed date/time, location, free entry, mandatory signup, participant cap and adult tag. Evidence: title: Herfstwandeling in het Beatrixpark. Bijzondere en zeldzame bomen, zaden en vruchten; date: 2026-10-25; time: 13:00–14:30; price: Free; language: Not stated; access: Registration required by email; max 12 participants; adult audience; Beatrixpark–Diepenbrockstraat.

Next step: Use the exact organizer event page; keep spoken language unstated despite Dutch page copy.

### jaapeden.nl

[Guide](jaapeden-nl.md) · partial · difficulty: medium · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Pricing page shows single public skate ticket, but not individually dated public skating sessions.

1. [web-extraction](https://www.jaapeden.nl/praktische-informatie/tarieven/): Adult single skate ticket €10.60; rental excluded; public opening-times page linked, no dated slot here Evidence: title: Jaap Eden IJsbaan tariffs; price: Adult single ticket €10.60; skate rental extra.

Next step: The public single-entry rate is €10.60 before skate rental; use public opening times for dated sessions and keep rates separate.

### jiadamahjong.com

[Guide](jiadamahjong-com.md) · unavailable · difficulty: low · retested: no

The direct product page is a past September event; no matching future date is given by this saved URL.

1. [web-extraction](https://jiadamahjong.com/products/mahjongmalatang-mogu): The page explicitly marked the Sep 19 event as past; it displayed the event title, hours, address, beginner-friendly label, and optional separately paid dinner. Evidence: title: 2026.09.19 | Mahjong Malatang - MOGU; date: 19 September 2026; time: 14:00–17:00; access: Past event; beginner friendly; MOGU Central Amsterdam.

Next step: Use the organizer’s current events listing to find a new dated Mahjong session inside the requested horizon; the saved 19 September event is past and should not be reused.

### kantlijn.org

[Guide](kantlijn-org.md) · partial · difficulty: low · retested: no

The homepage is easy to read and confirms free weekly writing workshops and walk-in access, but it only gives recurring weekdays, not individually dated occurrences. Do not expand those recurrences into dates.

1. [web-extraction](https://kantlijn.org/): Opened organizer homepage; agenda lists weekly West, Oost and Noord workshops; newcomer walk-in, free prompts and feedback are stated. Evidence: title: Kantlijn weekly writing workshops; time: West Monday 14:00–16:00; Oost Friday 14:00–16:00; Noord Wednesday 14:00–16:00; price: Free; access: Newcomers may walk in; shared writing prompt and feedback; Dutch website text only, spoken language unstated.

Next step: Use the homepage for format and newcomer access only; find a separate dated listing before proposing an occurrence.

### keramiekatelier.nl

[Guide](keramiekatelier-nl.md) · unavailable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Old domain redirects to current studio course page; homepage advertises multi-class courses, no one-off public dated session.

1. [web-extraction](https://keramiekatelier.nl/): Live page fetch failed in the web extraction tool. Evidence: No event/access fields extracted. Error: Web extraction followed redirect to artceramicsstudio.com but could not fetch redirected page; ordinary browser loaded it.
2. [desktop-browser](https://keramiekatelier.nl/): HTTP 200 redirect to artceramicsstudio.com; title Pottery and Ceramics Classes; course is 10 classes Evidence: title: Art Ceramics Studio; access: 10-class course; beginner and experienced participants.

Next step: The domain redirects to a ten-class course page; no one-off dated session is published there.

### kookfabriek.nl

[Guide](kookfabriek-nl.md) · usable · difficulty: medium · retested: yes

Homepage describes group bookings for 8–250 people, but separately links to public masterclasses that welcome solo visitors; the guide did not distinguish these routes.

1. [web-extraction](https://www.kookfabriek.nl/): The public homepage says private/group outings serve 8–250 and the Masterclasses page welcomes solo visitors; no dated masterclass was visible on the homepage. Evidence: title: De Kookfabriek homepage; access: General group events require groups of 8–250; masterclasses welcome solo attendees.
2. [desktop-browser](https://www.kookfabriek.nl/masterclasses/): Opened visible Masterclasses link, then advanced calendar to November 2026. Amsterdam listings included Kimmy’s Kitchen Club Nov 1, 14, 15, 29; Lotte Vermeer Nov 8; Niven Kunz Nov 22, each 16:00–20:30; €99. Evidence: title: Kookfabriek Amsterdam masterclasses; date: 1, 8, 14, 15, 22 and 29 November 2026; time: 16:00–20:30; price: €99; access: Solo visitors welcome at masterclasses; distinct from 8–250-person group outings.

Next step: Use the Masterclasses calendar and copy the actual Amsterdam date/time; the observed one-off classes list €99 and welcome solo attendees.

### luma.com

[Guide](luma-com.md) · partial · difficulty: low · retested: no

The official Luma event detail directly exposes date/time, venue, event structure, solo welcome, and ticket categories, but the listed ticket prices were not rendered in the public page output.

1. [web-extraction](https://luma.com/offline-hangout-gemeente-amsterdam-2): Opened public event page; exact date/time, venue, programme, ticket categories and audience terms visible; no ticket amounts displayed. Evidence: title: Offline Hangout + Speedfriending | GenZ Editie | Live Gitaar | Nieuw-West; date: 2026-11-19; time: 19:00–22:00; access: Amsterdam youth and young adults; can come solo; Stadspas and Nieuw-West Local ticket types have eligibility conditions; two non-alcoholic drinks included.

Next step: Use the saved event page for date/time and eligibility; leave ticket amount unstated when no amount is displayed.

### mangoinapot.com

[Guide](mangoinapot-com.md) · usable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Dated event calendar exposes exact dates/times; details require one event link for price.

1. [web-extraction](https://www.mangoinapot.com/workshop-dates): Calendar shows Nov 3 freestyle object 18:00–20:30 and Nov 7 matcha set 10:00–12:30 Evidence: title: Handbuilding Ceramics: Freestyle object with Alyona; date: 3 November 2026; time: 18:00–20:30.

Next step: The calendar provides individual dates/times; open a detail only when a specific session price or access term is needed.

### maqam-amsterdam.nl

[Guide](maqam-amsterdam-nl.md) · usable · difficulty: medium · retested: yes

The saved Warda detail is for November 2025; the guide needs an explicit stale-page check and route to the current program.

1. [web-extraction](https://www.maqam-amsterdam.nl/projecten/majam-november-warda): Live extraction returned Cache miss; public browser fallback then opened the page. Evidence: No event/access fields extracted. Error: Cache miss in web extraction; not a source denial.
2. [desktop-browser](https://www.maqam-amsterdam.nl/projecten/majam-november-warda): Normal extraction reported cache miss; browser fallback loaded the page and showed it was a free 2025 event, so it cannot establish a current occurrence. Evidence: title: MAJAM November: Warda; date: 13 November 2025; time: Doors 19:00; jam starts about 19:30, ends about 22:00; price: Free; access: Past event; no string-instrument experience required.
3. [desktop-browser](https://maqam-amsterdam.nl/projecten/majam-november): From the stale 2025 saved page, opened Programma then MAJAM November. Current detail states 12.11.2026, doors 19:00, start 19:30, free, and everyone welcome without musical experience. Evidence: title: MAJAM November; date: 12 November 2026; time: Doors 19:00; start 19:30; price: Free; access: Everyone welcome without musical experience; soup and tea mentioned.

Next step: Follow Programma to the current MAJAM entry and copy its displayed event details; confirm performer lineup on the page before publishing it.

### meetup.com

[Guide](meetup-com.md) · usable · difficulty: medium · retested: no

Web extraction could not access two public Meetup pages (one returned inaccessible and another Cache miss), but ordinary browser loading of the saved Oct 24 event succeeded with a public event detail and no sign-in. This is an extraction limitation, not a prompt failure.

1. [web-extraction](https://www.meetup.com/nl-nl/amsterdam-walks-group/events/317000034/): Web extraction returned 'URL is not accessible via this tool'; no event content extracted. Evidence: No event/access fields extracted. Error: URL not accessible via web extraction
2. [web-extraction](https://www.meetup.com/nl-nl/amsterdice-boardgameclub/events/316179819/): Web extraction returned Cache miss; no event content extracted. Evidence: No event/access fields extracted. Error: Cache miss
3. [desktop-browser](https://www.meetup.com/nl-nl/amsterdam-walks-group/events/317000034/): Documented Chromium fallback loaded the public event page without sign-in; exact meeting point, details, date/time and free entry displayed. Evidence: title: Amsterdam citycentre 8 km walk; date: 2026-10-24; time: 13:00–15:00; price: Free; access: Meet at central station; 2-hour/5–10km walk; optional coffee; RSVP/join action visible but not used.

Next step: When web extraction cannot open a Meetup event, use an ordinary public browser page and stop before Join/RSVP.

### mezrab.nl

[Guide](mezrab-nl.md) · partial · difficulty: medium · retested: no

The original guide had no short copy prompt; the live month list exposes dates/times, but this audit did not open event details for price/access/language.

1. [web-extraction](https://mezrab.nl/full-program/): Live page opened; first extraction response did not expose an event packet. Evidence: No event/access fields extracted.
2. [web-extraction](https://mezrab.nl/full-program/): A live page search for “2026” exposed the November 2026 list, including Mythos on 3 Nov at 20:00 and other dated entries. Price/access/language were not opened. Evidence: title: Mythos. Ancient tales from all around the world.; date: 3 November 2026; time: 20:00.

Next step: The November list exposes dated titles and starts; event details for price/access/language were not opened.

### mkateliers.nl

[Guide](mkateliers-nl.md) · unavailable · difficulty: low · retested: no

Initial extraction showed only the catalogue header; visible browser retry showed recurring Friday 09:30–12:30 ceramics in eight-lesson blocks, requiring prior clay experience, and no one-off beginner session.

1. [desktop-browser](https://www.mkateliers.nl/cursussen/keramiek-en-porselein/): Visible course page body shows Friday 09:30–12:30 recurring ceramics course, five blocks of eight lessons, three hours per lesson, prior clay experience required; materials contribution per block. Evidence: title: Keramiek en porselein • Stichting MK Ateliers Amsterdam; time: Friday 09:30–12:30 recurring lesson; course blocks of 8 lessons, each 3h; access: Prior clay experience required; not a one-off beginner session.

Next step: Skip this catalogue for a solo beginner event: it lists multi-lesson ceramics courses requiring prior clay experience, not dated one-off sessions.

### monk.nl

[Guide](monk-nl.md) · excluded · difficulty: low · retested: no

Not included in the historical audit; guide-only review completed without opening activity pages.

Guide-only review; no live visit under the saved activity blacklist.

Next step:

### movementsyoga.com

[Guide](movementsyoga-com.md) · partial · difficulty: medium · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Price page has no dated session; schedule requires separate public route/branch selection.

1. [web-extraction](https://movementsyoga.com/pricing/): Pricing page gives a standalone single-class rate and date-limited offers; no dated schedule rows were shown. Evidence: title: Movements pricing; price: €25 for one Hot Yoga or Hot Pilates class.

Next step: Record €25 as the one-class price; a dated occurrence was not shown on the tested pricing page.

### museumnacht.amsterdam

[Guide](museumnacht-amsterdam.md) · usable · difficulty: low · retested: no

The programme page is directly readable in the browser; program details are clear but price is not shown.

1. [web-extraction](https://museumnacht.amsterdam/programma/the-book-club): Live page opened but normal extraction returned no readable body; browser fallback used. Evidence: title: The Book Club | Museumnacht Amsterdam.
2. [desktop-browser](https://museumnacht.amsterdam/programma/the-book-club): Browser fallback displayed the dated programme, time, venue, participation description, mostly-English note, and no-prior-reading requirement. Evidence: title: The Book Club; date: 7 November 2026; time: 19:00–00:00; language: Mostly English; access: Grachtenmuseum; no prior reading required; ticket price not stated.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### muziekgebouw.nl

[Guide](muziekgebouw-nl.md) · usable · difficulty: low · retested: no

The organizer listing places title, exact occurrence time, adult audience and ticket price together in the main event content.

1. [web-extraction](https://www.muziekgebouw.nl/nl/agenda/soundlab-workshop-s5cf): Opened official SoundLAB event detail; title, date/time, adult label, €13.50 price, venue and last-tickets status visible. Evidence: title: SoundLAB workshop; date: 2026-11-29; time: 15:00–16:30; price: €13.50; access: For adults; Muziekgebouw Atriumzaal; last tickets displayed.

Next step: Use the saved event detail and preserve the displayed last-tickets status.

### oba.nl

[Guide](oba.md) · partial · difficulty: low · retested: no

Existing guide already documents OBA search filters and event-detail route. Browser succeeded after direct extraction failed.

1. [web-extraction](https://oba.nl/nl/agenda/origami-club-a4152490-3af7-489e-8e58-66167a038b9a): Live page fetch failed in the web extraction tool. Evidence: No event/access fields extracted. Error: Web extraction returned internal error; ordinary browser rendered event detail.
2. [desktop-browser](https://oba.nl/nl/agenda/origami-club-a4152490-3af7-489e-8e58-66167a038b9a): Ordinary browser rendered event detail and multiple upcoming editions. No price was stated in the visible event content. Evidence: title: Origami Club; date: 21 October 2026; next editions 8 and 18 November 2026; time: 21 Oct 17:30–19:00; 8 Nov 11:00–12:30; 18 Nov 17:30–19:00; language: English (Dutch-speaking volunteers also present); access: Beginners 16+; registration required; paper provided.

Next step: The detail lists future dates, times, English instruction and required email registration; price was not stated.

### olvminor.nl

[Guide](olvminor-nl.md) · unavailable · difficulty: low · retested: no

The saved homepage explains beginner suitability but its current listed dates start in January 2027, beyond the audit horizon.

1. [web-extraction](https://www.olvminor.nl/): Live open returned an internal error; public browser fallback loaded the page. Evidence: No event/access fields extracted. Error: Internal fetch error in web extraction; not a source denial.
2. [desktop-browser](https://www.olvminor.nl/): Browser fallback loaded the public homepage and displayed its beginner-suitability statement; listed events were in 2027, outside the target horizon. Evidence: title: OLV MINOR; access: All ages and experience levels welcomed; next listed dates shown are Jan/Feb 2027.

Next step: Recheck only when the organizer posts dates in the target horizon; the currently visible January/February 2027 listings are outside this audit range.

### ottavi.nl

[Guide](ottavi-nl.md) · usable · difficulty: medium · retested: no

The public cooking-studio agenda is a long but plainly structured list: each dated event shows its exact start time, title, per-person price and live availability before the description.

1. [web-extraction](https://ottavi.nl/kookstudio/): Opened official event list; Nov 8 wine tasting/masterclass listed 13:30, €69 per person and 15 places; Nov 6 cooking workshop listed 18:00, €89 and full. Evidence: title: Kaas + Wijn = Fijn Proeverij & Masterclass; date: 2026-11-08; time: 13:30; price: €69 per person; access: 15 places displayed; cooking/tasting distinction is explicit in event title and description; venue Jan van Galenstraat 102H.

Next step: Read the date/title/time/price/availability fields above each description and do not treat gift cards as event prices.

### oudekerk.nl

[Guide](oudekerk-nl.md) · usable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Homepage displays dated public programs; open one individual entry for details.

1. [web-extraction](https://oudekerk.nl/): Homepage lists Nov 6 Silence #73 at 08:00; November 13–March 7 exhibition; event listings visible Evidence: title: Silence #73: Laryssa Kim; date: 6 November 2026; time: 08:00.

Next step: Use a dated program detail for event admission; daily museum opening hours are not event occurrences.

### overdebrug-oostenburg.nl

[Guide](overdebrug-oostenburg-nl.md) · usable · difficulty: low · retested: no

Direct event detail exposes the date, start/end, price, and beginner/solo suitability.

1. [web-extraction](https://overdebrug-oostenburg.nl/agenda/board-game-club-3/): Public event detail identifies the 4 Nov board-game club, 19:30–22:00, free admission, beginners/solo welcome, and venue address. Evidence: title: Board Game Club; date: 4 November 2026; time: 19:30–22:00; price: Free; access: Beginners and solo attendance welcome.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### parkrun.co.nl

[Guide](parkrun-co-nl.md) · blocked · difficulty: low · retested: no

Saved event page was directly attempted, but the public site returned HTTP 403 in the ordinary browser; no event fields rendered. This is an access denial, not a guide wording problem.

1. [web-extraction](https://www.parkrun.co.nl/amsterdamsebos/): HTTP 405 Method Not Allowed Evidence: No event/access fields extracted. Error: Live public-page extraction returned 405.
2. [desktop-browser](https://www.parkrun.co.nl/amsterdamsebos/): HTTP 403 Forbidden page Evidence: No event/access fields extracted. Error: Visible browser rendered a 403 Forbidden response; no date, time, price, language, or access fields.

Next step: Retry the same public page on a later audit; do not infer a weekly occurrence from the park run name.

### peterpan.nl

[Guide](peterpan-nl.md) · partial · difficulty: medium · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Page confirms open individual workshops and English-speaking chefs, but no dates/price in current page extract.

1. [web-extraction](https://peterpan.nl/en/cooking-class-amsterdam/agenda-open-cooking-workshop-amsterdam/): Individual classes open to individuals/small groups; chefs speak English; no dated slot or price shown Evidence: title: Individual cooking classes; language: Chefs speak English; access: Open workshops for individuals and small groups.

Next step: The page confirms open individual workshops and English-speaking chefs; no dated workshop or price was shown.

### pretix.eu

[Guide](pretix-eu.md) · usable · difficulty: medium · retested: no

The public ticket page loaded in browser fallback and clearly marks every free slot fully booked with waiting lists.

1. [web-extraction](https://pretix.eu/API/NvdN26/): Live extraction said URL was not accessible via this tool; public browser fallback loaded the event page. Evidence: No event/access fields extracted. Error: Extraction tool limitation; browser succeeded.
2. [desktop-browser](https://pretix.eu/API/NvdN26/): Web extraction could not access the Pretix page; browser fallback displayed the dated event and all four free slots as fully booked with waiting-list options. No order was placed. Evidence: title: Nacht van de Nacht; date: 24 October 2026; time: 20:00–23:59; slots at 20:00, 21:00, 22:00, 23:00; price: Free; access: All slots fully booked; waiting lists shown.

Next step: The page supplies the exact free slots and fully-booked/waitlist status; no further extraction route is needed unless checking for later released capacity.

### repaircafe.amsterdam

[Guide](repaircafe-amsterdam.md) · usable · difficulty: medium · retested: yes

The saved venue card's Next time field was stale and contradicted the current dated Agenda rows. The guide lacked route and source-priority instructions for agenda date/time, venue scope/address, and FAQ costs.

1. [web-extraction](https://repaircafe.amsterdam/en): Live Agenda listed dated October and November occurrences including Kleding Repair Café and De Boomsspijker; rows showed date/time and district. Evidence: title: Kleding Repair Café; De Boomsspijker Repair Café; date: 2026-10-19; 2026-11-02; time: 10:00–11:30; 13:00–15:00; access: Agenda is publicly readable; named venue rows available..
2. [web-extraction](https://repaircafe.amsterdam/en/cafe/de-boomsspijker): Venue card supplied address and repair scope but displayed an out-of-date Next time field (September). Evidence: title: De Boomsspijker Repair Café; date: 2026-09-07 (stale Next time field; not used as current agenda date); access: Address Recht Boomssloot 52; electronics repairs..
3. [web-extraction](https://repaircafe.amsterdam/en/repaircafes): Organizer FAQ states admission and repair help are free; optional contribution; parts and refreshments may cost extra. Evidence: price: Admission and repair help free; optional contribution; parts/refreshments may cost extra.; access: Walk-in repair café; repair help subject to volunteer capacity..
4. [web-extraction](https://repaircafe.amsterdam/en): Retest after quick-start edit showed same dated Agenda rows and current date/time; stale venue-card warning retained. Evidence: title: Kleding Repair Café; De Boomsspijker Repair Café; date: 2026-10-19; 2026-11-02; time: 10:00–11:30; 13:00–15:00.

Next step: Use the current Agenda row as the occurrence source, and keep any conflicting venue-card date out of extracted event data.

### sambaschoolfidelinas.nl

[Guide](sambaschoolfidelinas-nl.md) · usable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Beginner page puts dated entries and single-visit price together.

1. [web-extraction](https://www.sambaschoolfidelinas.nl/lessen/samba-beginners): Nov 4/11/18/25, 19:00–20:00, €15 per class; beginner, solo-oriented Evidence: title: Samba Beginners Class in Amsterdam; date: 4, 11, 18, 25 November 2026; time: 19:00–20:00; price: €15 per class; access: Beginner; solo, no partner/equipment needed.

Next step: The beginner page gives upcoming dates and €15 per class; solo attendance and beginner level are explicit.

### shop.brandmeesters.nl

[Guide](shop-brandmeesters-nl.md) · usable · difficulty: low · retested: no

The direct booking detail page exposes exact date/time, price, language, and stock without checkout.

1. [web-extraction](https://shop.brandmeesters.nl/barista-workshop-29112026-1330.html): The public product page showed Nov 29, 13:30 to approx. 15:30/16:00, €85, Dutch, beginner barista basics, and stock. Evidence: title: Barista Workshop 29.11.2026 13:30; date: 29 November 2026; time: 13:30–15:30/16:00; price: €85; language: Dutch; access: In stock; beginner basics; Maasstraat 84.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### simoneheijloo.nl

[Guide](simoneheijloo-nl.md) · usable · difficulty: medium · retested: yes

The same page contains a current October–November Dates & Fee schedule and an older June block with conflicting prices. The guide did not tell Luna which dated block to trust.

1. [web-extraction](https://simoneheijloo.nl/african-contemporary/): Live page displayed current Oct–Nov dated schedule and lower June schedule with different prices. Evidence: title: African Contemporary — De Hallen; date: 2026-10-05, 2026-10-19, 2026-10-26; 2026-11-02, 2026-11-09, 2026-11-16; time: Mondays 18:30–19:30; price: Current block: €105 for all six / €20 single; older June block shows €85 / €18; access: Open to everyone; signup by email or booking page; Studio Belcampo Loft, De Hallen..
2. [web-extraction](https://simoneheijloo.nl/african-contemporary/): Retest after quick-start edit confirmed current Dates & Fee block and older June block remain visible with conflicting prices. Evidence: title: African Contemporary — De Hallen; date: 2026-10-05, 2026-10-19, 2026-10-26; 2026-11-02, 2026-11-09, 2026-11-16; time: Mondays 18:30–19:30; price: Current block: €105 series / €20 single; older June block: €85 / €18.

Next step: Keep only dates explicitly enumerated in the current block; retain the conflicting old fee as a warning, not an alternative current price.

### singsing.nl

[Guide](singsing-nl.md) · partial · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Page confirms walk-in open karaoke and recurring hours; no dated special event or public entry price.

1. [web-extraction](https://singsing.nl/en/open-karaoke/): Open karaoke, walk-in/no reservation; weekdays 20:00–04:00, Fri/Sat to 05:00; no admission fee stated Evidence: title: Open karaoke; time: Daily 20:00–04:00; Fri/Sat to 05:00; access: Walk-in, no reservation; two microphones circulate.

Next step: The page confirms open walk-in karaoke and hours; no dated special night or public admission price is listed.

### smaakcultuur.nl

[Guide](smaakcultuur-nl.md) · usable · difficulty: low · retested: no

The direct workshop page shows the November occurrence and exact price/time; no further navigation is needed.

1. [web-extraction](https://www.smaakcultuur.nl/workshop-zuurdesembrood): The public page showed Nov 20 13:30–16:00 at SMEG Showroom, €75, beginner suitability, and advance starter preparation. Evidence: title: Zuurdesem workshop; date: 20 November 2026; time: 13:30–16:00; price: €75 incl. VAT/materials; language: Dutch; English if group wants; access: Beginner friendly; starter to prepare in advance.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### sobamsterdam.nl

[Guide](sobamsterdam-nl.md) · partial · difficulty: low · retested: no

The public page gives recurring Friday hours and participation terms, but no individually dated target-window occurrence or price. Do not generate dates from the weekly schedule.

1. [web-extraction](https://www.sobamsterdam.nl/taalcafe/): Live language-café page displayed recurring Friday schedule and participation conditions. Evidence: title: SOB Amsterdam Taalcafé; time: Fridays 17:00–18:30; language: Dutch learning café; spoken languages of the session not stated; price: Not stated; access: No registration; for people learning Dutch; non-students welcome if they live or work in Amsterdam; Borgerstraat 52A..

Next step: Wait for an individually dated public listing before treating it as a target-window occurrence.

### soozamsterdam.nl

[Guide](soozamsterdam-nl.md) · partial · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Volunteer page allows one-off helping but provides no dates; it is not a public meal listing.

1. [web-extraction](https://soozamsterdam.nl/meedoen/helpend-handje/): One-off kitchen help and other volunteer roles described; no dates/price; volunteer role not meal access Evidence: title: Helpend handje; access: One-off volunteering possible; kitchen help offered.

Next step: The site permits one-off volunteering but gives no shift dates; treat the kitchen role as volunteering, not meal access.

### sportcity.nl

[Guide](sportcity-nl.md) · partial · difficulty: medium · retested: yes

The saved Zumba explainer has no exact session; the page links to a separate club/date roster and says group classes require membership.

1. [web-extraction](https://www.sportcity.nl/amsterdam/zumba): The Zumba page gives all-level suitability and membership requirement, and links to the group-class roster; it does not display an exact date or session. Evidence: title: Zumba in Amsterdam; access: All levels; live group class access requires Fitness & Groepslessen membership; class about one hour.
2. [desktop-browser](https://www.sportcity.nl/amsterdam/waterlooplein/groepslesrooster): Rejected optional cookies with visible Weigeren; opened club selector, chose Amsterdam Waterlooplein and opened roster. Public roster displayed Week 42 (12–18 Oct) only; no target-range session was observed and no future-week control was tested. Evidence: title: Groepslesrooster Amsterdam Waterlooplein; date: Visible week 42: 12–18 October 2026 only; access: Zumba page states group lessons require Fitness & Groepslessen membership.

Next step: The public Waterlooplein roster loaded only its current Week 42 (12–18 Oct); no target-horizon session was exposed. Stop unless a public future-week control appears, and preserve membership requirement.

### sportclubmatch.nl

[Guide](sportclubmatch-nl.md) · partial · difficulty: medium · retested: yes

The saved URL is a Pilates page although the source title says Zumba Gold. It shows recurring hours and several price types, so the guide needed to prevent activity substitution and date inference.

1. [web-extraction](https://sportclubmatch.nl/en/fitness/pilates/): Live page is a Pilates listing, with weekly schedule and single/monthly prices; no specific dates or spoken language shown. Evidence: title: Pilates; time: Saturday 10:00–11:00; Monday 18:30–19:30; price: Monthly single weekly class €34 (€44 with coffee); drop-in class or gym day pass €10.50; one-time registration €19.50; first Pilates taster free; access: Sint Gilleshof 5; recurring timetable only; dates and spoken language unstated..
2. [web-extraction](https://sportclubmatch.nl/en/fitness/pilates/): Retest after quick-start edit confirmed the Pilates activity, recurring hours and price labels. Evidence: title: Pilates; time: Saturday 10:00–11:00; Monday 18:30–19:30; price: €34 monthly; €10.50 drop-in/gym day; €19.50 registration; free first taster.

Next step: Do not treat recurring class times as dated events or attribute the Pilates prices to Zumba Gold.

### spui25.nl

[Guide](spui25.md) · partial · difficulty: low · retested: no

Existing guide gives a direct month URL, clear extraction steps and stop rule. Live agenda showed several dated entries, but visible starts at 17:00 do not meet the requested weekday time window; event prices were absent.

1. [web-extraction](https://www.spui25.nl/agenda/location/spui25/start/2026/11): November agenda shows exact dates/times and location; examples include 4 Nov 17:00 and 25 Nov 17:00. Registration links appear, but no price was stated. Evidence: title: Beeldregie in politiek Den Haag; date: 4 November 2026; time: 17:00; access: Registration link shown; price unstated.

Next step: The November agenda has dates and starts, but observed 17:00 weekday events fall outside the requested time window; price was not stated.

### stadswandelkantoor.nl

[Guide](stadswandelkantoor-nl.md) · partial · difficulty: low · retested: no

Detailed saved guide already notes open-tour signup, €17.50 and no public individual dates; current page confirms this.

1. [web-extraction](https://www.stadswandelkantoor.nl/nieuw): Open tours available for signup; €17.50/€20 per person, cash; page form has no visible individual dated departure Evidence: title: Open Rondleidingen; price: €17.50 or €20 per person; cash on site; access: Signup available; no dated departure visible.

Next step: The catalogue gives tour prices but no dated departure; keep the offer undated until a specific start appears.

### station-west.amsterdam

[Guide](station-west-amsterdam.md) · partial · difficulty: low · retested: no

Official calendar lists dated sessions and prices directly; the first current entries were 16–19 Oct, so target dates require scanning farther down.

1. [web-extraction](https://station-west.amsterdam/creatieve-workshops-in-amsterdam/): The live official calendar directly exposed dated single-session cards and price/status; Nov entries are farther down the same page. Evidence: title: Creatieve workshops in Amsterdam; date: 16–19 October 2026 visible near top; time: 10:30–12:00; other displayed sessions 11:00–13:00, 14:30–16:30; price: €18–€37 for visible single sessions; access: Calendar labels one-session tickets and sold-out status.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### stcamsterdam.nl

[Guide](stcamsterdam-nl.md) · usable · difficulty: medium · retested: yes

Guide listed many individual shifts but had no route to the live dated calendar. Following the site’s Event calendar link exposed dates/statuses, then the individual page supplied eligibility and language.

1. [web-extraction](https://www.stcamsterdam.nl/events/saturday-team-up-to-clean-up-sloterpark-west/): Live saved event page describes the Sloterpark cleanup and signup terms, but does not show an occurrence date or time on the detail page. Evidence: title: Saturday | Team up to clean-up Sloterpark | West; language: English/Dutch; access: Only Netherlands residents may volunteer; signup required; friends/family must also sign up..
2. [web-extraction](https://www.stcamsterdam.nl/event-calendar/): Calendar displayed dated shifts including Sloterpark cleanup Oct 24, 2026 14:00–16:00, plus target-window November entries and Full/Canceled status labels. Evidence: title: Saturday | Team up to clean-up Sloterpark | West; date: 2026-10-24; time: 14:00–16:00; access: Public calendar; statuses include Full and Canceled..
3. [web-extraction](https://www.stcamsterdam.nl/event-calendar/): Retest after guide edit reconfirmed the live calendar and dated rows, including Oct 24 Sloterpark cleanup at 14:00–16:00. Evidence: title: Saturday | Team up to clean-up Sloterpark | West; date: 2026-10-24; time: 14:00–16:00.

Next step: Use the calendar as occurrence source and the individual shift page for eligibility/language; do not enter signup.

### stretchandfold.nl

[Guide](stretchandfold-nl.md) · usable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Calendar exposes dated events; detailed page needed for single-visit cost/access.

1. [web-extraction](https://www.stretchandfold.nl/events): Nov 18 Kimchi Making 19:00–21:00; Nov 25 Paint & Sip 18:30–21:00, beginner-friendly Evidence: title: Craft Club: Kimchi Making; date: 18 November 2026; time: 19:00–21:00.

Next step: Use calendar rows for title/date/time; event price and beginner access were not opened on this audit.

### studio-koekoek.com

[Guide](studio-koekoek-com.md) · usable · difficulty: low · retested: yes

Catalog opened directly and the saved guide already has working sort/list steps; extracted response did not include card details in this attempt.

1. [web-extraction](https://studio-koekoek.com/product-category/workshops/workshops-with-seats/): The current catalog page opened; no card fields were included in this extraction response. Existing guide already records an observed catalog route and stop rule. Evidence: title: Workshops with available seats - Studio Koekoek.
2. [web-extraction](https://studio-koekoek.com/product/31-october-2026-1400-workshop-ton-sur-ton/): Opened the public product detail from the saved workshop route. Page states 31 Oct 2026, 14:00–16:30, €69, in stock, 2.5 hours, beginner suitable, materials included, Dutch and English, Weesperstraat 100. Separate catalog browser attempt returned 403. Evidence: title: Workshop Ton sur Ton; date: 31 October 2026; time: 14:00–16:30; price: €69; language: Dutch and English; access: In stock; beginner suitable; materials included; Weesperstraat 100.

Next step: Catalog browser view returned 403; use the public product detail route when the catalog or saved card supplies it, then verify exact date, stock and beginner fit without adding to cart.

### studio191.nl

[Guide](studio191-nl.md) · partial · difficulty: medium · retested: yes

Text extraction omitted the schedule rows; an ordinary visible browser rendered the weekly timetable. The visible week was Oct 18–24 and the captured event detail was on Oct 18, so this attempt did not verify a future target-window occurrence. Guide now says to wait for the browser schedule and stop when requested dates are not shown.

1. [web-extraction](https://studio191.nl/schedule/): Page exposed class navigation, studio choices, and walk-in/advance-booking statement but schedule rows were missing from extracted text. Evidence: access: Walk-ins allowed; advance booking recommended to guarantee a class place.. Error: Schedule widget rows were absent from extraction.
2. [desktop-browser](https://studio191.nl/schedule/): Visible browser rendered week Sun 10/18–Sat 10/24 and class details, including Power Pilates Sunday Oct 18 08:30–09:20 at Mat Studio (de Pijp); week UI exposed the schedule but no future target-window row was captured. Evidence: title: Power Pilates; date: 2026-10-18; time: 08:30–09:20; access: Schedule shows booking status; page says walk-in allowed, booking recommended..
3. [desktop-browser](https://studio191.nl/prices/): Visible pricing page distinguishes single class (€20), Intro 3 (€40), and Reformer single (€28); Intro 3 and single class do not cover Reformer. Evidence: price: Single class €20; Intro 3 €40; Reformer single €28; access: Class passes valid one month (single) / one month (Intro 3); Reformer separate..
4. [desktop-browser](https://studio191.nl/schedule/): Retest after quick-start edit rendered the same Oct 18–24 week timetable and class rows; request-range stop rule remains necessary. Evidence: title: Power Pilates; date: 2026-10-18; time: 08:30–09:20.

Next step: For future weeks, use only a visibly confirmed date before claiming a target-window class; do not infer from recurrence.

### theartcafe.nl

[Guide](theartcafe-nl.md) · usable · difficulty: low · retested: no

Original guide had no compact field-copy prompt. Live calendar displays an individually dated November event and its time/price; detail route is not required for this observed packet.

1. [web-extraction](https://www.theartcafe.nl/nl/workshops): Live calendar lists Model Schilderen on 13 Nov 2026, 19:30–22:00, at 6F Waterlooplein; page states €40 and no experience required. Evidence: title: Model Schilderen; date: 13 November 2026; time: 19:30–22:00; price: €40; access: No experience required.

Next step: The live calendar provides 13 Nov, 19:30–22:00 and €40; language was not stated.

### theatersport.nl

[Guide](theatersport-nl.md) · usable · difficulty: low · retested: no

Initial extraction returned title only; visible browser retry showed 24 Nov 20:45–22:30, €10 + €0.25, Polanentheater, all experience levels.

1. [desktop-browser](https://www.theatersport.nl/event-details/proefles-improvisatietheater-24-november-2026): Visible event detail body showed 24 Nov 2026 20:45–22:30, €10 plus €0.25, Polanentheater, beginner/any experience welcome. Evidence: title: Proefles Improvisatietheater; date: 24 November 2026; time: 20:45–22:30; price: €10 + €0.25 fee; access: Polanentheater; all experience levels can try.
2. [desktop-browser](https://www.theatersport.nl/event-details/proefles-improvisatietheater-24-november-2026): Visible browser body supplied date, time, price, venue and all-experience invitation missing from extraction excerpt. Evidence: title: Proefles Improvisatietheater; date: 24 November 2026; time: 20:45–22:30; price: €10 + €0.25 fee; access: Polanentheater; all experience levels welcome.

Next step: Use the public event detail; confirm availability there if needed. It explicitly invites people to try all experience levels.

### theclayroomamsterdam.com

[Guide](theclayroomamsterdam-com.md) · partial · difficulty: low · retested: no

Direct workshop page lists Sunday 22 November 13:30–16:00, €75, available spots, beginner-friendly 2.5-hour workshop, English instruction, and materials/firing included; the page does not display the year beside the date, so the specific 2026 occurrence is unverified.

1. [web-extraction](https://www.theclayroomamsterdam.com/service-page/festive-fun-afternoon-workshop): Live organizer page lists Sunday 22 November 13:30–16:00, €75, available spots, beginner-friendly 2.5-hour workshop, English instruction, materials/firing included; page does not display the year beside the date. Evidence: title: Festive Fun - Afternoon Workshop; date: Sunday 22 November (year not displayed on page); time: 13:30–16:00; price: €75; language: English; access: No experience necessary; children welcome when accompanied by an adult; available spots shown..

Next step: Confirm the year from a current dated page before treating the November date as a specific 2026 occurrence.

### toastmasters.org

[Guide](toastmasters-org.md) · partial · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Club profile gives recurring meeting schedule and free guest terms, but no instance date; address is listed.

1. [web-extraction](https://www.toastmasters.org/Find-a-Club/00009210-00009210): 2nd and 4th Friday 19:30; Bilderberg Garden Hotel address; free guest visits, participation optional Evidence: title: Amsterdam Toastmasters Club; time: 2nd and 4th Friday, 19:30; price: Free guest visit; access: Open to all interested parties; no pressure to participate; location on page.

Next step: The profile supports free guest visits and recurring Friday time; an individually dated meeting was not shown.

### tolhuistuin.nl

[Guide](tolhuistuin.md) · usable · difficulty: low · retested: no

Initial extraction returned title only; visible browser retry showed ONE FINE MESS on 13 Nov, doors 18:30, 19:00–23:59, free, English, IJzaal.

1. [desktop-browser](https://tolhuistuin.nl/evenementen/one-fine-mess-9): Visible event detail body showed Friday 13 Nov 2026, doors 18:30, event 19:00–23:59, free, English, IJzaal. Evidence: title: ONE FINE MESS; date: 13 November 2026; time: Doors 18:30; event 19:00–23:59; price: Free; language: English; access: IJzaal, Tolhuistuin.
2. [desktop-browser](https://tolhuistuin.nl/evenementen/one-fine-mess-9): Ordinary visible browser showed the complete event details; extraction excerpt was title-only. Evidence: title: ONE FINE MESS; date: 13 November 2026; time: Doors 18:30; event 19:00–23:59; price: Free; language: English; access: IJzaal, Tolhuistuin.

Next step: Use the event detail for this date and verify availability on the public event page when needed; no account or purchase is needed to extract these fields.

### tomgoldhand.com

[Guide](tomgoldhand-com.md) · usable · difficulty: low · retested: no

The saved course page clearly enumerates dates and fees, but it is a 14-class course with limited single-class spots and signup/downpayment requirements; do not present it as an unrestricted drop-in.

1. [web-extraction](https://tomgoldhand.com/dance-classes-workshops/dance-improvisation-classes-in-amsterdam/): Live page lists Monday 10:15–12:00, dates through Nov 30, 2026; 20 full-course places and five card/single-class places; registration required. Full course fee varies by income (€170/€185/€200), single €23, first tryout €18. Evidence: title: Dance Improvisation Course (Monday / Amsterdam); date: 2026-10-19, 2026-10-26, 2026-11-02, 2026-11-09, 2026-11-16, 2026-11-23, 2026-11-30; time: 10:15–12:00; price: Full course €170/€185/€200 by income; single class €23; first tryout €18; access: 20 full-course places; five card/single class places; signup and downpayment required; Belcampo Loft, De Hallen..

Next step: Keep course commitment and limited single-class availability explicit; do not infer availability from the listed dates.

### upclubstudios.com

[Guide](upclubstudios-com.md) · partial · difficulty: medium · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Home page confirms formats and intro deal but no dated class schedule or standalone single class price.

1. [web-extraction](https://upclubstudios.com/): ROW/RIDE/STRENGTH described; 2 workouts for €19; no class occurrence date on homepage Evidence: title: Upclub ROW & RIDE workouts; price: Intro offer: 2 workouts for €19.

Next step: The homepage supports workout formats and a two-workout €19 intro offer; current dated classes and single-class price remain unknown.

### volkssterrenwachtamsterdam.nl

[Guide](volkssterrenwachtamsterdam-nl.md) · usable · difficulty: low · retested: no

Browser fallback reads a current exact event page; advance registration is stated, while price/language are not.

1. [web-extraction](https://www.volkssterrenwachtamsterdam.nl/index.php/outreach/outreach202611api): Live open returned an internal fetch error; public browser fallback loaded the event page. Evidence: No event/access fields extracted. Error: Internal fetch error in web extraction; not a source denial.
2. [desktop-browser](https://www.volkssterrenwachtamsterdam.nl/index.php/outreach/outreach202611api): Web extraction failed to fetch; browser fallback displayed the exact Nov 20 event and advance-registration requirement. Price and language were unstated. Evidence: title: Publieke Sterrenkijkavond; date: 20 November 2026; time: 19:00–22:00; access: Everyone welcome; advance UvA registration required; Science Park 904.

Next step: Keep the direct saved URL. Retest only if the next audit needs fields this page did not expose.

### volksuniversiteitamsterdam.nl

[Guide](volksuniversiteitamsterdam-nl.md) · usable · difficulty: medium · retested: yes

The saved link opened a broad catalogue without navigation guidance. Opening a concrete course detail exposed status, fee, duration, location, and exact course dates; the new quick start directs Luna to an individual detail page and flags multi-session commitment.

1. [web-extraction](https://www.volksuniversiteitamsterdam.nl/): Live homepage offers category navigation and online/in-person catalogue cards with prices/statuses, but no dates in the sampled cards. Evidence: title: Volksuniversiteit Amsterdam course catalogue; price: Homepage samples include €195 online course, €400 documentary course, and €22 lecture; access: Catalogue cards show statuses such as Open, Last chance, or Last places..
2. [web-extraction](https://volksuniversiteitamsterdam.nl/cursussen/maak-je-eigen-korte-documentaire): Course detail lists Oct 30, Nov 6, 13, 20, 27 2026 at 13:00–15:00; €400 for eight weekly two-hour sessions; open signup; OBA Oosterdokskade. This is a multi-session course, not a single drop-in. Evidence: title: Maak je eigen korte documentaire; date: 2026-10-30, 2026-11-06, 2026-11-13, 2026-11-20, 2026-11-27; time: Fridays 13:00–15:00; price: €400 for eight two-hour meetings; access: Status Open; eight weekly sessions at OBA Oosterdokskade; signup available..
3. [web-extraction](https://volksuniversiteitamsterdam.nl/cursussen/maak-je-eigen-korte-documentaire): Direct-URL retest returned not accessible; following the course card from the homepage again displayed the dated schedule, €400 price, and open status. Evidence: title: Maak je eigen korte documentaire; date: 2026-10-30, 2026-11-06, 2026-11-13, 2026-11-20, 2026-11-27; time: Fridays 13:00–15:00; price: €400 for eight meetings; access: Open course enrollment; multi-session course.. Error: Direct URL route was inaccessible to extraction; homepage-to-course-card route succeeded on retest.

Next step: Use the homepage-to-course-card route when a copied course URL is inaccessible; preserve the multi-session commitment explicitly.

### vondelgym.nl

[Guide](vondelgym-nl.md) · partial · difficulty: medium · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Zuid page gives €19.50 day pass and explicit schedule link, but no dated class; day pass inclusion must be verified.

1. [web-extraction](https://www.vondelgym.nl/gyms/vondelgym-zuid): Day pass €19.50 (shown valid 4 weeks) and schedule link; no dated class details on branch page Evidence: title: Vondelgym Zuid; price: €19.50 day pass; access: FAQ says one group lesson may be included; must verify schedule/class terms.

Next step: The Zuid page gives a €19.50 day pass; the class schedule was not inspected, so dated class admission remains unknown.

### vrijeacademie.nl

[Guide](vrijeacademie-nl.md) · usable · difficulty: low · retested: no

Initial extraction returned title only; visible retry after rejecting optional cookies showed 15 Nov 14:00–17:00, €89, materials included and nearly full/waitlist; booking asks for an account, which was not entered.

1. [desktop-browser](https://www.vrijeacademie.nl/ons-aanbod/workshop-cyanotype/): After choosing visible “NIET AKKOORD” for optional cookies, browser showed 15 Nov 14:00–17:00, €89, Amsterdam, materials included, nearly full/waitlist. Booking requires an account; stopped before booking. Evidence: title: Workshop Cyanotype; date: 15 November 2026; time: 14:00–17:00; price: €89; access: In person, Amsterdam; materials included; almost full/waitlist; booking page asks for account.
2. [desktop-browser](https://www.vrijeacademie.nl/ons-aanbod/workshop-cyanotype/): Rejected optional cookies using visible “NIET AKKOORD”; displayed exact date/time/price and waitlist status. Stopped before account flow. Evidence: title: Workshop Cyanotype; date: 15 November 2026; time: 14:00–17:00; price: €89; access: Materials included; almost full / waitlist; booking asks account.

Next step: Use the cyanotype workshop page for the dated price and waitlist status; do not continue into account creation or booking.

### waag.org

[Guide](waag-org.md) · unavailable · difficulty: low · retested: no

The saved FabLab project page has a closed project duration ending 1 January 2025; the Open Wetlab page describes an ongoing research programme but no public drop-in calendar or target-window public session. This is source availability, not a prompt issue.

1. [web-extraction](https://www.waag.org/en/project/fablab-amsterdam/): Live page describes workshop formats but states project duration 30 Jun 2008–1 Jan 2025. Evidence: title: FabLab Amsterdam; date: Project duration: 2008-06-30 to 2025-01-01; access: No current public drop-in or dated session shown..
2. [web-extraction](https://www.waag.org/en/lab/open-wetlab/): Live Open Wetlab page describes annual BioHack Academy and research programme; no public drop-in calendar or current in-range session visible. Evidence: title: Open Wetlab; access: Research programme/annual academy described; no public open hours or individual target-window listing shown..

Next step: Wait for an individually dated public session or posted open hours; do not treat the legacy project page as current access.

### wijkconnect.com

[Guide](wijkconnect-com.md) · usable · difficulty: low · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Ordinary browser succeeded after web extraction error; detail provides recurrence/time/price but calendar confirms exact date.

1. [web-extraction](https://www.wijkconnect.com/amsterdam/organisaties/8345/huis-van-de-buurt-de-boomsspijker/agenda/26159/film-dineravond-buurtbewoners): Live page fetch failed in the web extraction tool. Evidence: No event/access fields extracted. Error: Web extraction returned internal error; ordinary browser rendered event page and calendar.
2. [desktop-browser](https://www.wijkconnect.com/amsterdam/organisaties/8345/huis-van-de-buurt-de-boomsspijker/agenda/26159/film-dineravond-buurtbewoners): Film & Dineravond; second Friday; €15.50; 20:00–22:00; guest-list email; calendar context includes 13 Nov 2026 Evidence: title: Film & Dineravond buurtbewoners; date: 13 November 2026 (calendar); time: 20:00–22:00; price: €15.50; access: Email guest-list signup.

Next step: Pair the November calendar date with the detail’s 20:00–22:00 time, €15.50 price and guest-list email.

### wildernisamsterdam.nl

[Guide](wildernisamsterdam-nl.md) · usable · difficulty: low · retested: no

Initial extraction returned title only; visible retry after declining optional cookies showed an English €78 Terrarium on 17 Nov, doors 18:45/start 19:00, plus a Kokedama listing with no stated start time.

1. [desktop-browser](https://wildernisamsterdam.nl/en/workshops/): Visible workshops body after choosing “Decline” showed Terrarium on 17 Nov (also 15 Dec), English, €78, doors 18:45/start 19:00, Bilderdijkstraat 165F. Kokedama Nov 24 €50 has walk-in 18:45–18:55 and duration 1.5h, without stated start. Evidence: title: Terrarium workshop; date: 17 November 2026; time: Doors 18:45; starts 19:00; price: €78; language: English; access: Bilderdijkstraat 165F.
2. [desktop-browser](https://wildernisamsterdam.nl/en/workshops/): Declined optional cookies using visible choice. Visible cards gave Terrarium date/time/price/language/location and Kokedama details; no registration performed. Evidence: title: Terrarium workshop; date: 17 November and 15 December 2026; time: Doors 18:45; starts 19:00; price: €78; language: English; access: Bilderdijkstraat 165F.

Next step: Use the Terrarium detail for exact start time; its listing is English at €78. Kokedama has a walk-in window but no explicit start time, so do not infer one.

### yagoy.nl

[Guide](yagoy-nl.md) · partial · difficulty: medium · retested: yes

Homepage extraction lists pass prices but hides class rows behind the schedule widget. A visible browser rendered the de Pijp weekly timetable; the displayed week was Oct 18–24 and only the Oct 18 sessions were inspected, so no later target-window occurrence is asserted.

1. [web-extraction](https://yagoy.nl/): Live homepage lists publicly readable class pass prices and studio information; class timetable not shown in extracted page. Evidence: price: Single €18; two classes €30; introductory one-month unlimited pass €50; access: Homepage links to studio schedules; price purchase link exists but not entered..
2. [desktop-browser](https://yagoy.nl/schedule-pijp/): Visible browser rendered week Sun 10/18–Sat 10/24; Sunday Oct 18 includes core & flow 09:00–10:15 and relax & flow 12:30–13:45, both displayed as closed/full. No later target-window occurrence captured. Evidence: title: core & flow; relax & flow; date: 2026-10-18; time: 09:00–10:15; 12:30–13:45; access: All levels indicated for some visible classes; displayed booking status closed..
3. [desktop-browser](https://yagoy.nl/schedule-pijp/): Retest after guide edit rendered the same weekly timetable and Oct 18 classes; requested-range stop rule remains necessary. Evidence: title: relax & flow; date: 2026-10-18; time: 12:30–13:45; access: All levels; booking status closed..

Next step: Only claim classes whose exact date is visible and whose displayed status is not closed/full.

### zumba.com

[Guide](zumba-com.md) · blocked · difficulty: high · retested: no

The original guide contained only a saved URL and generic recheck rules, without a short field-copy prompt or source-specific stop rule. Browser returned HTTP 403 Cloudflare “Just a moment” security verification; stop at challenge. Web extraction cache miss is not the security block.

1. [web-extraction](https://www.zumba.com/en-US/class_detail/index/04b0e2c6-7ecd-43a5-b923-aa234f5b09d8): Fetch failed with cache miss Evidence: No event/access fields extracted. Error: Web extraction cache miss.
2. [desktop-browser](https://www.zumba.com/en-US/class_detail/index/04b0e2c6-7ecd-43a5-b923-aa234f5b09d8): HTTP 403, Cloudflare security verification page; no class fields readable Evidence: No event/access fields extracted. Error: Cloudflare HTTP 403 security challenge.

Next step: The detail returned Cloudflare HTTP 403; stop at the challenge and keep the class unverified.
