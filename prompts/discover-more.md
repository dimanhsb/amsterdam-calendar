# Amsterdam Open Week — master discovery prompt

## Current profile and reusable workflow

Ideas are browsed by activity and by provider. Keep `data/idea-catalog.json` in sync with new `data/ideas.json` records; use explicit saved activity/provider relationships and null for an unidentified provider. Read `source-guides/idea-catalog.md`. Potential providers do not establish current sessions, admission or beginner access.

Investigate city history, architecture, neighborhood, nature and themed walks. Distinguish genuinely free entry from tip-based/pay-what-you-want tours, donation entry and fixed per-person admission. A private group quotation is not a public single-person ticket price. Record mandatory booking/entrance fees separately. Verify spoken English/Dutch on the actual tour or session, never from webpage language. Use `languages: ["en"]` / `["nl"]` / both only when stated; otherwise `languages: []`. Where a provider offers separate language choices, retain `languageMode: "options"` and verify the chosen session. Mark `activityType: "walking-tour"` and use `price.type: "tip-based"` with null amount if no fixed fee is published but tipping is expected. Keep exact dates undated until individually verified.

Read `data/preferences.json` and `source-guides/README.md` first. Apply the current profile settings when relevant. Retain other times as searchable alternatives, never silently change a published time. The current coverage is 19 October–30 November 2026 inclusive; use a new explicitly requested window for later runs.

Use one source guide per website and small evidence batches. Record actual `researchMethod`, `researchRound`, `discoverySource` and explicit `ideaIds`; log unsuccessful routes too. Run `scripts/ingest.py` as a dry run, review evidence, then apply; regenerate the report and build/check. Start with cheaper models for straightforward extraction, escalate ambiguous access, prices or eligibility for review. Android Firefox is a public rendering fallback; no accounts, bookings, payments, contact or access-control bypass. Read `source-guides/REPORT.md` to prioritize sources by real dated/preferred yield. Historical seed ideas below are an archive and do not override this blacklist.


Act as my Amsterdam drop-in activity researcher and community scout. Browse current sources; save reusable evidence. Help me choose things I can actually do next week, and discover ideas outside the usual fitness/pottery lists.

## My context
I live near Waterlooplein. Nearby is preferable, but other Amsterdam neighborhoods are welcome. I travel between the Netherlands and Greece, so I cannot commit to weekly attendance or a sequential course. I want to meet people and gradually build a broader community. Gentle movement or dance is a plus, not a hard requirement. I already do Greek traditional dance; seek other, non-Greek communities. I declined rock and roll/jive. Salsa/bachata/merengue only qualify if a complete beginner can attend a standalone introduction plus social without a partner or prior lessons. Investigate Dutch traditional dances separately from pan-European Balfolk. Balfolk at Mezrab is a priority lead.

My age, budget, accessibility needs, languages beyond this conversation, transport and activity level have NOT been supplied. Do not infer them. Ask only if useful; proceed with varied options and clearly label language and intensity. Never infer age suitability from photos. Do not repeat health claims from the earlier AI list.

## Set the week explicitly
Use Europe/Amsterdam local time. State today's date, then define “next week” as the next Monday through Sunday. Do not silently substitute a rolling seven days. Allow an explicit requested date range. Account for daylight saving changes; store timestamps with the offset for each date. Never turn a recurring weekday into a confirmed occurrence without a dated listing or explicit organizer confirmation.

## Research and expand
1. Read the complete seed list below, `data/ideas.json`, existing research reports, and previously checked sources. Preserve failed/uncertain leads and corrections. Do not re-present them as verified.
2. Search in English AND Dutch. Useful terms: losse les, eenmalige workshop, inloop, open atelier, proefles, beginners, zonder partner, geen ervaring nodig, samen koken, buurttafel, wandelgroep, natuurwandeling, vrijwilliger een dag, bordspellenavond, repair café, volksdansen, balfolk, dansuitleg.
3. Explore beyond studios: neighborhood centers, OBA branches, community gardens, nature groups, food-rescue shifts, shared cooking, repair/textile cafes, board games, casual team sport, volunteering, singing and music jams, amateur astronomy, heritage/maker walks, museum making, and hands-on civic groups. Include free and low-cost options. Passive lectures can be a secondary choice; label them audience experiences.
4. Prioritize organizer event pages, official timetables and ticket pages. Use I amsterdam, UiT/Uitagenda, Meetup, Eventbrite, Hipsy, Amsterdam Alternative and social posts as discovery or corroboration. They may repeat stale information. Find the organizer and exact dated occurrence. Honor access rules; use public/authorized feeds and manual verification when no permitted API exists. Do not contact organizers, book, pay or subscribe on my behalf.
5. For each genuinely new idea explain why the format creates interaction, how someone can arrive alone, whether return attendance is optional, and what evidence is still missing. Aim for at least 15 new hypotheses across 5 categories before reducing to a shortlist. Suggest a concrete next search for each unverified lead.

## Return evidence, not an invented schedule
Produce 5–10 useful dated choices if the evidence supports them; do not pad. Also return an evergreen source catalog and an unverified idea backlog. For every event include:
- Stable ID; title; organizer; category; description; exact start/end (end may be unknown); IANA timezone; venue/address; neighborhood. Do not invent walking/cycling times. Use a map link or a sourced route estimate labeled as such.
- EUR minimum/maximum, whether free is explicit, mandatory fees/materials/rental/food, concessions if relevant, and a price evidence URL. Unknown price is null, never zero. “From” prices are not guaranteed totals.
- Event/organizer URL, booking URL, all corroborating URLs; source type; date retrieved; original event ID if supplied; short paraphrased field evidence; uncertainty/conflicts. Avoid extensive copying.
- One-session policy, beginner prerequisites, partner requirement, language, intensity/access details if stated. Distinguish visitor entry from a taught beginner session and course trial from a commitment-free event.
- Participation format: active collaboration, hosted mingling, parallel activity, audience, or unknown. Social fit is an editorial estimate, with a reason; it is not a promise of friendship.
- Booking method, availability as observed (or unknown), cancellation/refund information if found. A published listing does not establish spare places.
- Verification state: dated organizer evidence, dated listing corroborated with organizer, schedule-only lead, needs confirmation, canceled, or sold out. Keep rejected options and reasons.

Resolve conflicts field by field. An exact dated organizer exception overrides generic recurrence copy. Preserve both sources and why one wins. Deduplicate by organizer event ID/canonical URL first, then normalized title + venue + start time; keep the evidence from all sources. Never merge different ticket tiers or occurrences accidentally. Do not export uncertain recurring leads as calendar events. For exact dated events, export correct UTC instants or TZID with VTIMEZONE; do not fabricate an end time or use an all-day event when time is unknown.

## Rank and explain
Give 3 strongest picks with tradeoffs, then a compact week agenda. Rank flexible entry, active interaction, beginner/no-partner accessibility, closeness, transparent cost and evidence freshness. Avoid a precise numeric “social score.” Include one good fallback and make conflicts visible. Suggest a small experiment: one movement activity, one collaborative making session, and one recurring community you can revisit without obligation.

## Help the project improve
Return machine-readable event/source records matching the existing data files, a change log, stale records to revisit, source access/refresh notes, and the best next investigation questions. Propose RSS/ICS/JSON-LD/API sources only after checking they exist. Keep manual refresh separate from live automation. Never claim the site automatically updates unless a functioning ingestion job has actually been deployed. Later, explore preference feedback, travel/away mode, notifications, source health, cancellations, duplicate handling, field confidence, source terms, and a weekly digest. Suggest the smallest next implementation and acceptance checks.

## Full original seed list (unverified unless separately researched)
- CREA: Short workshops, arts, music jams. Caveat: Course catalog may require a full term; do not assume a five-minute walk.
- MK Ateliers / MK24: Drawing, painting, open studio. Caveat: Verify current identity, open access and individual-session bookings.
- Heart & Soul Pottery Studio: Wheel throwing, handbuilding tasters. Caveat: Check that each workshop is standalone and firing/collection terms.
- Art Ceramics Studio · Gillian Smith: Ceramics and glazing. Caveat: Check current workshop listings and actual address.
- The Clay Room Amsterdam: Handbuilding pottery. Caveat: Verify current studio, format and all-in price.
- AGA LAB: Screen printing, etching, risograph. Caveat: Open lab may require induction or prior technical skills.
- Volksuniversiteit Amsterdam: Lectures, photography, writing, conversation. Caveat: Many offers are courses; look specifically for one-session events.
- Amsterdam House of Arts & Crafts: Leather, paint pouring, screen printing, mosaics. Caveat: Verify public individual bookings and travel details.
- De Oude Kerk open studio: Drawing, acoustic jams, architecture sketching. Caveat: Specific open studio claim unverified; museum access is not a workshop.
- Studio Klei Amsterdam: Pottery tasters and decoration. Caveat: Exact venue, booking model and existence of these sessions need checking.
- De Lokatie Upcycling Lab: Textile repair and furniture upcycling. Caveat: A thrift shop is not evidence of an open workshop; verify lab claim.
- Waag Open Wetlab: Bio-art, DIY biology, biomaterials. Caveat: Historical lab name does not prove current public drop-in access.
- Fablab Amsterdam at Waag: Laser cutting, 3D printing, maker nights. Caveat: Check current operation, inductions and supervised access.
- Foam: Photography workshops and walks. Caveat: Check dates, level and whether exhibition admission is included.
- Upclub ROW & RIDE: Indoor rowing and cycling. Caveat: Verify current Weesperstraat venue and pay-per-session access.
- Vondelgym Oost: CrossFit, bag training, gymnastics. Caveat: Single tickets may have experience or membership conditions.
- Saints & Stars Oud-Zuid: Boxing, strength, reformer classes. Caveat: Check location-specific timetable and total single-session cost.
- Saints & Stars Oud-West: Bootcamp and strength classes. Caveat: Check current branch and one-off access.
- Het Gymlokaal West: Handstands, mobility, functional movement. Caveat: Verify beginner entry and one-off ticket.
- Kracht Amsterdam: Functional strength and CrossFit. Caveat: CrossFit visitor drop-in may require prior experience.
- Vondelgym West: Kickboxing, running and strength. Caveat: Distinguish club access from group class entitlement.
- Vondelgym Zuid: Functional workouts. Caveat: Verify class level and independent ticket.
- Eastbound Gym: Boxing and Muay Thai. Caveat: Equipment rental and beginner single-session access need checking.
- Tribe Jiu-Jitsu Amsterdam: BJJ fundamentals and open mats. Caveat: Open mat is often for experienced practitioners; check beginner instruction.
- Krav Maga Amsterdam: Self-defense. Caveat: Exact organizer and one-off beginner policy unverified.
- Parkour Discipline Studio: Parkour and freerunning. Caveat: Exact named venue and adult beginner availability unverified.
- Calisthenics Club Amsterdam: Bodyweight classes and handstands. Caveat: Identify exact organizer; avoid assuming advanced skills are beginner suitable.
- Padel Club Metropolitain: Beginner clinics and social play. Caveat: Check exact club and group-matching rather than court rental alone.
- Squash City: Squash and fitness. Caveat: Court rental requires a playing partner unless a social session is explicit.
- Boogieland: Boxing and conditioning. Caveat: Verify first-timer welcome, equipment and single ticket.
- Vos Gym Amsterdam: Kickboxing and bag training. Caveat: Check current location and beginner class requirements.
- Svaha Yoga: Yoga and tea afterwards. Caveat: Social tea and language claims require verification.
- Movements City: Hot yoga and Pilates. Caveat: Check exact address, heat level and single-class terms.
- Equal Yoga: Hot yoga and core workouts. Caveat: Verify beginner level and mat costs.
- Studio 191 Amsterdam: Barre, yoga and Pilates. Caveat: Check branch, equipment and one-off booking.
- Yagoy: Yin, restorative yoga and breathwork. Caveat: Verify current schedule and beginner suitability.
- Movements Vondelpark: Hot Pilates and Vinyasa. Caveat: Check single entry and heat/intensity details.
- Sound Bath Amsterdam: Gong and singing-bowl sessions. Caveat: Identify actual organizer; social contact may be limited.
- Wim Hof Method Experience Center: Breathwork and cold exposure. Caveat: Exact center unverified; do not repeat health benefit claims.
- Consciousness Club Amsterdam: Breathwork, meditation and tea. Caveat: Exact venue/location and current public program unverified.
- The Breathwork Movement Studio: Guided breathwork. Caveat: Verify exact business and format; no medical benefit claims.
- Klimmuur Amsterdam Centraal: Roped climbing and bouldering. Caveat: Roped climbing needs training/belay arrangements; day entry is not a social class.
- Beest Boulders het Lab Amsterdam: Bouldering. Caveat: Verify branch naming, entry and shoe hire.
- Beest Boulders Amsterdam: Bouldering. Caveat: Look for coached beginner sessions or hosted social nights.
- Beta Boulders Amsterdam: Bouldering and coworking. Caveat: Check the branch and address.
- Monk Bouldergym Amsterdam: Bouldering in Noord. Caveat: Check introductory session and hosted community activities.
- Balfolk at Mezrab / Balfolk Amsterdam: European folk social dance. Caveat: Verify dates, introductory workshops, and whether a partner is needed.
- Dutch traditional folk dance: Dutch regional dances. Caveat: Distinguish Dutch dances from pan-European Balfolk.
- Amsterdam Dance Center: Open ballet, hip-hop, contemporary, jazz, heels. Caveat: Open class may still require level-specific experience.
- Chassé Dance Studios: Afrohouse, street and commercial dance. Caveat: Check true beginner open classes, not sequential courses.
- Lucia Marthas Institute: Musical, pop/show and technique dance. Caveat: Adult public one-off entry not established by school existence.
- Salsa, bachata, merengue beginner socials: Intro plus social dancing. Caveat: Conditional interest only: must work as a first standalone visit with no partner.
- Rock and roll / jive: Social rock dancing. Caveat: User explicitly declined; retain as excluded, do not recommend.
- Fly Inverted Aerial Studio: Silks, hoop and aerial hammocks. Caveat: Exact studio and beginner single-session policy unverified.
- Pole Dance Factory Amsterdam: Pole, flexibility and chair dance. Caveat: Check branch, intro prerequisites and independent ticket.
- AcroYoga Amsterdam sessions: Partner balance and jams. Caveat: Jams may require experience; no-partner entry needs explicit confirmation.
- De Kookfabriek Amsterdam: Cooking workshops. Caveat: Private/corporate groups are not public individual bookings.
- Amsterdam Wine Academy: Wine tastings and food pairings. Caveat: Verify exact organizer and single evenings.
- Barista Company Academy: Coffee and latte art. Caveat: Verify exact venue, public booking and equipment inclusions.
- Baking Lab Amsterdam: Sourdough, fermentation and circular baking. Caveat: Check actual public workshop dates and take-home inclusions.
- Zuiderbad: Swimming and aqua fitness. Caveat: Lane swimming is lower interaction; classes need separate schedule checks.
- De Mirandabad: Swimming and aqua fitness. Caveat: Separate leisure entry, lap swim and instructed sessions.
- Noorderparkbad: Swimming and aquatic classes. Caveat: Check reservation and ticket type.
- Jaap Eden Ice Rink: Ice skating and technique lessons. Caveat: Seasonal: verify public sessions, rentals and independent beginner lessons.
- Canal SUP Amsterdam: SUP tours and SUP yoga. Caveat: Exact organizer and seasonal schedule unverified.
- Sloterpas Watersports Center: Sailing, windsurfing and kayaking. Caveat: Exact venue name and one-off taught sessions unverified.
- Watersportvereniging IJburg: Coastal rowing and paddling. Caveat: Club membership and beginner safety induction may apply.
- Boom Chicago: English improv tasters. Caveat: Check actual one-off classes rather than course enrollment.
- Muziekgebouw aan ’t IJ Sound Lab: Experimental instruments and sound. Caveat: Check adult individual tickets; some sessions may be family/group-only.
- BIMHUIS Workshop Stage: Jazz and rhythm workshops. Caveat: Audience masterclasses are not necessarily open playing sessions.
- Amsterdam Songwriting Guild: Songwriting feedback circles. Caveat: Exact organization and public drop-ins unverified.
- Pakhuis de Zwijger: Talks, workshops and civic discussions. Caveat: Verify language and active participation; a panel audience is lower interaction.
- Amsterdam Writing Workshops: Creative writing and feedback. Caveat: Exact organizer and one-session format unverified.
- Debate Club Amsterdam: Debate and public speaking. Caveat: Exact group near Roeterseiland and guest policy unverified.

## Additional directions from Astra (hypotheses to qualify)
- Balfolk social with the introductory workshop: Movement, repeated partner/group changes and a low-pressure way to participate immediately. Next check: Exact Oct25 evidence above. Prioritize. Confirm ticket availability; retain beginner arrival time separately from doors.
- A called ceilidh or contra-dance evening: A caller may teach each dance; social movement without a term of classes. Next check: Hypothesis. Find a current Amsterdam occurrence explicitly accepting beginners and solo visitors; do not substitute a Scottish dance course.
- International circle-dance afternoon: Group activity may feel familiar while broadening beyond Greek community. Next check: Hypothesis. Verify repertoire, mixed community, drop-in admission and whether instruction restarts each session.
- Beginner contact-improvisation workshop followed by a jam: Responsive movement and structured interaction. Next check: Hypothesis; lower priority until comfort with physical contact and movement level are known. A jam alone is not proof of beginner suitability.
- Facilitated body percussion or vocal improvisation: Making something together with no instrument to own. Next check: Hypothesis. Require a single-session offer and explicit novice access.
- Pop-up choir or single-evening singalong: Cooperation, shared achievement, little physical strain. Next check: Hypothesis. Exclude seasonal rehearsal groups unless the organizer explicitly permits independent attendance.
- Public karaoke with an identifiable host or newcomer night: Easy spontaneous option close to central Amsterdam; no technique progression. Next check: Public walk-in format supported by Sing Sing, Rembrandtplein 45. Hosted introductions, admission cost and next-week special programme unverified.
- Hosted board-game day: Small tables create sustained conversation and a shared task. Next check: Amsterdice explicitly welcomes beginners and joining other tables. Its observed next date was Oct18, outside the target week. Do not extrapolate Oct25.
- Beginner-friendly chess, backgammon or go social: One-to-one interaction, repeatable without a course. Next check: Hypothesis. Research a hosted matchmaking session rather than assuming a café with game boards welcomes solo joiners.
- A one-shot tabletop role-playing game: Introductions and collaborative storytelling are built in. Next check: Hypothesis. Verify one-shot rather than campaign, beginner seat, language, duration and preparation.
- Pub quiz with a solo-player joining policy: Conversation and teamwork without special equipment. Next check: Hypothesis. “Book a table” often presumes an existing team; require an organizer joining table or explicit team matching.
- Clothing-mending circle or repair café: A concrete project makes conversation easier. Next check: Repair Café Amsterdam's De Steek listing supports clothing repair on Mondays, 16:00–20:00. It displays an older next-date label; confirm current occurrence and whether visitors repair together or await a service.
- Shared craft table: visible mending, embroidery or crochet: Slower pace with room to talk. Next check: De Steek supports craft offers, but several highlighted products are private group bookings or courses. Public single-seat workshop remains unverified.
- Cooperative bike-repair workshop: Practical skill and light movement with natural questions. Next check: Hypothesis. Amsterdam repair calendar lists ABC Community bike repair; distinguish public service from a participatory workshop and check skills/tools policy.
- Volunteer cooking or food-rescue shift: Side-by-side work is likely to produce real conversation. Next check: One-day volunteering supported by Serve the City. Dated Noord leads above; check shift length, physical work and onboarding.
- Neighbourhood dinner with a cooking/helping role: Shared task plus shared table, potentially repeatable after travel. Next check: SOOZ Helpend Handje explicitly allows one-off help, including cooking. No dated opening verified. A request to contact staff is not a bookable calendar event.
- Community garden work morning: Light movement and recurring faces without sequential lessons. Next check: Hypothesis. Search flexible green volunteering, then verify one-off participation, tools, physical demands and weather cancellation.
- Group park or canal-side cleanup: A clear common task; walking pace rather than workout. Next check: Hypothesis. Require a dated organizer listing, start point and group format; solo litter picking does not satisfy the social aim.
- Guided tree, bird or fungi walk: Small-group movement with frequent conversation prompts. Next check: IVN public excursions supports regular public nature outings. Exact Beatrixpark event above. Language and participant mix unknown.
- Citizen-science observation session: Shared discovery makes introductions easier. Next check: Hypothesis. Look for one-off bird counts, water testing or urban biodiversity events; separate training-required projects.
- Urban sketch walk with an end-of-session sharing circle: Walking plus an easy topic for conversation. Next check: Hypothesis. Verify social sharing/coffee, beginner welcome and independent attendance; silent drawing alone scores lower.
- Photo walk with paired exercises or critique: Modest movement and a reason to interact. Next check: Hypothesis. Require a public single-seat session; exclude private tours and professional equipment prerequisites unless clearly acceptable.
- Bookbinding, zine-making or printmaking taster: Small groups and tangible shared materials. Next check: Hypothesis. Require one-session completion and materials-inclusive price; studio open hours do not imply instruction.
- A facilitated reading group using a short text provided there: Shared discussion without weeks of homework. Next check: Hypothesis. Distinguish this from a traditional book club requiring advance reading or membership.
- Philosophical conversation or structured discussion salon: More reliable interaction than listening to a lecture. Next check: Hypothesis. Look for small-group dialogue, language and a newcomer joining policy; Q&A alone does not count as strong interaction.
- Social table tennis, pétanque or casual doubles session: Movement with natural turn-taking and low equipment burden. Next check: Hypothesis. Confirm equipment, matchmaking, level and single-session payment; free public facilities alone are not organized events.
## Deeper browser research — 18 October 2026

Keep researching both the original ideas and new directions. The calendar covers 19 October–30 November2026. This remains a dated research snapshot, not a live booking feed. Use browser inspection of public organizer calendars and follow event cards into exact details and ticket selectors. Navigate to November explicitly; record which dates the booking window actually exposes. Do not extrapolate a weekly recurrence into unpublished sessions.

Investigate ClassPass as a discovery and booking channel, then cross-check the studio’s own schedule, exact branch, class level and direct single-visit price. Public ClassPass pages returned Cloudflare403 during this pass. Record access limits; do not bypass blocks or start a trial. Credits depend on the session/account and must remain separate from euro prices. Never convert credits into a fabricated cash equivalent. A two- or three-class intro package is not a standard single-class price. Keep verified undated offers in Drop-in options, outside the dated calendar and ICS.

For every price, distinguish the standard adult single visit from concessions, first-timer trials, bundles, membership rates and optional support tiers. Include compulsory booking fees; list equipment rental, first-registration charges, materials, firing/collection costs and required cards separately. Check whether first-visit registration is already included before adding it twice. Donation entry is a separate policy from free admission and an unknown price. Prefer a ticket selector’s total over older fee-excluding body text, documenting the difference.

Distinguish Basic/absolute novice, Beginners/some experience and Open level. Check physical contact, heat, vigorous movement, instrument/skill requirements and reading/preparation. Keep unknown age/language/ability explicit. A group yoga class does not prove introductions; assess the social mechanism in plain language. Prioritize shared tasks, rotating partners, facilitated discussion, hosted games and time to stay afterwards.

Deduplicate by organizer, venue, local date/time and actual activity, preserving saved event IDs. Follow booking links read-only to check sold-out and waitlist labels without registering, booking or contacting anyone. Conflicting dates, workshop identity or availability need explicit flags and export exclusion. Preserve source URLs, checkedAt and which fields each source establishes; make browser blocks and extracted-page evidence visible. Calendar times use Europe/Amsterdam: clocks change25October2026; preserve local wall time with the correct offset.

Use Luna for independent source research and Astra for an adversarial evidence/fit audit. Keep a machine-readable batch of events,sources,offers,priceUpdates and ideaReviews. Maintain all original ideas and preferences, including declined rock/jive; add new directions without inflating confirmed-event counts. Next research should increase breadth, not just more occurrences of the same venue.

### Six further directions from Astra

- Dutch conversation café at SOB: Organizer welcomes non-students and allows walk-in attendance for Amsterdam residents/workers; usual Fridays17:00–18:30, excluding school holidays. Exact target dates and fee need confirmation. Conditional on wanting Dutch practice. Source: https://www.sobamsterdam.nl/taalcafe/
- Public telescope observing and astronomy outreach: Exact UvA October24 event is free but fully booked. VSA lists November20 19:00–22:00 at SciencePark904; registration availability,fee and language unconfirmed. Seek small-group tours or shared observing. Source: https://www.volkssterrenwachtamsterdam.nl/index.php/outreach
- Public-speaking guest meeting with impromptu speaking: Amsterdam Toastmasters supports free guests; confirm exact current venue and date,English delivery,guest limits and whether impromptu participation is optional. Other club pages have conflicting addresses; do not transfer them. Source: https://www.toastmasters.org/Find-a-Club/00009210-00009210
- Ground juggling / object-manipulation taster: Current CircusLab open training is self-guided,from€5,without formal lessons or supervision. Find an instructed novice workshop rather than treating unsupervised aerial/open training as suitable. Source: https://www.circuslab.amsterdam/open-training
- Beginner orienteering with a partner and debrief: OLV MINOR welcomes walkers and all levels; no convenient exact target occurrence established. Ask about pairs,beginner briefing,equipment and a social debrief. Source: https://www.olvminor.nl/
- Parkrun walking or volunteering followed by coffee: AmsterdamseBos official page was blocked; current meeting point,cancellations,coffee and one-off volunteer openings need official confirmation. Do not manufacture weekly Saturday entries. Source: https://www.parkrun.co.nl/amsterdamsebos/
## Organisers and formats from the additional-listings research

Use these alongside all original seeds and Astra directions. The library retains the original100 ideas and subsequent additions. A researched format is not a promise of current ticket availability.

- Station West · one-session art and music workshops: Guided drawing,painting,collage and beginner percussion. Select an individual session ticket. Exclude multi-session courses and pair-only portrait tickets. English support varies by topic; confirm the exact session. Source: https://station-west.amsterdam/creatieve-workshops-in-amsterdam/
- ClubCuisine · public single-seat cooking: Open-registration cooking workshops for individual participants. VerifiedNovember2,3 and7 sessions are€95. Reopen the actual month and dated ticket; older indexed inventory can disagree with the live calendar. Source: https://clubcuisine.nl/events/
- Stretch & Fold · craft and food workshops: Weaving,fermentation and painting sessions. Choose a one-event ticket. Check ingredients,materials and collection requirements; do not transfer one workshop’s fee or inclusions to another. Source: https://www.stretchandfold.nl/events
- The Art Café · Waterlooplein workshops: Small creative workshops at Waterlooplein6F. Close to the user’s preferred area. ExactOctober/November dates are published; two prices remain unknown. Confirm price and model-painting format before booking. Source: https://www.theartcafe.nl/nl/workshops
- Smaak & Cultuur · one-day sourdough: Hands-on bread making in a standalone workshop. November20 costs€75. Prepare a starter in the preceding week. Dutch delivery; English if the group wishes. Confirm the showroom’s meeting details. Source: https://www.smaakcultuur.nl/workshop-zuurdesembrood
- Dam Hoops · independent hoopdance workshop: Beginner and improver hoopdance in a small group. November20 is€15.80 at DeSchakel. No waist-hooping ability required; confirm available loan equipment and capacity. Source: https://hipsy.eu/event/256765-hoopdance-workshop
- Moving Sparkles · single 5Rhythms session: Guided warm-up and free-form movement without fixed steps. Choose an individually listed NDSM or Friday session; no consecutive attendance required. Single-session prices differ by venue; language and exact Friday address need confirmation. Source: https://hipsy.nl/event/242346-5rhythms-amsterdam-noord-an-ecstatic-experience
- Common Ground · Resonance Movement Practice: Expressive movement exercises with tea and time together. A separate single-session ticket is explicitly available alongside the course. Standard€20.80; concessions and packages are separate. Source: https://hipsy.nl/event/252724-resonance-movement-practice
- Common Ground · listening and NVC workshops: Facilitated listening,dialogue and connection exercises. Reserve one evening. Donation-based participation may have a Free reservation card. Arrive before the18:50 door cutoff; do not treat the reservation label as the final cost. Source: https://hipsy.nl/event/254141-nvc-and-authentic-relating-playground
- Kaap · independent ecstatic dance evening: Free-form movement with an opening and time together afterwards. Regular ticket€23.30 for the verified dates. Early tiers are conditional. Conversation is outside the talk-free dance floor; arrive for the opening. Source: https://hipsy.nl/event/250704-ecstatic-dance-kaap-dj-rachi
- Oostenburg Board Game Club: Hosted board games with solo and beginner access. VerifiedNovember4,19:30–22:00,free entry. Recheck the next actual hosted date rather than inferring a monthly recurrence. Source: https://overdebrug-oostenburg.nl/agenda/board-game-club-3/
- Buurtteam · Amstelpark group nature walk: Guided walking with shared reflection in a small group. Signup via gezond@buurtteamamsterdamzuid.nl; maximum12. Fee,age eligibility and spoken language remain unconfirmed. Confirm the entrance meeting point. Source: https://www.buurtteamamsterdam.nl/serie/groepswandeling-in-de-natuur-amstelpark/
- De Rooij · one-day beginner photography: A standalone photography day using your own camera. November21 is fully booked with a waiting list. Keep as a future-format lead; do not substitute the calendar’s defaultDecember5 date into this November calendar. Source: https://www.derooijfotografie.nl/fotocursus/fotografie-cursus-amsterdam/
- Studio Koekoek: Embroidery, Sashiko and visible mending workshops near Waterlooplein. Check the exact workshop level, date, total fee and remaining seats. Source: https://studio-koekoek.com/product-category/workshops/workshops-with-seats/
- Atelier Kleie: Handbuilding workshops with independent single-session reservations. Check the exact workshop level, date, total fee and remaining seats. Source: https://atelierkleie.wordpress.com/workshops/

For inaccessible sources, ask the installed Hermes local agent to use ordinary Android Firefox where available. Require actual visible-browser evidence, an exact date/time and an honest record of what did or did not load. Verify emulator boot before treating setup as research; preserve other devices/services and clean up task-owned disposable resources. Stop at login,verification,rate-limit or denial gates. Never infer an Android success from an APK download or a healthy container. Keep unsuccessful attempts as gaps, outside the dated event count. Follow-up on 18 October 2026: ordinary Android Firefox successfully loaded the public ClassPass EQUAL Rozengracht page and AHAC’s public Open Atelier product page. No ClassPass sessions/credits or individual AHAC slots were verified in the inspected views. AHAC displayed a starting price of €59; retain that qualifier. Continue from the public product calendar at https://booking.leisureking.eu/bm/ab3fc530c18df81c3718b7129276caac/assortiment/88905?lang=NL and inspect its individual day/time rows before proposing occurrences. Heart & Soul and Koekoek remain open research gaps.

When expanding the calendar, save the existing dated-ID baseline and count newly dated usable occurrences after source and identity deduplication. Different organizer accounts may cross-list the same event. Compare venue,performer,date and actual programme time; count one occurrence while retaining both sources. A promoted old lead counts only once as newly dated. Exclude sold-out,waitlist,cancelled and availability-conflict entries from the usable-new claim. Check booking links against the event date: the cheapest/default calendar selection may be outside the requested range.
