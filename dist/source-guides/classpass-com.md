# ClassPass — dated schedules via Android Firefox

Refreshed 21 October 2026. Hermes local successfully rendered public dated schedules in normal Android Firefox for EQUAL Rozengracht, Upclub ROW & RIDE and Studio 191 Oost. ClassPass credit amounts remain unknown: controls say “See pricing”. Earlier desktop security-verification failures are historical observations of that client, not a finding that all public schedules are unavailable.

## Luna quick start · working Android route

1. Ask Hermes local to follow the Android research skill using the approved disposable setup: container at most 4 GiB, guest 2 GiB, loopback-only ports. Preserve existing services. Firefox Terms acceptance is already approved with optional diagnostics and crash reports off. Do not use a physical phone.
2. Open one exact public branch link below. Confirm its address. Dismiss optional cookies and ordinary browser hints if needed. Scroll below Info: the dated schedule can be three substantial scrolls down. An initial trial banner does not mean the schedule is absent.
3. Read the visible day/date header. Use the visible next-day arrow or “See next day” control for each actual date in {start_date}–{end_date}; scroll through its rows and capture screenshot plus accessibility XML. Sticky headers can hide the first row: adjust the viewport and capture it separately. XML rows may extend beyond the screenshot crop; label that evidence honestly.
4. Record each displayed title, date, start, duration/end and instructor if present. Do not infer unseen rows, repeat a weekly timetable, or treat partial day coverage as complete. Apply Amsterdam DST offsets (25 October 2026 changes to +01:00).
5. “See pricing”, “Join ClassPass” and trial adverts establish neither credit price nor remaining places. Keep both unknown. Stop at a security/login/transaction gate; no private APIs or account actions.
6. Match exact branch + start + class against canonical events before ingestion. Enrich duplicates with this evidence. Check official organizer pages separately for single-class EUR prices and mandatory extras; never convert credits to euros. A special ADE class does not automatically inherit an ordinary class-card price.
7. Save evidence, report actual route and yields, then remove only the task-owned emulator resources. Parent reviews and ingests; Hermes does not publish.

Working captures and independent review: `research/round9/`. Android evidence files are retained locally under `/tmp/hermes-round9-evidence/`; they are temporary, so retain the reviewed structured observations in the repository.

## Branch links — first three verified this round; others are leads

- [Upclub ROW & RIDE](https://classpass.com/studios/upclub-row-and-ride-amsterdam) — Weesperstraat 69; convenient to Waterlooplein.
- [EQUAL Rozengracht](https://classpass.com/studios/equal-rozengracht-amsterdam).
- [Studio191 Oost](https://classpass.com/studios/studio-191-oost-amsterdam).
- [Movements City](https://classpass.com/studios/movements-city-amsterdam).
- [Yagoy Pijp — correct branch](https://classpass.com/studios/yagoy-pijp-amsterdam) — Karel du Jardinstraat 33-1. The earlier saved de Pijp offer incorrectly linked West; corrected this round. Direct EUR price evidence is older and was not refreshed by fixing the branch link.
- [Svaha Downtown](https://classpass.com/studios/svaha-yoga-downtown-amsterdam).

Other researched leads: [Chassé](https://classpass.com/studios/chasse-dance-studios-amsterdam), [Zhembrovskyy de Pijp](https://classpass.com/studios/zhembrovskyy-de-pijp-amsterdam), [Salsa te Gusta Zeeburgerpad](https://classpass.com/studios/salsa-te-gusta-zeeburgerpad-amsterdam). Their profile alone does not prove standalone access or an upcoming date.

## Prices and access conditions

Ordinary direct single visits were independently checked at EQUAL (€20; towel bring-own or €2.50 rental) and Upclub (€19, two-week pass validity). These are organizer products, not ClassPass credit quotes. Exact spoken delivery language and remaining inventory need separate evidence. Studio 191 prices must distinguish mat classes from Reformer.

## Copyable prompt

“Ask Hermes local to use normal Android Firefox in the approved disposable emulator and inspect {studio_profile_url} for {start_date}–{end_date}. Confirm the branch address. Scroll below Info to find the actual dated schedule, then use visible next-day controls. Return individually observed title/date/start/duration/instructor rows with screenshots and XML. Handle sticky headers and distinguish screenshot-visible from accessibility-tree rows. Keep unshown credits, language and places unknown. Match duplicates before adding. Obtain any direct EUR price separately from the official organizer and identify mandatory extras and special-class exceptions. Do not infer recurrence, convert credits, sign in, create an account, start a trial, book or pay. Stop at security/account gates. Save a sanitized report and clean up only task-owned emulator resources.”

## Historical access observations

Round 8 desktop Chromium hit security verification on five profiles and indexed extraction showed past schedules. That client stopped at the gate. Round 9's user-requested normal Android Firefox attempt encountered no such gate on the three successful profiles above. Neither result guarantees future access: document what the current client actually displays. See `research/round8/classpass-findings.json` for the older observations.
