# Journey Rubrics — Grade Yourself at Every Stage

The stages tell you *what to do*. The skills *coach* you. These rubrics let you **score yourself** — turning prose guidance into a pass/fail gate so you (or the agent) can honestly answer "is this stage actually done, or am I kidding myself?"

## How to use

- Score each dimension **0–3**: 0 = absent/failing, 1 = weak, 2 = solid, 3 = strong.
- The **pass bar** for advancing a stage is: **every dimension ≥ 2, and no dimension at 0.** A single 0 is a stop — that dimension is a hole that the next stage will fall through.
- Be brutal. The whole value of a rubric is that it resists the founder's instinct to round up. Score the evidence, not the hope.
- An agent (`/ent-stage-router`, `/ent-pmf-evaluator`) can grade against these; so can a co-founder or advisor. The most useful grade is one done by someone allowed to disagree with you.

Anti-gaming rule: a dimension scores high **only with evidence**. "We talked to customers" is a 1; "8 of 12 in our narrow segment had built a workaround and 3 pre-paid" is a 3. Behavior and specifics beat assertions.

**Evidence gate:** a score of 2 or 3 must cite a specific artifact in the venture workspace —
a row in `interviews.csv`, a line in `experiment_log.md`, a signed LOI, a number in
`pmf_dashboard.md`. No artifact, the score is at most 1. Record scores in `rubric_scores.md`.
Before grading the Stage 06 → 07 gate, run `/ent-red-team` automatically.

---

## Stage 00 — Prepared Mind

*Can you advance to picking an insight?*

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Fluency** | Can't hold a conversation in the space | Knows the jargon | Cocktail-party conversational | Insiders treat you as one of them |
| **Research network** | <5 contacts | 10–20 | 30–50 who'd take your call | 50+ inbound starting |
| **Earned secrets** | Only consensus views | One mild surprise | 1–2 beliefs that surprise informed people | Multiple defensible non-obvious beliefs |
| **Conviction vs. enthusiasm** | Excited, can't say why | Enthusiasm only | Conviction with reasons | Conviction + honest about failure modes |
| **A specific problem** | A space, no problem | A vague problem | A specific recurring problem named | A problem + who feels it most acutely |
| **Rubric fit** | Haven't built one | Built, not applied | Passes must-haves | Passes, with trade-offs explicit |

**Pass:** all ≥ 2, no 0s. If "a specific problem" is below 2, you're still exploring — stay in Stage 00. → next: [`stages/01_insight_and_idea.md`](../stages/01_insight_and_idea.md)

---

## Stage 01 — Insight & Idea

*Do you have a falsifiable bet, not a wish?*

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Three-part structure** | A wish ("would be cool") | An idea, no structure | Inflection → possibility → blindspot, stated | …and each part defensible with evidence |
| **Non-consensus** | Everyone agrees | Mildly differentiated | 3 informed people would dispute it | …and you can defend against each |
| **Inflection / why-now** | No why-now | "AI is changing things" | Specific change, dated | 3+ pieces of evidence for it |
| **Structural blindspot** | "We'll move faster" | Vague | Named structural reason incumbents can't | RPV-grounded, would-cost-them-X tested |
| **Targetable wedge** | "Mid-market" | A broad segment | Can identify 50 specific customers | Can name 10 real ones today |
| **10-year excitement** | Meh | Financial only | Excited about the destination | Excited *and* it survives the hard parts |

**Pass:** all ≥ 2, no 0s. If non-consensus or inflection is below 2, you have an idea, not an insight. → next: [`stages/02_customer_discovery.md`](../stages/02_customer_discovery.md)

---

## Stage 02 — Customer Discovery

*Have you found a desperate customer, not a polite one?*

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Narrow who** | "Companies" | A broad segment | Nameable; 50 identifiable | 10 real names listed |
| **Desperation markers** | Politeness only | 1–2 markers, scattered | 3+ markers in 5+ people | Strong markers across the segment |
| **Workaround evidence** | None | Mentioned vaguely | Observed a real workaround | Multiple, built independently |
| **Recurrence** | You raised it | Came up once | Unprompted across conversations | Unprompted + emotionally charged |
| **Mom Test discipline** | Pitched; got compliments | Some leading questions | Behavior-focused, past-tense | Clean — uncomfortable, no compliments |
| **Sample depth** | <10 interviews | 10–20 | 30–50 | 50+ with synthesis |

**Pass:** all ≥ 2, no 0s. If desperation markers or workaround evidence is below 2, you have a needy market — kill signal. → next: [`stages/03_problem_solution_fit.md`](../stages/03_problem_solution_fit.md)

---

## Stage 03 — Problem–Solution Fit

*Real hot problem + plausible solution + non-broken economics?*

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Problem statement** | Vague | Some lines evidenced | Every line evidenced | …and defensible to a skeptic |
| **One pain** | Five pains | Two or three | One sharp pain | One pain + frequency × magnitude quantified |
| **Painkiller not vitamin** | Vitamin | Mild painkiller | Clear painkiller | Painkiller + psychological value dimension |
| **Unit economics** | LTV/CAC < 1 | ≈ 1 | > 3 plausible at scale | > 3 + payback < 12mo |
| **Concept-test commitments** | Compliments only | One soft yes | 3+ behavioral commitments | Pre-pays / signed LOIs |
| **Leap of faith** | Unnamed | Vague / technical | One behavioral assumption | …and a direct test designed |

**Pass:** all ≥ 2, no 0s. If concept-test commitments or unit economics is below 2, don't build yet. → next: [`stages/04_value_hypothesis.md`](../stages/04_value_hypothesis.md)

---

## Stage 04 — Value Hypothesis

*Is the bet specific enough to test?*

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **What** | "AI for X" | A category | Specific, buildable in 3–6mo | …with explicit v1 exclusions |
| **Who** | "Developers" | A segment | Narrow; 10 nameable | …defined by behavior + circumstance |
| **How** | Undefined | Vague pricing | Delivery/distribution/price set; charges from day one (unless ad-based) | …and matched to how the buyer buys |
| **Leap of faith** | = the whole hypothesis | Two+ assumptions | One behavioral assumption, separated | …testable with a direct experiment |
| **What's NOT in v1** | Everything's in | Implicit | Explicit exclusion list | …ruthless, tied to the LOF |
| **Stress-tested** | Never challenged | Friends liked it | Survived a founders' feedback meeting | …a customer + skeptic + investor pushed and it held |

**Pass:** all ≥ 2, no 0s. If the leap of faith is below 2 (five assumptions in one), you can't interpret the MVP. → next: [`stages/05_mvp_build.md`](../stages/05_mvp_build.md)

---

## Stage 05 — MVP Build

*Did you build the smallest thing that tests the leap of faith — and is it in real hands?*

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Usable & live** | Slides / mockup | Prototype | Usable product in customers' hands | …used in the real workflow |
| **Smallest feature set** | 15 features | Overbuilt | Only what tests the LOF | …with non-core done by humans (concierge) |
| **Paying customers** | 0 | 1–2 | 5+ in the narrow who | …converting in days, not months |
| **LOF tested by behavior** | Untested | Stated intent | Real behavior tested it | …confirmed or cleanly refuted |
| **Built to learn** | Built to scale prematurely | Shipping heads-down | Learning rate is the metric | Two-week review cadence held |
| **Instrumented** | Not measuring | Vanity metrics | Measuring the LOF behavior | …cohort/retention wired from day one |

**Pass:** all ≥ 2, no 0s. Fewer than 5 paying customers = no problem-solution fit; go back. → next: [`stages/06_pmf_measurement.md`](../stages/06_pmf_measurement.md)

---

## Stage 06 — PMF Measurement

*Are the dogs eating the dog food?*

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Held narrow who** | Broadened to anyone | Drifting | Held the narrow who | …and measuring only against it |
| **Sean Ellis** | <10% very disappointed | 10–25% | 25–40% climbing | ≥ 40% in the narrow who |
| **Retention** | Asymptotes to zero | Decaying slowly | Flattens above zero (paying) | …flat + improving cohort-over-cohort |
| **Organic acquisition** | All paid | <20% organic | ~40% and climbing | >40%; could stop paid and still grow |
| **LOF verified** | Unverified | Anecdotal | Verified by behavior | …by a specific, repeatable behavior |
| **The tells** | None | One | 3+ (referrals, shrinking cycle, pricing power) | Customers sell it for you |

**Pass:** all ≥ 2, no 0s, AND Sean Ellis ≥ 40% with retention flattening = **PMF**. Below bar → [`stages/07_pivot_or_persevere.md`](../stages/07_pivot_or_persevere.md).

---

## Stage 07 — Pivot or Persevere

*Are you making the change decision cleanly, not emotionally?*

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Failure mode diagnosed** | "It's not working" | A guess | Mapped to who/how/what/insight | …with the specific failing metric named |
| **Over-performing slice** | Not looked | Looked, unclear | Identified (or honestly none) | …and the pivot points toward it |
| **New value hypothesis** | None | Vague | Defensible what/who/how/LOF | …grounded in existing data |
| **Written commitment** | Verbal only | Loose | Timeline + success/fail thresholds | …+ pre-committed next move, co-signed |
| **Pivot vs. restart** | Restarting unknowingly | Confused | Distinguished correctly | …holding the what, iterating the who |
| **Decision owned** | Investor/emotion-driven | Pressured | Team owns it | …data-driven, panel-informed |

**Pass:** all ≥ 2, no 0s. If you've pivoted twice with no over-performing slice, the honest score is "shut down or restart" — don't pivot a third time.

---

## A note on scoring honestly

The rubric only works if you score the evidence, not the ambition. Two habits:

1. **Cite the evidence for every score of 2–3.** If you can't point to a specific conversation, number, or behavior, the real score is 1.
2. **Have someone else grade you.** Founders systematically over-score their own who-narrowness, their desperation evidence, and their PMF. The most useful grade comes from a co-founder, advisor, or the `/ent-red-team` skill — someone allowed to disagree.

The rubric is a mirror, not a trophy. Its job is to tell you where you actually are, so you stop advancing on hope.
