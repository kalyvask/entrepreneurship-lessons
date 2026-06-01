# Judgment and Pareto — Deciding Under Uncertainty

Most of this library is about gathering evidence so you can decide well. But the defining condition
of the pre-PMF search is that **the evidence is never complete** — you act on partial data, against a
deadline, with money running out. The scarce, high-leverage skill in that condition is **judgment**:
making a good call when the data needed to be certain does not exist and cannot be obtained in time.

This framework is the operating discipline for those calls. It pairs with every gate in the journey
— each one (advance or not, pivot or persevere, what to build, what to test next) is a judgment call
made on incomplete information.

## Judgment, defined

Judgment is the ability to make good decisions under uncertainty. Anyone can decide well when all the
data is on the table; that is bookkeeping, not judgment. The rare ability is to be right more often
than not when the data is missing — and to know which missing data actually matters and which is
noise you can ignore.

Two implications for a founder:

- **It is the highest-leverage skill pre-PMF**, because ambiguity is the default, not the exception.
  You will rarely have the study, the cohort, the sample size you want before the decision is due.
- **It is learnable but not teachable by rule.** It comes from repeatedly making calls, seeing what
  happened, and tightening the model. The fastest way to build it is to watch someone with excellent
  judgment decide, and study *what they chose to ignore*.

## Pareto — the operating discipline of the under-resourced

The 80/20 principle is the single most useful tool for exercising judgment under scarcity: **a small
fraction of the problem (roughly 20%) drives most of the value (roughly 80%). Find that fraction and
work only on it.** Everything else is, for now, a distraction you can defer or drop.

This is not a productivity nicety. Pre-PMF you are structurally short on time, people, and money, so
the only way to move is to refuse to spread effort evenly. The discipline is:

1. **Name the few variables that actually move the outcome.** For a pre-PMF venture that is almost
   always: is the customer *desperate*, is the narrow *who* right, is the leap of faith being tested.
   Not: the logo, the pricing page, the org chart, the roadmap past the next test.
2. **Put effort there and consciously starve the rest.** Choosing what *not* to do is the act.
3. **Re-derive the 20% each stage**, because it moves. In discovery it is desperation evidence; at
   the MVP it is the leap-of-faith behaviour; at the PMF gate it is retention and organic pull.

A tell of strong judgment: when handed a long list of things that "should" be looked at, the operator
declines most of it as low-relevance rather than dutifully grinding through all of it. Answering every
question equally is the absence of judgment, not its proof.

## Optimize for magnitude, not hit rate

You will not be right most of the time, and chasing a high hit rate makes you timid. The people with
the best judgment are often right only slightly more than half the time — but they are **big when they
are right and small when they are wrong**. Borrowing the baseball term, optimize **slugging
percentage**, not batting average: the magnitude of the correct calls is what compounds, not the
fraction of calls that were correct.

Practically: size the bet to the conviction and the evidence. A weak-evidence call gets a cheap,
reversible test (a concept test, not a build). A high-conviction, evidenced call gets real resources.
This is the same logic as the three-phase validation sequence — make being wrong cheap, so that being
right occasionally can be large.

## How to sharpen it

- **Decide the 20% before you gather.** Write down, before the data comes in, which one or two facts
  would actually change the decision. Go get *those*; ignore the rest. (This is the pre-registration
  habit from `playbooks/concept_test.md`, applied to thinking rather than testing.)
- **Make the call, write the reasoning, check it later.** Judgment improves only with a feedback
  loop. The `lof_ledger.md` and `decision_dossier.md` in the venture workspace exist partly for this:
  a logged decision with its reasoning is a judgment you can grade in hindsight.
- **Study someone who decides well.** You do not need a formal mentorship — observe what an operator
  with a track record chooses to focus on and, more tellingly, what they wave away. See the career
  layer's note on learning by observation (`career/career_strategy.md`).
- **Separate reversible from irreversible.** Spend judgment on the irreversible calls; default-yes and
  move fast on the reversible ones. See `frameworks/conflicts.md` for where this overrides "gather
  more evidence."

## Where this lives in the journey

Judgment and Pareto are not a stage; they are how you execute every stage under uncertainty. They
bite hardest where the data is thinnest and the stakes highest:

- [Stage 05 — MVP Build](../stages/05_mvp_build.md) — what to build vs. cut is a Pareto call on the
  leap of faith; `/ent-mvp-review` and `/ent-mvp-scoper` apply it.
- [Stage 07 — Pivot or Persevere](../stages/07_pivot_or_persevere.md) — the highest-stakes judgment
  call in the journey, made on deliberately incomplete data; `/ent-pivot-coach` runs it.
- [Stage 06 — PMF Measurement](../stages/06_pmf_measurement.md) — reading thin, noisy early metrics
  is judgment, not arithmetic; `/ent-pmf-evaluator` applies it.

The tie-breaker when judgment and "get more data" conflict: see `frameworks/conflicts.md`. Pre-PMF,
the cost of a slow decision is usually higher than the cost of a wrong-but-cheap one.

## Source

Original synthesis for this repo. The 80/20 principle is Vilfredo Pareto's; the judgment-under-
uncertainty and magnitude-over-frequency framings are widely held in venture practice. Written here in
the repo's own words, consistent with `SOURCES.md`.
