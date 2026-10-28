# On-demand refresh

Run `python3 scripts/refresh.py` from the project directory. The default range is today through 27 days later in Amsterdam. Use `--start-date YYYY-MM-DD --end-date YYYY-MM-DD`, repeat `--source SOURCE-ID` to restrict sources, or use `--preview` to collect without rebuilding the local site. A preview still saves source snapshots and run reports locally.

The command respects the collector's robots, rate-limit and backoff rules and saves raw pages under `.collector-cache/runs/`. It records up to 20 recent refreshes in the Collection status page on the next build and creates a local `model-queue.json` with up to 20 candidate leads (`--luna-limit` changes this). `--terra-limit` records the agreed escalation budget, default 2.

**Current limitations:** the command cannot start Luna or Terra in the standalone environment and does not import, update or publish events. The queue is unreviewed; venue, date, participation and other facts still require verification. The script records these steps as unavailable/not attempted, rather than claiming success. The private ChatGPT Site requires the authenticated Sites workflow to publish the resulting build. Historical events and source evidence are preserved; the build excludes events whose dates are past. No automatic cleanup is implemented.

A failed or deferred source does not erase older data. A nonzero exit code signals partial collection or build failure; inspect `data/refresh-runs.json` and `.collector-cache/runs/<run-id>/run.json` for details. Raw HTML and the local review queue are not published.
