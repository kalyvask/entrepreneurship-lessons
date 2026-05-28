# Value Proposition Canvas (Osterwalder)

A zoom-in on the two most important blocks of the Business Model Canvas — **Customer Segments** and **Value Proposition** — and a tool for forcing *fit* between what the customer needs and what you offer. From *Value Proposition Design* (Osterwalder, Pigneur, Bernarda, Smith, 2014).

The canvas exists to answer one question precisely: **does what you're building actually relieve a pain or create a gain the customer cares about?** Most product ideas fail this test and the founder doesn't notice until after they've built.

## The two halves

```
        VALUE MAP                              CUSTOMER PROFILE
   (what you make)                          (what they need)

  ┌──────────────────┐                    ┌──────────────────┐
  │  Gain Creators   │  ───── fit ─────▶  │      Gains       │
  ├──────────────────┤                    ├──────────────────┤
  │ Products &       │                    │   Customer       │
  │ Services         │  ───── fit ─────▶  │   Jobs           │
  ├──────────────────┤                    ├──────────────────┤
  │  Pain Relievers  │  ───── fit ─────▶  │      Pains       │
  └──────────────────┘                    └──────────────────┘
```

You build the **Customer Profile** first (from research, not imagination), then the **Value Map**, then check whether they fit.

## The Customer Profile (right side)

Built entirely from customer discovery — see [`stages/02_customer_discovery.md`](../stages/02_customer_discovery.md). If you're filling this in from your own assumptions, you're doing it wrong.

### Customer Jobs

What the customer is trying to get done. (This is JTBD — see [`frameworks/jobs_to_be_done.md`](jobs_to_be_done.md).) Three kinds:

- **Functional jobs** — the concrete task ("reconcile last quarter's inventory numbers")
- **Social jobs** — how they want to be perceived ("look competent to my VP")
- **Emotional jobs** — how they want to feel ("stop dreading the monthly close")

Rank jobs by importance to the customer. Most products address one important job well, not five jobs poorly.

### Pains

Bad outcomes, obstacles, and risks around the jobs:

- **Undesired outcomes** — "the reconciliation takes 15 hours and is still wrong"
- **Obstacles** — "I can't get the data out of the legacy system"
- **Risks** — "if I get the numbers wrong, the board loses confidence in me"

Rank pains by severity (extreme → moderate). **Severe pains are where desperation lives** — see the desperation markers in [`frameworks/pmf.md`](pmf.md).

### Gains

Desired outcomes and benefits:

- **Required gains** — without these, the solution doesn't work ("it has to integrate with our ERP")
- **Expected gains** — basic expectations ("it should be reasonably fast")
- **Desired gains** — would love but don't expect ("it would predict next quarter")
- **Unexpected gains** — beyond their imagination ("it found errors we didn't know existed")

Rank gains by relevance (essential → nice-to-have).

## The Value Map (left side)

What you offer, mapped to the profile.

### Products & Services

What you actually provide. The list of things the customer can use. Be concrete: features, services, the support that surrounds them.

### Pain Relievers

How your products/services kill specific customer pains. **Map each pain reliever to a specific pain on the right side.** If a pain reliever doesn't connect to a ranked pain, it's a feature you built for yourself.

### Gain Creators

How your products/services produce specific customer gains. Same discipline: **map each gain creator to a ranked gain.**

## Achieving fit

There are three levels of fit, and you reach them in sequence:

1. **Problem–solution fit** — your value map addresses pains and gains that customers actually have (you have evidence from discovery). This is on paper.
2. **Product–market fit** — customers behave: they buy, use, retain, refer. This is in the market. (See [`stages/06_pmf_measurement.md`](../stages/06_pmf_measurement.md).)
3. **Business model fit** — the value proposition can be embedded in a profitable, scalable model. (See [`frameworks/business_model_canvas.md`](business_model_canvas.md) and [`frameworks/unit_economics.md`](unit_economics.md).)

The canvas helps with level 1. Levels 2 and 3 require the market.

## How to use it well

1. **Fill the Customer Profile from research, not assumptions.** Every job, pain, and gain should trace to something a real customer said or did. If you can't cite the source, it's a hypothesis to test, not a fact.
2. **Rank ruthlessly.** Severe pains and essential gains are where value lives. A product that relieves a moderate pain is a vitamin; one that relieves a severe pain is a painkiller. (See [`frameworks/value_dimensions.md`](value_dimensions.md) — painkillers beat vitamins.)
3. **Map every reliever and creator to a ranked item.** Unmapped relievers/creators are features you built because they were fun, not because anyone needed them.
4. **Look for the gaps.** Severe pains with no pain reliever = your roadmap. Pain relievers with no corresponding pain = cut them.
5. **Re-do it after every batch of interviews.** The profile changes as you learn. The first version is mostly wrong; that's expected.

## Common failure modes

| Failure | Why it kills you |
|---|---|
| Profile filled from imagination | You design for a customer who doesn't exist |
| No ranking | You treat a trivial pain like a severe one; you build the wrong reliever |
| Relievers/creators with no mapped pain/gain | Feature creep disguised as value |
| Treating "fit on paper" as PMF | Problem–solution fit ≠ product–market fit; behavior is the test |
| Static canvas | It should change with every batch of learning |
| Too many jobs | A product that serves 5 jobs serves none well; pick the one important job |

## Where this lives in the journey

- [Stage 02 — Customer Discovery](../stages/02_customer_discovery.md) — fill the Customer Profile from research
- [Stage 03 — Problem-Solution Fit](../stages/03_problem_solution_fit.md) — achieve problem-solution fit on the canvas
- [Stage 04 — Value Hypothesis](../stages/04_value_hypothesis.md) — the value hypothesis is the canvas's value map, sharpened to a *what/who/how*

## Source

*Value Proposition Design* — Alexander Osterwalder, Yves Pigneur, Gregory Bernarda, Alan Smith (2014). The companion to *Business Model Generation*. Both central to the Lean Launchpad methodology. See also [`frameworks/business_model_canvas.md`](business_model_canvas.md).
