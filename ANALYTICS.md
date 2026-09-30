# Traffic measurement operations

Status: prepared, disabled pending GoatCounter account creation. No historical website traffic is recoverable from this integration.

1. Create the hosted GoatCounter account for this workshop; use site domain `impartshadow.github.io/workshop`. The human-verification signup must be completed by the account owner. No paid plan is required at current small-site usage.
2. Set the `workshop-analytics` meta tag in `index.html` to the account's `https://ACCOUNT.goatcounter.com/count` endpoint. This public endpoint is not a secret. Keep dashboard access private. Set provider collection options conservatively.
3. Update the status in `PRIVACY.md` and this file. Run the browser checks, commit and push. Verify deployed assets before making a test visit.
4. Make one labeled operator test visit and trigger download, project-room and successful copy events. Inspect the receiving dashboard to confirm the named events arrived. Record the test window separately; do not report it as recruitment. Then use `?analytics=off` for subsequent operator checks.
5. At each recruitment review, report the measurement start date, page views/estimated visitors, source domains/campaigns and named event totals. Compare with actual outside contributions and peer replies from project rooms; do not infer individual conversion from aggregate counts. Export the dashboard data for the review. If collection fails or is unavailable, say unknown rather than zero.

Event definitions: `view-projects` is an in-page navigation click; `room-*` and `welcome-room` are departures toward GitHub; `download-*` are download clicks; `copy-prompt` requires clipboard success; `start-project` and `start-contribution` are clicks to forms. None proves task completion.

Use only the allowlisted `utm_source` values when sharing links. Early traffic cannot separate bots, maintainers and prospective participants perfectly. Do not use these counts alone to decide that a question has no appeal.

References: https://www.goatcounter.com/help/start · https://www.goatcounter.com/help/js · https://www.goatcounter.com/help/events
