# Interactive Opportunity Radar

A static, no-backend demo of the Opportunity Radar decision logic.

## What it does

The demo asks for operator-side inputs — career archetype, payer access, supplier/channel access, affordable loss, paid-pilot feasibility and time — then adds the v8.3 capital/customer falsification layer:

`Capital Heat × Payment × Retention × Contribution Economics`

It returns:

- heuristic Career→Founder transition readiness;
- payer proximity;
- Hype Divergence state;
- window pressure;
- best first wedge;
- anti-hype warning;
- first paid test;
- assetization path;
- a single verdict: START / BUY A REAL OPTION / WATCH / REJECT.

It also reads the repository's machine-readable `radar/opportunities.json` when served over HTTP.

## Important limits

This is a **decision aid**, not a prediction engine.

- Readiness is heuristic, not a startup-success probability.
- It does not perform live market research.
- Capital Heat is not an attractiveness bonus.
- A public demo must never use private user context.
- Current-market conclusions still require the full Skill workflow and dated evidence.

## Run locally

From the repository root:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/demo/
```

## GitHub Pages

The demo is intentionally static and Pages-compatible. Repository Pages still needs to be enabled separately in GitHub settings if you want a public URL.
