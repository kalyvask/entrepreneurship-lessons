# Stage 04 — The Value Hypothesis

> Rachleff's fire metaphor: a growth hypothesis only adds fuel to a fire that already exists. It can't start one. Only a value hypothesis can start the fire.

The value hypothesis is the artifact this entire methodology has been preparing you to write. It is short. It is specific. It is testable. And nine out of ten teams write it wrong on the first try.

This file is long because the value hypothesis is the most important thing you will write during your search for PMF. Read it twice.

## The structure

A value hypothesis has three components and one prerequisite.

```
VALUE HYPOTHESIS
What:   [the product — one sentence, specific enough to build to]
Who:    [the customer — narrow enough to identify 50 specific people]
How:    [the delivery / distribution / monetization]

LEAP OF FAITH
The one thing that must be true for this hypothesis to work.
```

That's it. No 9-section canvas. No 40 slides. **One paragraph plus one sentence.**

The discipline of the structure is the point. If you cannot compress your hypothesis to this shape, your understanding is not yet sharp enough. The compression itself produces the clarity.

## The three components

### What

The product. What you would build, in a sentence specific enough that an engineer could begin designing to it.

**Bad whats:**
- "A SaaS platform for HR teams" — too vague; many products fit
- "An AI tool" — meaningless
- "A marketplace that connects buyers and sellers in X" — the format, not the product

**Good whats:**
- "A web app that ingests vertical-farm crop schedules and produces daily harvest assignments per worker, optimizing for delivery commitments and waste minimization."
- "A SDK that lets mobile apps run on-device LLM inference under 3 seconds latency on iPhone 14+, with no network call."
- "A clinic management system specifically for direct primary care practices under 5 physicians, with embedded billing for membership-based plans."

The What should be **narrow enough** that you can build a useful first version in 3–6 months. It should be **specific enough** that you have to make explicit trade-offs (e.g., "no scheduling features in v1"). And it should be **honest** — what would actually be built, not what you'd write in a deck.

### Who

The customer. **The most counterintuitive and important part of the hypothesis.** Founders almost universally write this too broadly the first time.

**Bad whos:**
- "Mid-market companies" — there are 200,000 of them and they have nothing in common
- "Anyone running ops at a startup"
- "Consumers who care about sustainability"
- "Developers"

**Good whos** (from the Wealthfront staircase Rachleff teaches):
- "Engineers in consumer-focused tech companies about to go public, with under $1M in assets, who were reluctant DIY index investors."

That's narrow. So narrow that a stranger reading it can immediately picture exactly the person and exactly the situation. **That is the bar.** If you cannot manually find and reach out to 50 specific people who match your *who*, you have not narrowed enough.

A useful test: write down 10 names. Real people, real LinkedIn profiles, who fit your *who*. If you can't, the *who* is too vague.

A second test: would it be obvious to a customer reading your value prop that this is for them, or would they need a sales rep to convince them it might be? If they need convincing, the *who* is wrong (or the *what* is — but start by narrowing the *who*).

**Why narrow matters.** Narrow whos enable:
- Word-of-mouth growth (they all know each other; a small market is a connected one)
- Sharp positioning (you can speak their language)
- High concentration of feedback (your 10th customer is in the same Slack/conference/forum as your 1st)
- Sharp pricing (you can price to the specific value, not to a blended market)

After PMF, you broaden. Before PMF, you narrow.

### How

How you deliver, monetize, and distribute. Three sub-components:

- **Delivery:** Subscription? One-time purchase? Marketplace fee? Platform? Embedded?
- **Distribution:** Direct sales? Self-serve PLG? Channel partner? Inside sales? Outbound? Inbound?
- **Pricing model:** Per seat? Usage? Tiered? Flat? Free + upsell?

The How is where unit economics live. A great *what* sold the wrong way (e.g., self-serve product to a buyer who needs hand-holding) fails on the *how*. A weak *what* can sometimes survive a great *how* (the right channel matched to the right buyer).

**Charge from day one (unless you're ad-based).** A default heuristic: build payment into the *how* from the start, even a small amount. Free pilots and "we'll monetize later" filter for curiosity, not desperation — and the friction of payment is itself the cleanest desperation test. A desperate customer pays. The exception is genuinely ad-supported / network-effect consumer models where usage must precede monetization; everywhere else, the inability to charge early is a signal the pain isn't acute enough.

This is also the part of the hypothesis most likely to need iteration after MVP. Many companies that look like pivots in retrospect were *how* changes, not *what* changes. **Iterate the who, sometimes the how, almost never the what.** (See [Stage 07 — Pivot or Persevere](07_pivot_or_persevere.md).)

## The leap of faith

This is the most important word in the methodology. Most teams confuse it with the value hypothesis. It is something different.

**The leap of faith is the *one* thing that must be true for the business to work.** It is upstream of the value hypothesis: the value hypothesis is the *what, who, how* you chose *because* of the leap.

Examples:

- **SpaceX leap of faith:** Reusable rockets can dramatically reduce launch costs. → Value hypothesis: A launch services company offering low-cost rocket launches.
- **Airbnb leap of faith:** People will sleep in a stranger's house. → Value hypothesis: A marketplace where homeowners rent rooms to travelers.
- **Wealthfront leap of faith:** People will allow software to manage their investments. → Value hypothesis: A robo-advisor for engineers with under $1M in assets.
- **Anthropic leap of faith:** People will care about AI being more responsible. → Value hypothesis: An AI lab whose strategy reinforces responsibility — initially serving engineers (who care most), later enterprises (where it matters most).

**One sentence. One assumption.** If it's true, the business has a chance. If it's not, no amount of execution saves you.

The discipline:
1. **Surface it explicitly.** Write it down. On its own line. Separated from the value hypothesis.
2. **Hold it as a hypothesis, not a fact.** Anything you have not behaviorally verified is a hypothesis. The leap of faith is what you'd most like to test first.
3. **Design your MVP to test it.** As directly as possible. Strip everything else.

The most common mistake teams make every year — Rachleff says this every quarter — is **conflating the value hypothesis with the leap of faith, baking five assumptions into one MVP, and then being unable to interpret the results.** When the MVP underperforms, you don't know if the leap of faith was wrong, the value hypothesis was wrong, the implementation was wrong, the channel was wrong, or the pricing was wrong. Five variables changing at once is a scientist's nightmare.

## The narrowing exercise

You arrive at a great value hypothesis through narrowing, not abstraction. Practical method:

### Step 1 — Draft the broadest plausible version

Write your value hypothesis as broadly as you'd be comfortable saying it. Don't censor.

### Step 2 — Narrow the who one level at a time

Take your who. Apply *constraint after constraint* — geography, company size, role, lifecycle, behavior, pain trigger, budget level, technical sophistication — until you reach the Wealthfront-level of specificity.

Each narrowing should be defensible:
- *Why* this constraint? (Evidence from discovery.)
- *What* does it exclude? (Who falls out — and why is that okay?)
- *Can* I still find 50 of them? (Or have I narrowed myself out of a market?)

### Step 3 — Re-test against discovery evidence

For the narrowed *who*, ask: which of my desperate customers from Stage 02 actually match this? If fewer than 5 match, the narrowing is too tight or the discovery sample was wrong. If most match, you've correctly identified the cluster.

### Step 4 — Restate the what to fit the narrowed who

Often a narrow *who* obviates features that were in the broad *what.* A vertical-farm crop scheduler for "all of agriculture" needs to handle 50 use cases; for "10–50k sq ft leafy greens, single-site, US" it might need to handle 3. The narrow *who* lets you make the *what* sharper.

### Step 5 — Articulate the leap of faith separately

After the *what / who / how* is written: ask the prompt — *if all three were perfectly executed, what one thing would still need to be true for this to work?* That's your leap of faith.

## Worked examples

Three sanitized templates, drawn from the patterns visible in student work and published cases:

### Example A — Enterprise SaaS

```
VALUE HYPOTHESIS
What: A web application that ingests scheduling data from vertical-farm growing software (Argus, Priva) 
      and produces daily harvest-and-delivery assignments for hourly workers, optimizing for 
      delivery commitments and waste minimization.
Who:  General managers of US-based, single-site, leafy-greens vertical farms in the 10,000–50,000 sq ft 
      capacity range, currently coordinating harvest schedules via Excel and Slack, with at least one 
      major wholesale customer they cannot afford to miss.
How:  SaaS, $2,000–4,000/mo, sold via outbound founder-led sales to GMs, free 30-day pilot.

LEAP OF FAITH
Mid-market vertical farm GMs will treat scheduling optimization as a P1 problem worth a 
multi-thousand-dollar monthly subscription within 3 months of seeing the product work once.
```

### Example B — Developer infrastructure

```
VALUE HYPOTHESIS
What: An SDK and on-device runtime that lets iOS apps run 7B-parameter LLMs locally with sub-3-second 
      latency on iPhone 14+ hardware, with no network call required.
Who:  Mobile-first product teams at consumer apps with >100k MAU that handle sensitive user content 
      (mental health, finance, journaling) and cannot send user data to cloud LLM endpoints for 
      regulatory, privacy, or trust reasons.
How:  Developer-led PLG, free tier under 10k devices, $5k/mo at 100k devices, Apple App Store 
      compliance support included.

LEAP OF FAITH
Mobile teams currently using cloud LLMs will accept the build-complexity trade-off of an on-device 
runtime in exchange for not sending user content off-device.
```

### Example C — Consumer

```
VALUE HYPOTHESIS
What: A mobile app where direct primary care patients submit a daily 30-second video to their physician 
      and receive an asynchronous text response within 24 hours.
Who:  DPC (direct primary care) patients aged 35–55 paying $200–500/mo membership at small (<5 physician) 
      practices, who currently communicate with their clinician via phone tag and email and routinely 
      delay raising minor concerns.
How:  Bundled into the DPC practice's existing membership (no patient charge), $4/patient/mo billed to 
      the practice, distributed via clinician-led launch within each practice.

LEAP OF FAITH
DPC clinicians will recommend (and patients will use) async video for routine concerns frequently 
enough to convert at least 40% of phone-tag interactions, justifying $4/patient/mo to the practice.
```

In each case: the leap of faith is the one behavioral assumption that the rest of the business rests on. Test that, you test the business. Skip it, you're flying blind.

## Sanity-check questions

Before you commit, run the hypothesis through these:

**What questions**
- Is it specific enough that an engineer could begin designing to it?
- Is it narrow enough that you can build a useful v1 in 3–6 months?
- Have you explicitly named what's NOT in v1?
- Is there a clear inflection that makes this *what* possible/necessary now?

**Who questions**
- Can you name 10 real people who match?
- Can you describe how you'd reach 50 more?
- Is the *who* defined by behavior and circumstance, not demographics?
- Would a person reading the *who* know immediately whether it's them?

**How questions**
- Does the pricing match the magnitude of pain you observed?
- Does the distribution match how the customer naturally discovers solutions?
- Are the unit economics plausible at scale (LTV/CAC > 3, payback < 12 mo)?

**Leap of faith questions**
- Is it ONE assumption, not five?
- Is it behavioral, not technical? (Technical risk is execution; behavioral risk is the leap.)
- Can you describe an experiment that would directly test it?
- Are you uncomfortable when you state it aloud? (If not, it's probably consensus — not a leap.)

## Founders' feedback meeting

The PMF framework includes a specific ritual: the **founders' feedback meeting**. You present your value hypothesis to a panel of advisors, customers, and skeptics. The panel's job is to **criticize, not to approve.** Your job is to **listen, not to defend.**

The exit criterion: the team owns the decision to proceed. Not the panel.

Whether you formally run a founders' feedback meeting or not, the spirit matters: before committing to build, you submit the hypothesis to people who will push back. If nobody pushes back, your hypothesis is probably consensus — or your reviewers are too polite. Find different reviewers.

## Common failure modes in this stage

| Failure | What it looks like | Why it kills you |
|---|---|---|
| Compound value hypothesis | "We're building X, Y, and Z for A, B, and C with three pricing models" | Untestable; you can't run a controlled experiment |
| Vague who | "Mid-market", "developers", "ops teams" | You'll talk to anyone with a pulse; the data is noise |
| Vague what | "AI for X" with no specifics | Engineering can't start; you'll keep redefining |
| Leap of faith = value hypothesis | Treats the whole hypothesis as the leap | Five variables in one experiment; uninterpretable results |
| Leap of faith is technical | "We need to build a thing that works at low latency" | That's an engineering risk, not a leap of faith. Leaps of faith are behavioral. |
| Skipping the founders' feedback meeting | "We don't need to defend it" | You'll defend it to a customer instead, and that's an expensive room |
| Hedging the *who* | "Primarily X, but also Y and Z" | If you can serve three audiences, you're not narrow. Pick one. |
| Optimizing for the deck, not the test | Pitch-ready bullets, untest-ready specifics | The hypothesis is for *you* to test, not for someone else to read |

## Exit criteria

You move to [Stage 05 — MVP Build](05_mvp_build.md) when:

1. The value hypothesis fits on one screen and is specific enough to build to.
2. The leap of faith is one sentence, behavioral, separated from the value hypothesis.
3. You've stress-tested it in a founders' feedback meeting or equivalent.
4. You have an explicit list of what's IN and what's NOT IN v1.
5. You know how you'd design an MVP that tests the leap of faith directly.
6. Your back-of-envelope unit economics work at the price level you're contemplating.

## Required reading

- [`frameworks/pmf.md`](../frameworks/pmf.md) — the value hypothesis framework in full
- [`frameworks/lean_startup.md`](../frameworks/lean_startup.md) — Ries on leap of faith and MVPs
- [`frameworks/customer_development.md`](../frameworks/customer_development.md) — Blank's parallel framing
- [`templates/value_hypothesis.md`](../templates/value_hypothesis.md) — fill-in template
- [`playbooks/value_hypothesis_critique.md`](../playbooks/value_hypothesis_critique.md) — how to run a founders' feedback meeting

## Agent partner

- `/ent-value-hypothesis-builder` — walks you through writing a PMF-grade value hypothesis from your discovery notes; pushes back on vague *whos* and compound *whats*
- `/ent-red-team` — pressure-tests the hypothesis against the strongest arguments against it (best run on a copy of your draft, not the original)
