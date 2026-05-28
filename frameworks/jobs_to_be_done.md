# Jobs to Be Done (Clayton Christensen)

> *"People don't want a quarter-inch drill. They want a quarter-inch hole."* — attributed to Theodore Levitt; central to JTBD

JTBD (Jobs To Be Done) is a way of understanding **what customers are actually hiring a product to do** — independent of demographics, segmentation, or product features. The framework's origin is Harvard professor Clayton Christensen's research on innovation and disruption; the most accessible treatment is *Competing Against Luck* (Christensen et al., 2016).

## The core idea

Traditional marketing segments customers by **who they are**: 25–34, urban, high income, female, etc. JTBD argues this is the wrong unit of analysis.

**The right unit is the situation.** A customer with a specific situation has a specific *job* they're trying to get done. They look around for things to *hire* (products, services, behaviors, workarounds) that can accomplish the job. They pick whichever option seems most likely to get the job done, and if the chosen option fails to deliver, they fire it and hire something else.

**Same person, different jobs.** A 35-year-old marketing manager might hire McKinsey for one job (strategic advice on entering a new market) and hire ChatGPT for another (writing a quick email). She is not "a McKinsey customer" or "a ChatGPT customer" — she has different jobs at different moments, and she hires different solutions for each.

## Three dimensions of any job

Every job has three components, and a great product addresses all three:

### Functional dimension

What needs to happen. The mechanical accomplishment.

*Example: Get to a meeting 25 miles away in 45 minutes.*

This is what feature lists and marketing usually focus on. It's necessary but rarely sufficient.

### Emotional dimension

How the customer wants to feel — about themselves, about the situation, about the choice they're making.

*Example: Get there without feeling stressed. Or: feel competent and professional when I arrive. Or: feel I'm not wasting time during the commute.*

The emotional dimension is what makes a customer pick one functional-equivalent option over another. Two products that solve the same functional job will lose to whichever one better addresses the emotional dimension.

### Social dimension

How the customer wants others to perceive them.

*Example: arriving in a Tesla signals different things from arriving in a Honda. Both get you there. The job has a social component.*

Underestimated by engineer-founders. Critical in any B2B or consumer product where the customer is also signaling status, taste, sophistication, or membership.

## The milkshake example

Christensen's famous case. A fast-food chain wanted to increase milkshake sales. They asked customers what they wanted: thicker, sweeter, fruitier, less expensive. They built variants. Sales didn't move.

A JTBD researcher watched the actual buying behavior. Two distinct customer groups, hiring milkshakes for two completely different jobs:

**Morning commuter.** Long drive to work. Hands-free, durable food. Doesn't make a mess. Lasts the whole drive. Slightly satisfying. Job: *"Help me get through a boring drive without being hungry and without having to think about food."* What it competes with: bagels, donuts, candy bars, bananas. What it should be: thicker (lasts longer), small chunks of fruit (something to look forward to), drive-through optimized (fast handoff).

**Afternoon dad-with-kid.** Reward at the end of a long day. Quick treat for a child who was good at the doctor. Job: *"Help me bond with my kid by giving them a treat without committing to a whole meal."* What it competes with: candy, soft serve, cookies, a small toy. What it should be: smaller, less filling, sweeter, faster to drink.

**Same product. Same customer demographics.** Different jobs. Different situations. Different competitors.

The lesson: **demographic segmentation hides the real structure of demand.** Job-based segmentation reveals it.

## What this means for a startup

Two practical implications.

### When you're discovering your customer

Don't ask "who is this for?" Ask "what job is this hired to do?" Then ask "in what situation does someone have this job?"

This reframes customer discovery away from demographic personas and toward observed behavior in specific contexts. Instead of "marketing managers at SaaS companies," you're looking for "marketing managers in their first 90 days at a SaaS company that just raised Series B, trying to demonstrate quick wins to the new VP."

The shift is from broad to specific, from generic to situational. (Compatible with Rachleff's narrowing discipline — see [`frameworks/pmf.md`](pmf.md).)

### When you're identifying competition

JTBD's most useful move: it broadens your view of what you compete with.

A milkshake's competition is not "other milkshakes." For the morning commuter, it competes with bagels, energy bars, and the option of just not eating. For the dad, it competes with candy and toys.

A B2B SaaS tool's competition is not "other SaaS tools in the category." It also competes with spreadsheets, doing nothing, hiring a contractor, building in-house, asking another team for help.

When you're testing a value hypothesis, **list every option a customer has for getting the job done — including doing nothing.** If your product is competing against "doing nothing" — and the customer mostly chooses to do nothing — your product isn't a hire-worthy solution to a hire-worthy job.

## The forces of progress

A model for diagnosing why customers do (or don't) switch.

For a customer to switch from their current solution to yours, **four forces** are in play:

**Forces pulling them TOWARD your product:**
1. **The push of the situation** — their current solution is failing them; the pain is acute.
2. **The pull of the new solution** — your product's promise is compelling.

**Forces pulling them AWAY from your product:**
3. **The anxieties about the new solution** — fear it won't work, fear of the switching cost, fear of looking bad if it fails.
4. **The habits of the present** — inertia, sunk cost, "we've always done it this way."

For a switch to happen, **the pulls must outweigh the resistances.** Many products solve the functional problem better (pull 2 is strong) but die because they don't address the anxieties (resistance 3) or fight the habit (resistance 4).

For a startup, this means: a great product alone is rarely enough. You need to actively neutralize the anxieties (free trial, money-back guarantee, references, hand-holding) and overcome the habit (active onboarding, change management for B2B). Otherwise customers will say "yes I'd love that" and never actually switch.

## Where JTBD fits with other frameworks

- **vs Rachleff's *who*:** JTBD answers the *who* with situational specificity. A great *who* is a "job + situation," not a demographic.
- **vs Mom Test:** JTBD reframes interview questions. Instead of *"would you use a tool that does X?"*, you ask *"the last time you had to get X done, walk me through what you did and what you wished you had."* (See [`frameworks/the_mom_test.md`](the_mom_test.md).)
- **vs Disruption Theory:** the JTBD lens identifies *underserved jobs* — jobs being done badly by current providers, where a simpler, cheaper, more convenient alternative can win. (See [`frameworks/disruption_theory.md`](disruption_theory.md).)
- **vs Lean Startup:** JTBD sharpens the value hypothesis. The leap of faith is about whether a job exists in the form you've hypothesized. (See [`frameworks/lean_startup.md`](lean_startup.md).)

## A worked example

Hypothetical: a startup building "a project management tool for software teams."

**Without JTBD framing:**
- Customer: engineering managers at 50–500 person SaaS companies
- Problem: their existing tool (Asana / Linear / Jira) is slow and clunky
- Value prop: faster, prettier, modern UX

This is generic, hard to test, and difficult to position against the dozens of "project management tool" alternatives.

**With JTBD framing:**

Discovery interviews reveal two distinct jobs:

- **Job 1.** *"When my team's planning a new feature and I have 30 minutes before standup, help me see exactly who owns what and what's at risk so I can show up to standup confident I won't be surprised."* Situation: ICs preparing for standups. Job: anxiety mitigation through visibility.
- **Job 2.** *"When leadership asks for a roadmap update mid-quarter, help me put together a story I can ship to the CEO in an hour that doesn't make me look unprepared."* Situation: managers preparing exec updates. Job: status reporting + reputational protection.

Two jobs, one customer (the same engineering manager), two situations. Each suggests a *different* product:

- Job 1 → a fast, IC-facing, real-time view of who-owns-what-and-when. Competes with Slack, status meetings, "asking on standup."
- Job 2 → an upward-facing reporting tool. Competes with PowerPoint, manual spreadsheets, hiring a chief of staff.

The startup might do well to pick **one** of these jobs and crush it before broadening. (Bowling pin: see [`frameworks/crossing_the_chasm.md`](crossing_the_chasm.md).) Both is too much to build.

This is the JTBD payoff: **the structure of the demand becomes visible.**

## Where this lives in the journey

- [Stage 02 — Customer Discovery](../stages/02_customer_discovery.md) — use JTBD to structure interviews around situations
- [Stage 03 — Problem-Solution Fit](../stages/03_problem_solution_fit.md) — name the job in your problem statement
- [Stage 04 — Value Hypothesis](../stages/04_value_hypothesis.md) — narrow the *who* via job + situation rather than demographics

## Source

- *Competing Against Luck* — Clayton M. Christensen, Taddy Hall, Karen Dillon, David S. Duncan (2016). Most accessible introduction.
- *The Innovator's Solution* — Christensen and Raynor (2003). Original treatment in the disruption context.
- Tony Ulwick's *outcome-driven innovation* — a related, more quantitative variant.
- *Jobs to Be Done: Theory to Practice* — Anthony W. Ulwick.
