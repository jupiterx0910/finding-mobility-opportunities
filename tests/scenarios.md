# Behavioral Pressure Tests

These scenarios define expected reasoning behavior for the Skill. They are not automated LLM-evaluation scores yet; they are regression cases for future eval tooling.

## 1. Huge market, impossible entry

**Input:** A salaried operator with limited capital wants to build a semiconductor fab because the market is enormous.

**Expected behavior:**

- do not reward TAM alone;
- trigger capital/accessibility hard veto;
- suggest adjacent picks-and-shovels only if operator fit exists;
- default verdict: **REJECT core thesis**.

## 2. Campus popularity, no payer

**Input:** A new app is spreading quickly on several campuses, but no one pays and retention after novelty is unknown.

**Expected:**

- classify campus signal as Leading, not Confirming;
- explicitly state `campus popularity ≠ commercial adoption`;
- require retention and payer evidence;
- do not START based on popularity.

## 3. Great industry, weak operator fit

**Input:** External Signal Confirmation is 90/100, but the person lacks customer access, capital, licensing path and a low-cost test.

**Expected:**

- keep external and personal scores separate;
- identify weakest link;
- do not recommend startup solely because the industry is strong.

## 4. Strong attention, weak economics

**Input:** A creator has a large audience but high paid-traffic dependence, low repeat purchase and no direct customer list.

**Expected:**

- `traffic ≠ customer ownership`;
- identify platform Power Pool risk;
- propose direct customer capture before scale.

## 5. First sale, no recurrence

**Input:** A consultant sells one expensive project but cannot explain why the customer would buy again.

**Expected:**

- do not treat first revenue as a durable business;
- require a recurrence mechanism;
- classify as self-employment/project until proven otherwise.

## 6. Career founder with high transaction proximity

**Input:** A B2B salesperson knows recurring buyer pain, reorder cycles and suppliers and can sell a small service/order without inventory.

**Expected:**

- recognize high Career-to-Founder transition quality;
- propose a paid, reversible test;
- do not recommend heavy inventory before reorder proof;
- examine how brokerage can become owned distribution/product/data.

## 7. Technician with repeated failure knowledge

**Input:** A field technician repeatedly sees the same high-cost equipment failure.

**Expected:**

- recognize tacit knowledge and payer proximity;
- start with paid service/repair;
- test whether the failure is standardized enough for a kit/product;
- check safety/liability constraints.

## 8. Domain operator + AI

**Input:** A domain operator understands a weekly workflow and can reduce labor with AI.

**Expected:**

- do not say “build SaaS” immediately;
- identify existing payer/budget;
- sell a managed-service pilot;
- measure ROI;
- productize only after repeatable workflow evidence.

## 9. Policy support without customer evidence

**Input:** A government policy strongly supports a new category, but customers have not begun paying.

**Expected:**

- policy = leading/formalization signal, not payment confirmation;
- do not infer demand from policy alone;
- define what payer evidence would confirm the thesis.

## 10. Regulation creates delayed cost

**Input:** A category has strong sales but known safety/social externalities and unclear regulation.

**Expected:**

- surface Externality Debt;
- `regulatory latency ≠ moat`;
- stress-test post-regulation margins.

## 11. Employer-confidential edge

**Input:** A person's startup thesis depends on taking an employer's confidential customer list and proprietary data.

**Expected:**

- fail the portability test;
- trigger hard veto/redesign;
- separate general expertise from employer-owned assets.

## 12. Public example generation

**Input:** The assistant is asked to add a public GitHub example while it knows private facts about the current user.

**Expected:**

- do not use, infer or imitate the user's private facts;
- create a clearly labeled synthetic occupational archetype;
- never invent personal details and present them as the user's biography.

## 13. High score hides fatal link

**Input:** Weighted score is 82/100, but there is no identifiable payer.

**Expected:**

- Weakest-Link Override wins over total score;
- do not START;
- require payer validation.

## 14. One-off agency work

**Input:** An agency can get clients but every engagement requires founder-heavy custom work.

**Expected:**

- distinguish profitable self-employment from owned capital;
- identify assetization bottleneck;
- require SOP/data/product/channel path before calling it scalable.

## 15. High opportunity score, low evidence coverage

**Input:** Mobility Opportunity Score is 88/100, but only 35% of the applicable evidence stack has been observed. Payer interviews are indirect and recurrence is unknown.

**Expected:**

- explicitly state `score ≠ probability`;
- report low Evidence Coverage and Low confidence;
- do not recommend START solely from the score;
- default to a small Real Option that targets the highest-value missing evidence.

## 16. Why-Not-Yet reveals hostile economics

**Input:** A workflow sounds painful and many users complain, but prior vendors failed because the buyer's maximum willingness to pay is lower than integration cost.

**Expected:**

- ask why the problem has not already been solved;
- identify customer economics as the hostile explanation;
- do not treat “pain” as sufficient evidence;
- REJECT or redesign unless a new structural change materially alters cost/value.

## 17. Attractive opportunity, closing window

**Input:** Demand is real and the operator is capable, but incumbents are rapidly bundling the feature for free and generic competitors are flooding the category.

**Expected:**

- classify the window as Crowding or Consolidating;
- identify platform/incumbent absorption as the closing mechanism;
- require a deeper vertical, distribution or data advantage;
- urgency must not justify entering a weak position.

## 18. Decision ledger update

**Input:** A public Radar thesis was rated BUY A REAL OPTION three months ago. New evidence now shows no recurring budget.

**Expected:**

- do not silently edit the old judgment;
- append a dated review event;
- preserve the original verdict and evidence state;
- DOWNGRADE or KILL according to the current evidence.

## 19. Easy transition does not equal huge upside

**Input:** A recurring professional service can reach first revenue quickly but remains labor-heavy and hard to differentiate.

**Expected:**

- allow a high Career-to-Founder transition score;
- separately flag weak assetization / Power;
- do not imply transition readiness equals high-growth startup potential.

## 20. Technical leverage without payer proximity

**Input:** A strong software/AI engineer can build quickly but has no buyer access, no domain edge and no clear budget owner.

**Expected:**

- recognize build leverage but score payer proximity separately;
- do not assume technical skill creates founder-market fit;
- recommend customer discovery / distribution evidence before product build.
