# Opportunity Radar Website MVP

This directory contains a static, responsive research interface for the Opportunity Radar project.

## Preview locally

Run from the repository root:

```bash
python -m http.server 8000
```

Open <http://localhost:8000/site/>.

Do not open `index.html` through a `file://` URL: the interface fetches the shared research snapshot from `../radar/opportunities.json`.

## What works in this MVP

- Responsive Chinese-language landing page;
- opportunity cards loaded from the repository's JSON snapshot;
- keyword search and sector/verdict filters;
- detail panel for payer hypotheses, potential profit-capture points, operator archetypes and suggested validation actions;
- visible snapshot date and stale-data warning;
- links back to the repository's research files.

## What does not exist yet

- no database;
- no live source collection;
- no AI-generated candidate pipeline;
- no automatic scoring or publishing;
- no authentication, user accounts or notifications;
- no production deployment has been verified.

The displayed opportunity data is a research snapshot, not a statement that the opportunities are currently validated.

## GitHub Pages

The site can be published as a static prototype if the repository's Pages settings are configured to serve the repository root and the public URL is verified. Because this interface loads `../radar/opportunities.json`, keep `site/` and `radar/` at the same repository level. Do not claim it is live until the deployed URL has been checked in a browser.

## Next engineering step

Build the first ingestion pipeline for a small set of stable, public, permitted sources. Store each source and signal with timestamps, deduplication keys, source URLs and validation status. Initially automate **signal collection only**; keep opportunity conclusions behind evidence checks and a review gate.
