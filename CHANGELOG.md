# Changelog

## v8.1 — Opportunity Intelligence System

### Added

- `Evidence Coverage & Confidence` layer so opportunity scores cannot masquerade as probabilities.
- Evidence-quality grades and a four-number readout: Signal Score, Mobility Score, Evidence Coverage and Confidence.
- `Career → Founder Transition Map 2026` covering more than twenty occupational archetypes with a transition-readiness rubric.
- `Why-Not-Yet Test` to force the strongest benign and hostile explanation for why an opportunity remains unsolved.
- `Opportunity Window / Half-Life` lifecycle: Opening → Expanding → Crowding → Consolidating → Closed to generalists.
- Append-only `Opportunity Decision Ledger` with upgrade / downgrade / confirm / kill review events.
- Machine-readable `radar/opportunities.json` snapshot.
- New behavioral pressure tests for low evidence coverage, hostile economics, closing windows, decision-ledger updates, transition-readiness vs upside, and technical skill without payer access.

### Changed

- `SKILL.md` now requires Evidence Coverage, Confidence, Key Unknowns, Why-Not-Yet and Opportunity Window before the final verdict.
- Scorecards now explicitly state `score ≠ probability` and use confidence-adjusted action sizing.
- Output template now separates evidence strength from opportunity attractiveness and adds timing/window analysis.
- README positioning now emphasizes an auditable decision system rather than a static opportunity framework.
- Current Radar judgments are preserved in a public ledger rather than silently rewritten later.

## v8.0 — Clean Rebuild / Career-to-Founder Release

### Added

- Clean repository rebuild with no inherited Git history.
- `Career-to-Founder Transition Lens` as a first-class analytical layer.
- Six synthetic career-founder examples focused on roles with low transition friction.
- Explicit public-example privacy rule: no private user context, profile data or inferred personal history may be used in public examples.
- Updated dual scorecards with career-transition quality and Power Pool access.
- Historical backtests for ecommerce, mobile apps, creator economy, e-cigarettes and AI-native services.
- August 2026 Opportunity Radar with dated primary sources.
- Three-book entrepreneurship reading path.
- Validator and scenario tests.

### Changed

- Representative founder examples prioritize **B2B sales, cross-border operations, industrial technicians, procurement/supply chain, domain operator + AI, and growth/commercialization** rather than treating corporate seniority as the default founder profile.
- Core formula updated to emphasize `career edge` and transition friction.
- Opportunity selection asks which jobs are already accumulating payers, transactions, suppliers, tacit knowledge and portable distribution.
- Public examples are explicitly synthetic and must not resemble a real user profile derived from private conversation.

### Removed

- Any public example that depended on inferred or unverified personal-user information.
- The assumption that executives or prestigious titles are inherently better startup launchpads.

## v7.x — Opportunity Decision Architecture

Earlier design iterations introduced:

- causal reasoning chain;
- Power Pool analysis;
- dual scores;
- Real Options and Kill Criteria;
- assetization path;
- framework comparison;
- youth/campus early-warning signals.

The v8.0 clean rebuild preserved the useful methodology while resetting the public repository with stricter example/privacy rules and a stronger career-to-founder focus.
