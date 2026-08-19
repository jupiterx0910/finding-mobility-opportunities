---
name: finding-mobility-opportunities
description: Evidence-driven opportunity discovery for startup ideas, emerging industries, career-to-founder transitions and small-team ownership paths. Finds what a specific operator can enter, validate and turn into owned capital.
metadata:
  author: jupiterx0910
  version: "8.2.0"
---

# Opportunity Radar Agent Skill

Use the repository root `SKILL.md` as the canonical operating procedure. This file is a portable skill package entrypoint for agent environments that discover skills under `skills/<name>/SKILL.md`.

## Required behavior

Follow this causal chain:

`Need → Change → Career-to-Founder Fit → Signals → Payment → Industry Formation → Capital Heat → Economic Quality → Power → Operator Fit → Evidence Confidence → Why-Not-Yet → Window → Paid Pilot → Recurrence → Assetization → Real Option → Decision Ledger`

Always:

- distinguish fact, inference and hypothesis;
- state geography and as-of date for current analysis;
- separate User / Beneficiary / Buyer / Payer;
- treat VC/angel/strategic funding as a capital signal, **not** customer proof;
- report Capital Heat separately as `C0 Cold / C1 Emerging / C2 Building / C3 Hot / C4 Euphoric / C5 Unwinding`;
- report Signal Score, Mobility Score, Evidence Coverage and Confidence separately;
- actively search for the strongest hostile explanation;
- require a 30–60 day paid test before large commitment when feasible;
- define leading, confirmation and kill criteria;
- identify the Power Pool and an assetization path;
- preserve dated decisions rather than rewriting history;
- use failure / false-positive backtests when the category is hype-sensitive.

## Public artifact rule

For public README, examples, datasets, benchmarks or demos, use synthetic / fictional operator archetypes only. Never expose private user context or infer personal facts into a public artifact.

## Reference loading

Load only what the task needs:

- `references/capital-heat-lens.md` for VC / angel / strategic capital;
- `references/evidence-confidence.md` for evidence coverage and confidence;
- `references/window-and-why-not-yet.md` for timing and hostile explanations;
- `references/career-to-founder-transition.md` for employment-to-ownership mobility;
- `cases/failure-backtests/` for historical false positives;
- `references/output-template.md` for the final output structure.

## Verdicts

Return exactly one primary verdict:

`START | BUY A REAL OPTION | WATCH | REJECT`

Never interpret a score as a probability of success.
