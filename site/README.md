# Opportunity Radar Website MVP

This directory contains a static, responsive research interface for the Opportunity Radar project.

## Preview locally

Run from the repository root:

```bash
python -m http.server 8000
```

Open <http://localhost:8000/site/>.

Do not open `index.html` through a `file://` URL. For local preview, the interface tries `./radar/` and then `../radar/`; the Pages build copies the data snapshots to `public/radar/`.

## What works in this MVP

- Responsive Chinese-language landing page;
- opportunity cards loaded from the repository's JSON snapshot;
- keyword search and sector/verdict filters;
- detail panel for payer hypotheses, potential profit-capture points, operator archetypes and suggested validation actions;
- visible snapshot date and stale-data warning;
- links back to the repository's research files.

## What does not exist yet

- no database;
- no database or account system;\n- public signal collection is implemented in `scripts/collect_signals.py` and scheduled by `.github/workflows/collect-signals.yml`; first-run success must be checked in Actions;
- no AI-generated candidate pipeline;
- no automatic scoring or publishing;
- no authentication, user accounts or notifications;
- no production deployment has been verified.

The displayed opportunity data is a research snapshot, not a statement that the opportunities are currently validated.

## GitHub Pages

The `.github/workflows/deploy-site.yml` workflow assembles `site/` at the Pages root and copies the opportunity, signal and collection-report JSON snapshots into `/radar/`. It uses GitHub Pages Actions deployment. Do not claim the site is live until the deployment workflow succeeds and the resulting URL has been checked in a browser.

## Next engineering step

Next, verify the first scheduled collection run and Pages deployment. Review source failures and signal quality before expanding the source registry. Keep opportunity conclusions behind evidence checks and a review gate.
