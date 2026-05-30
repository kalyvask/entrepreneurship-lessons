# Where the Frameworks Disagree

This repo synthesizes a shelf of methods — Lean Startup, Customer Development, RDI, the Mom
Test, Crossing the Chasm, Jobs to Be Done, Disruption Theory, the Business Model Canvas, the
10-Star Product. Most of the time they reinforce each other. Sometimes they give **opposite
advice at the same moment**, and a study guide that pretends otherwise leaves you to discover
the contradiction the expensive way.

This file names the real conflicts and says which side to follow, when, and why.

## The tie-breaker

When two methods disagree, the **product-market-fit learnings win**. Concretely, the four
rules that override everything else:

1. **Desperation, not need** — behaviour over stated intent.
2. **Iterate the *who* (sometimes the *how*), never the *what*** — hold the insight.
3. **Narrow** — the targetable who beats the big market.
4. **Rate of learning over rate of shipping** — make being wrong cheap.

If a framework's advice survives those four, follow it. If it doesn't, it loses here.

## The conflicts at a glance

| # | The tension | Side A | Side B | Follow… | Because |
|---|---|---|---|---|---|
| 1 | When to start building | Lean: ship an MVP early and learn | RDI: months of research before you commit | **B upstream, A once you have a desperate who** | A build is the most expensive way to learn; research is cheaper. Don't build before desperation. |
| 2 | Is the MVP the first test? | "MVP" colloquially = first thing you build | This repo: concept → implementation → **then** MVP | **B (staged sequence)** | One big test confounds five variables. Run the cheap tests first. |
| 3 | Breadth of understanding | JTBD: understand the job across the market | Moore: win one beachhead of early adopters | **A to find the job, B to pick the who** | Narrow who wins; use JTBD to aim, not to widen. |
| 4 | How complete v1 must be | Moore: pragmatists demand a whole product | Lean: ship the minimum | **B before PMF, A after** | Pre-PMF you sell to visionaries who tolerate broken. Whole-product is a post-chasm problem. |
| 5 | Listen to customers? | Blank: get out of the building, listen | Insight/disruption: customers can't see the non-consensus future | **Both, split by layer** | Listen for *pain and behaviour*; never let customers design the *what*. |
| 6 | Pivot fast or persevere? | Lean: celebrate the pivot | PMF/RDI: hold the what; don't death-pivot | **Pivot the who/how fast; hold the what; 3-month floor** | Conviction on the insight, flexibility on the who. |
| 7 | Pricing evidence | Surveys / lean-canvas WTP questions | Mom Test: observe payment, distrust stated WTP | **B always** | Stated willingness-to-pay is noise; observed payment is signal. |
| 8 | Vision vs. wedge | 10-star / "aim for a $100M business" | Narrowest wedge this week | **Both — already resolved** | Big destination, narrow first step. See `ten_star_product.md`. |
| 9 | The PMF number | Sean Ellis 40% "very disappointed" (consumer-origin) | B2B reads PMF via retention/expansion/references | **Weight by your motion** | The dogs eating the dog food looks different in enterprise; don't worship one number. |

## The ones worth expanding

### 1. "Ship the MVP" (Lean) vs. "earn the right first" (RDI)

The Lean Startup made "build-measure-learn" the default reflex: get something in front of
users and iterate. RDI and the prepared-mind stage say the opposite for someone who doesn't
yet know which problem matters — spend weeks in research before committing a line of code.

**They are sequenced, not competing.** RDI is upstream: its output (a defensible insight + a
desperate who) is the *input* to Lean. The failure mode is starting Lean's loop before you
have an insight — you build fast, learn nothing, and pivot in circles for two years.

> Follow RDI until you can name a specific problem and 10 real people who feel it. Then, and
> only then, switch to the build-measure-learn loop. **PMF tie-breaker:** a build is the most
> expensive learning there is; don't spend it to discover something a conversation would have
> told you.

### 4. Moore's "whole product" vs. Lean minimalism

Moore is right that **pragmatists** (the early majority, across the chasm) demand a complete
solution with references before they buy. Lean is right that you should ship the minimum.
These collide if you treat them as simultaneous.

They aren't. Pre-PMF you are selling to **visionaries / early adopters** who buy on vision and
tolerate a broken product. The whole product is what you assemble *after* PMF, to cross the
chasm. Building the whole product before PMF is the classic capital-burn.

> Pre-PMF: minimum that tests the leap of faith. Post-PMF: whole product to cross the chasm.
> **PMF tie-breaker:** build to learn, not to complete.

### 5. "Customers know" vs. "customers don't know"

Customer Development says get out of the building and listen. The insight-led/disruption view
says customers can't articulate a non-consensus future — if you'd asked them, they'd have
asked for a faster horse.

Both are true at different layers. **Listen for pain and past behaviour** (the Mom Test keeps
this honest). **Do not listen for solution requests** — the *what* comes from your insight,
not from a feature list dictated by lukewarm prospects. Adding requested features to
non-desperate customers is the "lunacy" failure mode.

> Customers own the problem and the desperation. You own the what. **PMF tie-breaker:**
> behaviour over opinions; iterate the who, never let the customer design the what.

### 6. Pivot fast vs. persevere

Lean made pivoting a badge of honour. RDI and the PMF framework warn against death-pivoting
and insist you hold the *what*. The resolution is in the vocabulary: a **pivot** changes the
*who* (sometimes the *how*) and is often right and should be done decisively; a **restart**
changes the *what* and rarely works.

> Pivot the who/how fast and cleanly; hold the what; give any single pivot a 3-month floor
> before the next decision. **PMF tie-breaker:** iterate the who, not the what; two pivots
> with no over-performing slice means restart or shut down, not a third pivot.

### 9. The 40% Sean Ellis bar isn't universal

The 40%-"very disappointed" threshold comes from consumer products with many users. A B2B
venture with eight enterprise customers can have real PMF that the survey under-reads, or a
flattering survey with leaky logos. Don't let one number override the rest of the Stage 06
rubric.

> Weight the PMF signals by your motion: consumer leans on Sean Ellis + organic; B2B leans on
> retention + expansion + unprompted references + shrinking sales cycle. **PMF tie-breaker:**
> the test is whether the dogs eat the dog food on their own, measured honestly for your
> motion — not a single borrowed benchmark.

## How to use this file

When a skill or a stage points you two ways at once, come here, find the conflict, and apply
the tie-breaker. The stages reference this file at the moments the tension actually bites
(building, narrowing, pricing, pivoting). If you find a conflict not listed here, that is a
good issue to open.

## Source

Original synthesis for this repo. Generalizes the one reconciliation already written in
`ten_star_product.md` ("The tension with narrowing — resolved") to the rest of the library.
Underlying methods are credited in `SOURCES.md`.
