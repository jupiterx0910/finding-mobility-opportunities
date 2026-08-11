# Contributing

Opportunity Radar becomes more useful when contributions add **evidence, counterexamples, backtests and falsifiable hypotheses**, not just more ideas.

## Good contributions

- historical backtests using only evidence observable at the time;
- dated emerging-opportunity signals with primary sources;
- counterexamples that expose a weak rule;
- synthetic career-to-founder cases;
- better scoring or veto logic;
- pressure-test scenarios;
- corrections to current radar entries.

## Public Example Privacy Rule

This rule is mandatory.

All public founder/operator examples must be **synthetic / fictional**.

Do **not** use:

- a real user's private conversation;
- remembered user history;
- private profile data;
- inferred personal background;
- unverified details about a real person;
- employer-confidential customer/supplier data.

Every file in `examples/` must clearly state that it is a fictional operator archetype and is not based on any real user or private conversation.

If a real public founder/company is used in a historical case, cite public sources and separate documented facts from interpretation.

## Add an Opportunity

Include:

```text
Opportunity:
Geography:
As-of date:
Structural need:
Opening change / why now:
Best-fit career/founder archetypes:
Payer:
Payment evidence:
Talent signal:
Supply-chain signal:
Formalization / regulation:
Power Pool hypothesis:
Leading indicators:
Confirmation indicators:
Kill criteria:
Unknowns:
Primary sources:
```

## Add a Synthetic Founder Example

Include:

```text
Synthetic archetype:
Why this career is close to the opportunity:
Portable edge:
Non-portable / employer-owned assets to avoid:
Payer:
Concrete offer:
30–60 day paid test:
Recurrence:
Power Pool:
Assetization:
Kill criteria:
Verdict:
```

Do not write biographies. The purpose is to test a transition pattern, not to imitate a real person.

## Add a Historical Backtest

A good backtest must answer:

1. What structural need existed?
2. What changed?
3. Which people/careers were naturally positioned?
4. What signals were observable **at the time**?
5. When did payment become visible?
6. How did the ecosystem form?
7. Where did the Power Pool settle?
8. What should the framework have rejected?
9. What could not have been known early?

Avoid hindsight theater. If your argument depends on knowing the eventual winner, rewrite it.

## Evidence Standards

Prefer:

1. primary sources;
2. regulators / standards bodies;
3. company filings and official product/career pages;
4. high-quality research and authoritative datasets.

Label inference as inference.

Do not use funding, downloads, social attention or a single news story as proof of a durable business.

## Pull Request Checklist

- [ ] Claims that can change include an as-of date.
- [ ] Public examples are synthetic or are documented public historical cases.
- [ ] No private user/profile/conversation data appears.
- [ ] Facts and inferences are separated.
- [ ] Payer is explicit.
- [ ] Power Pool is addressed.
- [ ] Kill criteria are written before a strong conclusion.
- [ ] Links/sources work.
- [ ] `python scripts/validate_skill.py` passes.
