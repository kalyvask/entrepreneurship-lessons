# Stanford Lessons on Entrepreneurship

A practitioner's library and Claude Code agent partner for the journey from **a curious mind** to **product-market fit**.

Distilled from Stanford GSB's entrepreneurship coursework — Andy Rachleff and John Vrionis's STRAMGT 514 (Product-Market Fit), Steve Blank and Mar Hershenson's ENG 245 (Lean Launchpad), Scott Brady and Brett Jordan's STRAMGT 546 (Research Driven Inspiration), and the MKTG 535 Product Launch case method — plus the foundational texts the courses assign: *The Lean Startup* (Ries), *The Four Steps to the Epiphany* (Blank), *Crossing the Chasm* (Moore), *The Innovator's Solution* (Christensen), *The Mom Test* (Fitzpatrick), *Sprint* (Knapp), *Think Again* (Grant), and *Testing Business Ideas* (Bland/Osterwalder).

This is not class notes. It is a working library plus an agent that helps you execute.

## What this repo is

Three things in one:

1. **A guide.** A stage-by-stage map from the moment you start exploring an industry to the moment you can confidently say "we have product-market fit." Every stage names what to do, what trap to avoid, and what to read.
2. **A reference library.** The frameworks themselves — Build-Measure-Learn, Customer Development, Value Hypothesis, JTBD, Crossing the Chasm, Disruption Theory, Mom Test — in tight standalone files you can cite, lend, or come back to in 6 months.
3. **An agent partner.** Twelve Claude Code skills that work alongside you. Tell it where you are, and it loads the right framework, runs the right playbook, asks the right questions, and pushes back when you're kidding yourself.

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

Then open Claude Code in a project directory where you're tracking your venture (a notes folder, a workspace, anything). Tell it what you're working on. The skills auto-load based on the stage you're in:

- `/ent-stage-router` — "I'm working on [X]. What stage am I in and what should I focus on?"
- `/ent-rdi-coach` — Pick a space and run the RDI methodology
- `/ent-interview-prep` — Prep before a customer conversation
- `/ent-interview-debrief` — Capture and synthesize after
- `/ent-value-hypothesis-builder` — Write a Rachleff-grade value hypothesis
- `/ent-mvp-scoper` — Decide the smallest thing that tests your leap of faith
- `/ent-pmf-evaluator` — Diagnose whether you have product-market fit (and you almost certainly don't)
- `/ent-pivot-coach` — Decide if and how to pivot
- `/ent-cold-email` — Write outreach that gets responses
- `/ent-synthesis-coach` — Turn 50 interviews into a thesis
- `/ent-prompt-troubleshoot` — When the AI is giving you slop
- `/ent-red-team` — Pressure-test a hypothesis against the strongest arguments against it

### As a reference for collaborators

The `frameworks/` directory is designed to be lent. If a co-founder, employee, or advisor needs to get up to speed on Customer Development, send them [`frameworks/customer_development.md`](frameworks/customer_development.md). One file. Self-contained.

## The map

| Stage | What it's for | Anchor |
|---|---|---|
| **00. Prepared mind** | You don't yet know what problem matters | RDI |
| **01. Insight & idea selection** | Turn research into a falsifiable bet | Inflection points + opportunity rubric |
| **02. Customer discovery** | Find who is desperate for what you'd build | Mom Test, customer development |
| **03. Problem–solution fit** | Confirm you've found a real, hot problem | Rachleff's "desperation" markers |
| **04. Value hypothesis** | Articulate what / who / how + leap of faith | Rachleff value hypothesis |
| **05. MVP — Build & test** | Smallest thing that proves leap of faith | Lean Startup MVP |
| **06. Validate** | Three-phase: concept → implementation → MVP | Rachleff validation sequence |
| **07. PMF measurement** | Are dogs eating the dog food? | Sean Ellis test, organic growth, retention |
| **08. Pivot or persevere** | What changes when things aren't working | Iterate the *who*, not the *what* |

After PMF, you're in execution land — that's a different methodology (Crossing the Chasm, Inside the Tornado), partially covered in [`frameworks/crossing_the_chasm.md`](frameworks/crossing_the_chasm.md).

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

If you read nothing else, read [`stages/04_value_hypothesis.md`](stages/04_value_hypothesis.md) and [`frameworks/rachleff_pmf.md`](frameworks/rachleff_pmf.md). Then come back.

## Acknowledgments and attribution

The substance here is not original. It is synthesized from:

- **Stanford STRAMGT 514** — Product-Market Fit (Andy Rachleff, John Vrionis)
- **Stanford ENG 245** — Lean Launchpad (Steve Blank, Mar Hershenson, lecturers including Jeff Epstein, George John, and others)
- **Stanford STRAMGT 546** — Research Driven Inspiration (Scott Brady, Brett Jordan)
- **Stanford MKTG 535** — Product Launch (Jonathan Levav, Sarah Tavel and others)
- **Texts:** *The Lean Startup* (Ries), *The Four Steps to the Epiphany* (Blank), *Crossing the Chasm* (Moore), *The Innovator's Solution* and *The Innovator's Dilemma* (Christensen), *The Mom Test* (Fitzpatrick), *Sprint* (Knapp), *Think Again* (Grant), *Testing Business Ideas* (Bland/Osterwalder), *Influence* (Cialdini)

The synthesis is mine — Alex Kalyvas. Errors are mine; the underlying ideas belong to the people listed above. Student names, specific case details, and any class-internal material has been stripped or anonymized.

## Status

Living document. Stages 00–08 are written. Frameworks are filling out — see [`frameworks/`](frameworks/) for the current set. The agent partner skills are in [`.claude/skills/`](.claude/skills/).

PRs and issues welcome.
