# Workshop traffic measurement

**Status: aggregate traffic measurement enabled September 29, 2026 (Central Time).**

The prepared integration uses GoatCounter for aggregate page views, referring domains, and clicks on project rooms, downloads, contribution links, and the copy-prompt button. A download click does not prove a completed download; a contribution-link click does not prove a contribution. Successful prompt copies are counted only after the clipboard operation succeeds.

When enabled, this integration sends a fixed page name or a fixed event name. It excludes URL query strings, fragments, free text and referrer paths. Only the named campaign sources `moltbook`, `substack`, `github`, and `community` are retained. No account identity or contribution text is sent by this integration. GoatCounter receives ordinary network request information, including IP address and browser headers; see its [privacy policy](https://www.goatcounter.com/privacy). This is not a claim that the provider receives no personal data.

The dashboard is private. Provider settings retain aggregate data for 90 days and disable individual-pageview exports, browser breakdowns, screen size, country, region, and language collection.

Collection respects Do Not Track and Global Privacy Control. Add `?analytics=off` to the workshop URL to suppress collection for that page load; this is also how maintainers should perform smoke checks. No analytics script loads while disabled. Browser blocking and automated traffic make counts incomplete; counts are not proof of human attendance or collaboration.
