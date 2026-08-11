# Opportunity Decision Ledger

This file is an **append-only public decision log**.

The purpose is to prevent hindsight rewriting.

Do not silently replace an old verdict with a new one. When evidence changes, add a new dated review event.

---

# Status Vocabulary

- `OPEN` — thesis is active; more evidence is required.
- `UPGRADED` — evidence improved enough to increase commitment.
- `DOWNGRADED` — evidence weakened; reduce commitment.
- `CONFIRMED` — key commercial assumptions have materially survived real-world tests.
- `KILLED` — a hard veto or decisive counter-signal broke the thesis.

Verdicts remain:

- `START`
- `BUY A REAL OPTION`
- `WATCH`
- `REJECT`

Status and verdict are different. A thesis can remain `OPEN` while moving from `WATCH` to `BUY A REAL OPTION`.

---

# Ledger Rules

1. Never delete an old decision because it became embarrassing.
2. Record the evidence that justified the decision **at the time**.
3. Separate observable fact from Opportunity Radar inference.
4. Record the strongest counter-thesis.
5. State what evidence would upgrade, downgrade or kill the thesis.
6. Do not backfill precise scores that were not actually calculated at the time.
7. If Evidence Coverage was not calculated, write `not yet measured`, not a fabricated percentage.
8. Future reviews append a new row/event; they do not rewrite the original event.

---

# Current Ledger

| ID | First seen | Opportunity | Geography | Stage | Initial verdict | Confidence | Evidence coverage | Status |
|---|---|---|---|---|---|---|---|---|
| OR-2026-08-01 | 2026-08-11 | Enterprise agent production deployment, governance & evaluation | Global / enterprise | S2–S3 | **BUY A REAL OPTION** | Medium-High | not yet measured | OPEN |
| OR-2026-08-02 | 2026-08-11 | Lightweight AI application services for manufacturing SMEs | China | S2–S3 | **BUY A REAL OPTION** | Medium-High | not yet measured | OPEN |
| OR-2026-08-03 | 2026-08-11 | Embodied-AI field deployment, training data & integration | China + global robotics | S2–S3 | **BUY A REAL OPTION** | Medium | not yet measured | OPEN |
| OR-2026-08-04 | 2026-08-11 | Cross-border compliance, localization & managed overseas operations | China outbound / global | S3 | **BUY A REAL OPTION** | Medium-High | not yet measured | OPEN |

Detailed theses: [2026-08 Radar](2026-08.md).

---

# Review Triggers

## OR-2026-08-01 — Enterprise agent production deployment

**Upgrade if:** recurring production contracts, repeatable governance/evaluation packages and measurable workflow ROI become visible.

**Downgrade if:** enterprise deployment remains mostly experimental or every project stays bespoke.

**Kill if:** platform vendors absorb nearly all governance/implementation value at negligible incremental cost.

## OR-2026-08-02 — Lightweight AI services for manufacturing SMEs

**Upgrade if:** repeated paid deployments appear in the same workflow/sub-industry and delivery hours fall with reuse.

**Downgrade if:** willingness to pay remains weak despite policy support or projects require heavy one-off integration.

**Kill if:** generic bundled software erases the service wedge or ROI cannot be measured.

## OR-2026-08-03 — Embodied-AI field deployment

**Upgrade if:** real multi-site commercial deployments, recurring operations revenue and measurable field ROI appear.

**Downgrade if:** activity remains demo/training-heavy without buyer budgets.

**Kill if:** hardware reliability, capital intensity or manufacturer vertical integration eliminates an accessible small-team position.

## OR-2026-08-04 — Cross-border managed operations

**Upgrade if:** recurring country/category-specific operating contracts and measurable risk/error reduction appear.

**Downgrade if:** the work remains one-off information consulting.

**Kill if:** liability, working-capital or regulatory complexity dominates achievable margin.

---

# Review Event Template

Append future events using this format:

```md
## YYYY-MM-DD — OR-XXXX — REVIEW

Previous verdict:
New verdict:
Status change:

New observable evidence:
- 

Counter-evidence:
- 

Evidence Coverage:
Confidence:
Weakest Link:
Opportunity Window:

Why the decision changed / did not change:

Next upgrade trigger:
Next downgrade trigger:
Kill criterion:
```

---

# Why This Matters

A framework that only explains winners after the fact can always look intelligent.

A ledger creates a harsher standard:

> **What did we believe before the outcome was known, why did we believe it, and did we update when reality disagreed?**