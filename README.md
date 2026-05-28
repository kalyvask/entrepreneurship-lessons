# Lessons on Entrepreneurship

A practitioner's library and Claude Code agent partner for the journey from **a curious mind** to **product-market fit**.

The spine of this repo is **the product-market fit framework** — the vocabulary, the discipline, and the rules of thumb behind the term *product-market fit*. Coined by Andy Rachleff (co-founder of Benchmark Capital and Wealthfront) and refined over decades alongside John Vrionis of Unusual Ventures.

**Sources.** This repo is synthesized entirely from the published books cited throughout (Ries, Blank, Moore, Christensen, Fitzpatrick, Knapp, Grant, Bland/Osterwalder, Cialdini) and from Unusual Ventures' publicly available [Field Guide](https://www.unusual.vc/handbook).

Around that spine, the library layers in the methodologies and texts that make the PMF framework executable in practice:

- **Steve Blank's Customer Development** — the systematic discipline of "getting out of the building"
- **Eric Ries's Lean Startup** — the build-measure-learn loop, validated learning
- **Scott Brady and Brett Jordan's Research Driven Inspiration (RDI)** — for the upstream work of finding an insight worth pursuing
- **The Lean Launchpad methodology** — week-by-week execution, Business Model Canvas, the practical artifacts
- **Rob Fitzpatrick's Mom Test** — how to talk to customers without poisoning the data
- **Geoffrey Moore's Crossing the Chasm** — early-adopter vs. pragmatist dynamics
- **Clayton Christensen's Jobs to Be Done and Disruption Theory** — how to identify problems incumbents structurally can't address
- **Jake Knapp's Design Sprint** — 5-day implementation testing
- **Adam Grant's Think Again** — the rethinking mindset
- **Bland & Osterwalder's Testing Business Ideas** — the experiment library

The result is a single, coherent path from "I have a vague interest in a space" to "I have a market desperate for my product, validated by organic growth."

## What this repo is

Three things in one:

1. **A guide.** A stage-by-stage map from the moment you start exploring an industry to the moment you can confidently claim PMF. Every stage names what to do, what trap to avoid, and what to read.
2. **A reference library.** The frameworks themselves — PMF, Build-Measure-Learn, Customer Development, Value Hypothesis, JTBD, Crossing the Chasm, Disruption Theory, Mom Test, RDI — in tight standalone files you can cite, lend, or come back to in 6 months.
3. **An agent partner.** Thirteen Claude Code skills that work alongside you. Tell it where you are, and it loads the right framework, runs the right playbook, asks the right questions, and pushes back when you're kidding yourself.

## How to use it

### As an entrepreneur

Start at [`stages/00_prepared_mind.md`](stages/00_prepared_mind.md) and walk through the stages in order. The order matters. Skipping ahead — picking a problem before you've earned the right to recognize one, or building before you've found a desperate customer — is the most reliable failure mode.

Each stage points to the frameworks you need (in `frameworks/`), the playbooks that take you through the actual work (in `playbooks/`), and the templates that produce the artifacts (in `templates/`).

### With the Claude Code agent partner

Install the skills:

```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/* ~/.claude/skills/
```

Then open Claude Code in a project directory where you're tracking your venture (a notes folder, a workspace, anything). Tell it what you're working on. The skills auto-load based on what you ask:

- `/ent-stage-router` — "I'm working on [X]. What stage am I in and what should I focus on?"
- `/ent-rdi-coach` — Pick a space and run research-driven inspiration end-to-end
- `/ent-interview-prep` — Prep before a customer conversation
- `/ent-interview-debrief` — Capture and synthesize after
- `/ent-value-hypothesis-builder` — Write a PMF-grade value hypothesis
- `/ent-mvp-scoper` — Decide the smallest thing that tests your leap of faith
- `/ent-pmf-evaluator` — Diagnose whether you have product-market fit
- `/ent-pivot-coach` — Decide if and how to pivot
- `/ent-cold-email` — Write outreach that gets responses
- `/ent-design-partners` — For B2B: identify, qualify, and manage the 2–5 design partners who co-create your MVP
- `/ent-synthesis-coach` — Turn 50 interviews into a thesis
- `/ent-idea-coach` — Convert research into a falsifiable bet
- `/ent-prompt-troubleshoot` — When the AI is giving you slop
- `/ent-red-team` — Pressure-test a hypothesis against the strongest arguments against it

### As a reference for collaborators

The `frameworks/` directory is designed to be lent. If a co-founder, employee, or advisor needs to get up to speed on Customer Development, send them [`frameworks/customer_development.md`](frameworks/customer_development.md). One file. Self-contained.

## The spine — the PMF framework

The PMF framework is built around a few load-bearing claims. Memorize them.

> *"Execution doesn't matter. The success or failure of an information-technology company can almost always be traced to the quality of its product-market fit, not its execution. If the dogs are not eating the dog food, no amount of execution will help."*

> *"The most important variable in a startup is the rate at which you learn."*

> *"Need is irrelevant. Desperation is everything."*

> *"Iterate the *who*. Sometimes the *how*. Never the *what*. Adding features does not make someone desperate."*

> *"Competitors are irrelevant before product-market fit."*

> *"First to product-market fit wins, not first to market."*

The full treatment is in [`frameworks/pmf.md`](frameworks/pmf.md).

## The map

| Stage | What it's for | PMF anchor | Supporting frameworks |
|---|---|---|---|
| **00. Prepared mind** | You don't yet know what problem matters | Insight as prerequisite | RDI |
| **01. Insight & idea selection** | Turn research into a falsifiable bet | The non-consensus insight | Disruption Theory, opportunity rubric |
| **02. Customer discovery** | Find who is desperate for what you'd build | Desperation, not need | Customer Development (Blank), Mom Test (Fitzpatrick) |
| **03. Problem–solution fit** | Confirm a real, hot problem | The desperation markers | Unit economics, JTBD |
| **04. Value hypothesis** | Articulate what / who / how + leap of faith | **The core of the framework** | Business Model Canvas |
| **05. MVP — Build & test** | Smallest thing that proves leap of faith | Three-phase validation | Lean Startup (Ries), Design Sprint (Knapp) |
| **06. PMF measurement** | Are dogs eating the dog food? | Validated value hypothesis with organic growth | Sean Ellis test, retention curves |
| **07. Pivot or persevere** | What changes when things aren't working | Iterate the *who*, not the *what* | Pivot taxonomies, savor the surprise |

After PMF, you're in execution land — a different methodology (Crossing the Chasm, Inside the Tornado), partially covered in [`frameworks/crossing_the_chasm.md`](frameworks/crossing_the_chasm.md).

## The one paragraph version

A startup is a learning machine, not an execution machine. Most fail not because the team executed poorly but because the market did not want the product. **Need is irrelevant; desperation is everything.** Your job before product-market fit is to discover a desperate customer for a specific value hypothesis grounded in a non-consensus insight about a technological or market inflection. You do this by running the cheapest possible experiments — concept tests, implementation tests, and only then an MVP — against a deliberately narrow audience. You measure the rate at which you learn, not the rate at which you ship. When experiments fail you iterate the *who* (sometimes the *how*), almost never the *what*. You hold competitors as irrelevant. You hold market size as someone else's concern. You read behavior, not intent. You will be wrong many times before you are right; the methodology is designed to make being wrong cheap, fast, and educational. Product-market fit means a market is desperate for your product — verified by organic growth, not paid attention. After PMF, you become an execution organization. Before PMF, you do not.

## The vocabulary that matters

Words on this list are used **precisely**. Mixing them up is how teams confuse themselves into failure.

- **Insight** — a non-consensus belief about how a market or technology is changing. Not "the world is going mobile" (consensus). Not "this would be cool" (a wish). An insight you can defend with evidence and surprise informed people with.
- **Leap of faith** — the *one* assumption your business depends on. If it's not true, nothing else matters.
- **Value hypothesis** — *what* you'd build, *who* you'd sell it to, *how* you'd deliver it. Pre-evidence.
- **Growth hypothesis** — how you scale beyond word-of-mouth cost-effectively. **Comes after value, never before.**
- **MVP** — usable product that either tests the leap of faith or gets a customer to pay. Not a video. Not a Figma file. Those are tests, not MVPs.
- **Pivot** — change the *who* (sometimes the *how*). Holds the *what* constant.
- **Restart** — change the *what*. Rarely succeeds.
- **Desperation** — customer behavior: pays with little proof, has tried to build it themselves, frustrated unprompted, wants it now.
- **Need** — customer says they'd like it. Useless on its own.
- **Product-market fit** — a market desperate for your product, validated by organic growth.
- **Early adopter / visionary** — buys on vision, tolerates broken, doesn't need references.
- **Pragmatist / early majority** — buys on references, demands whole product.
- **The chasm** — the structural gap between early adopters and pragmatists.
- **Concept test** — proves people would want it (a video, a landing page, a follow-me-home conversation). Days, not weeks.
- **Implementation test** — proves people would use the specific design (a Figma sprint, a Knapp 5-day sprint).
- **MVP test** — proves the leap of faith and/or generates revenue.

If you read nothing else, read [`stages/04_value_hypothesis.md`](stages/04_value_hypothesis.md) and [`frameworks/pmf.md`](frameworks/pmf.md). Then come back.

## Repo structure

```
stanford-lessons-on-enterpreneurship/
├── README.md
├── stages/
│   ├── 00_prepared_mind.md
│   ├── 01_insight_and_idea.md
│   ├── 02_customer_discovery.md
│   ├── 03_problem_solution_fit.md
│   ├── 04_value_hypothesis.md
│   ├── 05_mvp_build.md
│   ├── 06_pmf_measurement.md
│   └── 07_pivot_or_persevere.md
├── frameworks/
│   ├── pmf.md           ← the spine
│   ├── lean_startup.md
│   ├── customer_development.md
│   ├── rdi.md
│   ├── the_mom_test.md
│   ├── crossing_the_chasm.md
│   ├── jobs_to_be_done.md
│   ├── disruption_theory.md
│   ├── pmf_measurement.md
│   ├── business_model_canvas.md
│   ├── unit_economics.md
│   ├── design_sprint.md
│   └── ai_lifecycle.md
├── playbooks/
│   ├── customer_interview.md
│   ├── cold_email.md
│   ├── synthesis.md
│   ├── run_outreach.md
│   ├── build_industry_primer.md
│   ├── validation_sequence.md
│   ├── mvp_scoping.md
│   ├── pmf_assessment.md
│   └── pivot_decision.md
├── templates/
│   ├── opportunity_rubric.md
│   ├── value_hypothesis.md
│   ├── insight_statement.md
│   ├── problem_statement.md
│   ├── interview_script.md
│   ├── interview_debrief.md
│   ├── pmf_survey.md
│   ├── pivot_memo.md
│   └── industry_primer.md
└── .claude/skills/
    ├── ent-stage-router/SKILL.md
    ├── ent-rdi-coach/SKILL.md
    ├── ent-idea-coach/SKILL.md
    ├── ent-interview-prep/SKILL.md
    ├── ent-interview-debrief/SKILL.md
    ├── ent-value-hypothesis-builder/SKILL.md
    ├── ent-mvp-scoper/SKILL.md
    ├── ent-pmf-evaluator/SKILL.md
    ├── ent-pivot-coach/SKILL.md
    ├── ent-cold-email/SKILL.md
    ├── ent-synthesis-coach/SKILL.md
    ├── ent-red-team/SKILL.md
    └── ent-prompt-troubleshoot/SKILL.md
```

## Books

The published works this repo synthesizes — buy them, read them, internalize them.

### Product–market fit and the search process
- **[The Lean Startup](https://www.amazon.com/s?k=The+Lean+Startup+Eric+Ries)** — Eric Ries (2011). Build-Measure-Learn, validated learning, the original MVP vocabulary.
- **[The Four Steps to the Epiphany](https://www.amazon.com/s?k=Four+Steps+to+the+Epiphany+Steve+Blank)** — Steve Blank (2005). Customer Development methodology; the original "get out of the building."
- **[The Startup Owner's Manual](https://www.amazon.com/s?k=Startup+Owners+Manual+Blank+Dorf)** — Steve Blank and Bob Dorf (2012). The expanded, practitioner version of *Four Steps*.
- **[The Mom Test](https://www.amazon.com/s?k=Mom+Test+Rob+Fitzpatrick)** — Rob Fitzpatrick (2013). How to talk to customers without poisoning the data. 80 pages, the highest signal-to-noise book on this list.
- **[Sprint](https://www.amazon.com/s?k=Sprint+Jake+Knapp)** — Jake Knapp with John Zeratsky and Braden Kowitz (2016). The five-day design sprint methodology.

### Market dynamics and adoption
- **[Crossing the Chasm](https://www.amazon.com/s?k=Crossing+the+Chasm+Geoffrey+Moore)** — Geoffrey A. Moore (3rd edition 2014, originally 1991). Technology adoption lifecycle, the chasm, the whole product.
- **[Inside the Tornado](https://www.amazon.com/s?k=Inside+the+Tornado+Geoffrey+Moore)** — Geoffrey A. Moore (1995). Post-chasm strategy and hypergrowth dynamics.

### Disruption and innovation
- **[The Innovator's Dilemma](https://www.amazon.com/s?k=Innovators+Dilemma+Clayton+Christensen)** — Clayton M. Christensen (1997). Why great companies fail; sustaining vs. disruptive innovation.
- **[The Innovator's Solution](https://www.amazon.com/s?k=Innovators+Solution+Christensen+Raynor)** — Clayton M. Christensen and Michael E. Raynor (2003). RPV framework, JTBD foundations, the practical follow-up.
- **[Competing Against Luck](https://www.amazon.com/s?k=Competing+Against+Luck+Christensen)** — Christensen, Hall, Dillon, Duncan (2016). The accessible treatment of Jobs to Be Done.

### Tools and canvases
- **[Business Model Generation](https://www.amazon.com/s?k=Business+Model+Generation+Osterwalder)** — Alexander Osterwalder and Yves Pigneur (2010). The Business Model Canvas.
- **[Value Proposition Design](https://www.amazon.com/s?k=Value+Proposition+Design+Osterwalder)** — Osterwalder, Pigneur, Bernarda, Smith (2014). The Value Proposition Canvas.
- **[Testing Business Ideas](https://www.amazon.com/s?k=Testing+Business+Ideas+Bland+Osterwalder)** — David Bland and Alex Osterwalder (2019). 44 experiment patterns for validating business hypotheses.

### Mindset and persuasion
- **[Think Again](https://www.amazon.com/s?k=Think+Again+Adam+Grant)** — Adam Grant (2021). The rethinking discipline; scout vs. preacher mindset.
- **[Influence: The Psychology of Persuasion](https://www.amazon.com/s?k=Influence+Cialdini)** — Robert Cialdini (new and expanded edition 2021, originally 1984). The foundational text on persuasion.

### Beyond the books
- **[Unusual Field Guide](https://www.unusual.vc/handbook)** — John Vrionis and the Unusual Ventures team. Publicly available; the source of the Design Partners framework in this repo, plus deep treatments of value hypothesis, customer discovery, and MVP measurement.

## Status

Living document. PRs and issues welcome.
