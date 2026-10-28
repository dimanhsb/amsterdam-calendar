# Maintain activity and provider browsing

The Ideas page groups the saved records in two directions. `data/ideas.json` remains the research-note archive with stable IDs. `data/idea-catalog.json` has three arrays:

- `activities`: stable `id`, plain `name`, subject `category`, optional `description`.
- `providers`: stable `id`, actual provider/organizer name, a `url` already saved in source evidence or null, and optional `notes`/`aliases`.
- `links`: one explicit `{ideaId, activityId, providerId}` relationship; use `providerId: null` when a provider is not identified.

Use exact saved descriptions and research notes. Do not infer activity links from partial substrings: pottery wheel throwing is unrelated to rowing, upcycling is unrelated to indoor cycling, and an improver dance session is unrelated to improv comedy. Generic indexes, ticket platforms, addresses and activity names are not providers. Merge actual aliases and venue room names; keep distinct branches or unresolved identities separate. Studio Klei Amsterdam remains unresolved and must not borrow Atelier Kleie's URL.

Relationships are potential leads. A provider's shared research note does not prove every class is dated, open to solo visitors or beginner suitable. Preserve the original qualification in `ideas.json`; do not manufacture event counts from a shared domain or source index. Concerts and dance floors do not establish taught workshops/classes. Keep body percussion distinct from instrument drumming, Pilates distinct from barre, and conditional English support distinct from confirmed English delivery.

When adding a research idea, add at least one link. The app temporarily keeps unclassified future ideas visible, but the release check requires all current ideas to be mapped. Known activities without providers appear under “Provider not yet identified.” Search uses activity/provider/idea names, avoiding historical rejected comparisons in long notes.

Run `python3 scripts/build.py` and `node scripts/check.mjs`. Review both views, a cross-link, search/category changes, keyboard focus and the default blacklist on mobile before publishing. No new web claims are created by catalog grouping; fresh source research follows the relevant website guide.
