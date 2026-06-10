# Lessons on Entrepreneurship

A practitioner's library and Claude Code agent partner for the journey from **a curious mind** to **product-market fit**.

The spine of this repo is **the product-market fit framework** — the vocabulary, the discipline, and the rules of thumb behind the term *product-market fit*. Coined by Andy Rachleff (co-founder of Benchmark Capital and Wealthfront) and refined over decades also with John Vrionis of Unusual Ventures.

**Sources.** This repo is synthesized entirely from the published books cited throughout (Ries, Blank, Moore, Christensen, Fitzpatrick, Knapp, Grant, Bland/Osterwalder, Cialdini) and from Unusual Ventures' publicly available [Field Guide](https://www.unusual.vc/handbook). Full provenance — every entry a synthesis or adaptation in this repo's own words, never verbatim text — is in [`SOURCES.md`](SOURCES.md).

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
- **Diego Oppenheimer's Applied AI for the company lifecycle** — using AI as a research and build partner at each stage, and the prompting discipline that separates leverage from slop

The result is a single, coherent path from "I have a vague interest in a space" to "I have a market desperate for my product, validated by organic growth."

## What this repo is

Four things in one:

1. **A guide.** A stage-by-stage map from the moment you start exploring an industry to the moment you can confidently claim PMF. Every stage names what to do, what trap to avoid, and what to read — and a scorable **rubric** so you can honestly grade whether the stage is actually done.
2. **A reference library.** The frameworks themselves — PMF, Build-Measure-Learn, Customer Development, Value Hypothesis, JTBD, Crossing the Chasm, Disruption Theory, Market Type, Mom Test, RDI, Design Partners, Value Dimensions, Ideation Templates, the 10-Star Product — plus a map of [where they disagree](frameworks/conflicts.md). In tight standalone files you can cite, lend, or come back to in 6 months.
3. **An agent partner.** Twenty-five Claude Code skills that work alongside you. Tell it where you are, and it loads the right framework, runs the right playbook, asks the right questions, grades you against the rubric, and pushes back when you're kidding yourself.
4. **A venture workspace.** A small set of state files ([`scaffold/`](scaffold/)) so the agent picks up where you left off instead of re-diagnosing you every session — and so a stage only advances on evidence, not a checked box. You start by running `/ent-intake` (an interview that writes the state for you); every skill reads this state first and, if it doesn't exist yet, sends you to `/ent-intake` before anything else.

The destination is not PMF itself but three synthesized outputs you carry beyond the venture — your **PMF insights**, your **investment / founder-style memo**, and your **value-hypothesis stance** — built by `/ent-thesis` into `thesis_ledger.md`. The per-venture journey feeds that cross-venture thesis.

## How to use it

### As an entrepreneur

Start at [`stages/00_prepared_mind.md`](stages/00_prepared_mind.md) and walk through the stages in order. The order matters. Skipping ahead — picking a problem before you've earned the right to recognize one, or building before you've found a desperate customer — is the most reliable failure mode.

Each stage points to the frameworks you need (in `frameworks/`), the playbooks that take you through the actual work (in `playbooks/`), and the templates that produce the artifacts (in `templates/`).

### With the Claude Code agent partner

The skills reference the frameworks, playbooks, and templates by their path in this repo, so the reliable way to use them is to **run Claude Code inside the cloned repo**:

```bash
git clone https://github.com/kalyvask/entrepreneurship-lessons
cd entrepreneurship-lessons
claude   # skills auto-load from .claude/skills/, and every framework/playbook/template reference resolves
```

To make the coaching skills available from anywhere, install the repo as a plugin:

```
/plugin install github.com/kalyvask/entrepreneurship-lessons
```

The skills then appear as `/entrepreneurship-lessons:ent-…`. The supporting frameworks, playbooks, and templates ship with the plugin: each skill carries a note to resolve its repo-relative file references under the plugin root (`CLAUDE_PLUGIN_ROOT`) when installed that way, so both the in-repo and plugin paths work.

The skills auto-load based on what you ask:

- `/ent-intake` — Start here. The agent interviews you, places you on the 00→07 map, and writes your venture state for you (no file to fill in by hand)
- `/ent-office-hours` — The front door for a raw idea; it reframes the pain, challenges premises, and points you at the narrowest wedge
- `/ent-stage-router` — "I'm working on [X]. What stage am I in and what should I focus on?"
- `/ent-rdi-coach` — Pick a space and run research-driven inspiration end-to-end
- `/ent-interview-prep` — Prep before a customer conversation
- `/ent-interview-debrief` — Capture and synthesize after
- `/ent-value-hypothesis-builder` — Write a PMF-grade value hypothesis
- `/ent-customer-discovery` — Track a discovery sprint; surface patterns; flag needy vs. desperate
- `/ent-problem-statement` — Turn discovery notes into a defensible problem statement
- `/ent-concept-test` — Design a cheap test that proves demand before you build
- `/ent-unit-econ-check` — Back-of-envelope LTV/CAC sanity check
- `/ent-mvp-scoper` — Decide the smallest thing that tests your leap of faith
- `/ent-mvp-review` — Run a two-week product review during the build
- `/ent-design-partners` — For B2B: identify, qualify, and manage the 2–5 design partners who co-create your MVP
- `/ent-pmf-evaluator` — Diagnose whether you have product-market fit
- `/ent-pmf-memo` — Synthesize the whole journey into a shareable 1–2 page PMF memo
- `/ent-pivot-coach` — Decide if and how to pivot
- `/ent-cold-email` — Write outreach that gets responses
- `/ent-synthesis-coach` — Turn 50 interviews into a thesis
- `/ent-idea-coach` — Convert research into a falsifiable bet
- `/ent-prompt-troubleshoot` — When the AI is giving you slop
- `/ent-red-team` — Pressure-test a hypothesis against the strongest arguments against it
- `/ent-diligence` — Verification-first diligence: verify / flag / discard a claim set — your own memo before a sharp reader sees it, or a company you're evaluating
- `/ent-thesis` — Cross-venture layer: log durable learnings and synthesize them into your PMF insights, investment-style memo, and value-hypothesis stance
- `/ent-career-coach` — Off-spine: which job to take, which offer, whether to take a chief-of-staff role, when to leave — for someone aiming at startups. Not part of the venture journey.

### Operate from it — the venture workspace

The library is the knowledge; [`scaffold/`](scaffold/) is the state. Copy it into your venture so the agent works from where you actually are:

```bash
cp -r scaffold my-venture
```

You don't fill these in by hand. Run `/ent-intake` and the agent interviews you — what you're building, what evidence you have — then writes `founder-state.yaml` for you and keeps it current as you work. It holds `founder-state.yaml` (current stage, gate scores, blockers), `lof_ledger.md` (the one leap of faith and its status over time), `interviews.csv` (conversations scored on the four desperation markers), `experiment_log.md`, `rubric_scores.md`, `pmf_dashboard.md`, and a running `decision_dossier.md`. The one rule that makes it work: **a gate score of 2–3 requires a cited artifact in the workspace** — the agent won't advance a stage on an unevidenced claim. A filled, end-to-end example is in [`examples/example-venture/`](examples/example-venture/).

### As a reference for collaborators

The `frameworks/` directory is designed to be lent. If a co-founder, employee, or advisor needs to get up to speed on Customer Development, send them [`frameworks/customer_development.md`](frameworks/customer_development.md). One file. Self-contained.

## The map

| Stage | What it's for | PMF anchor | Supporting frameworks |
|---|---|---|---|
| **00. Prepared mind** | You don't yet know what problem matters | Insight as prerequisite | RDI |
| **01. Insight & idea selection** | Turn research into a falsifiable bet | The non-consensus insight | Disruption Theory, Market Type, opportunity rubric |
| **02. Customer discovery** | Find who is desperate for what you'd build | Desperation, not need | Customer Development (Blank), Mom Test (Fitzpatrick) |
| **03. Problem–solution fit** | Confirm a real, hot problem | The desperation markers | Unit economics, JTBD |
| **04. Value hypothesis** | Articulate what / who / how + leap of faith | **The core of the framework** | Business Model Canvas |
| **05. MVP — Build & test** | Smallest thing that proves leap of faith | Three-phase validation | Lean Startup (Ries), Design Sprint (Knapp) |
| **06. PMF measurement** | Are dogs eating the dog food? | Validated value hypothesis with organic growth | Sean Ellis test, retention curves |
| **07. Pivot or persevere** | What changes when things aren't working | Iterate the *who*, not the *what* | Pivot taxonomies, savor the surprise |

After PMF, you're in execution land — a different methodology (Crossing the Chasm, Inside the Tornado), partially covered in [`frameworks/crossing_the_chasm.md`](frameworks/crossing_the_chasm.md).

## Repo structure

```
entrepreneurship-lessons/
├── README.md
├── LICENSE                  (MIT)
├── NOTICE                   (attribution for adapted material)
├── CLAUDE.md                (working conventions for contributors and Claude Code)
├── SOURCES.md               (provenance: synthesis / adaptation — no verbatim text)
├── CONTRIBUTING.md
├── library.yaml             (machine-readable manifest — source of truth for counts)
├── stages/
│   ├── 00_prepared_mind.md
│   ├── 01_insight_and_idea.md
│   ├── 02_customer_discovery.md
│   ├── 03_problem_solution_fit.md
│   ├── 04_value_hypothesis.md
│   ├── 05_mvp_build.md
│   ├── 06_pmf_measurement.md
│   └── 07_pivot_or_persevere.md
├── frameworks/          (21 reference docs)
│   ├── pmf.md           ← the spine
│   ├── judgment_and_pareto.md   (deciding under uncertainty; 80/20)
│   ├── lean_startup.md
│   ├── customer_development.md
│   ├── rdi.md
│   ├── the_mom_test.md
│   ├── crossing_the_chasm.md
│   ├── market_type.md       (Blank's four market types; positioning)
│   ├── jobs_to_be_done.md
│   ├── disruption_theory.md
│   ├── pmf_measurement.md
│   ├── conflicts.md         (where the methods disagree, and which wins)
│   ├── business_model_canvas.md
│   ├── value_prop_canvas.md
│   ├── value_dimensions.md       (functional / economic / psychological)
│   ├── ideation_templates.md     (breaking functional fixedness)
│   ├── ten_star_product.md       (10-star vision + scope modes)
│   ├── unit_economics.md
│   ├── design_sprint.md
│   ├── design_partners.md
│   └── ai_lifecycle.md
├── playbooks/           (12 operational how-tos)
│   ├── customer_interview.md
│   ├── cold_email.md
│   ├── synthesis.md
│   ├── run_outreach.md
│   ├── build_industry_primer.md
│   ├── concept_test.md
│   ├── validation_sequence.md
│   ├── mvp_scoping.md
│   ├── value_hypothesis_critique.md  (founders' feedback meeting)
│   ├── pmf_assessment.md
│   ├── pivot_decision.md
│   └── diligence.md     (verification-first: verify / flag / discard)
├── rubrics/             (score yourself at every stage)
│   └── journey_rubrics.md        (pass/fail rubric for stages 00–07)
├── templates/           (14 fillable artifacts)
│   ├── self_reflection.md
│   ├── opportunity_rubric.md
│   ├── insight_statement.md
│   ├── problem_statement.md
│   ├── solution_shape.md
│   ├── value_hypothesis.md
│   ├── positioning_statement.md   (market-facing one-liner)
│   ├── interview_script.md
│   ├── interview_debrief.md
│   ├── industry_primer.md
│   ├── pmf_survey.md
│   ├── retention_dashboard.md
│   ├── pmf_memo.md               (the capstone synthesis)
│   └── pivot_memo.md
├── career/              (off-spine — a separate career-strategy layer, not the venture journey)
│   └── career_strategy.md
├── scaffold/            (the venture workspace — copy this into your project)
├── examples/
│   └── example-venture/          (a filled, end-to-end worked journey)
├── evals/               (behavioural fixtures for the skills)
├── tools/               (manifest + link + skill + workspace-state checks, run in CI)
├── .github/workflows/   (content-integrity CI)
├── .claude-plugin/
│   └── plugin.json
└── .claude/skills/      (25 Claude Code skills)
    ├── ent-intake/SKILL.md
    ├── ent-thesis/SKILL.md
    ├── ent-office-hours/SKILL.md
    ├── ent-stage-router/SKILL.md
    ├── ent-pmf-memo/SKILL.md
    ├── ent-rdi-coach/SKILL.md
    ├── ent-idea-coach/SKILL.md
    ├── ent-interview-prep/SKILL.md
    ├── ent-interview-debrief/SKILL.md
    ├── ent-customer-discovery/SKILL.md
    ├── ent-problem-statement/SKILL.md
    ├── ent-concept-test/SKILL.md
    ├── ent-unit-econ-check/SKILL.md
    ├── ent-value-hypothesis-builder/SKILL.md
    ├── ent-mvp-scoper/SKILL.md
    ├── ent-mvp-review/SKILL.md
    ├── ent-design-partners/SKILL.md
    ├── ent-pmf-evaluator/SKILL.md
    ├── ent-pivot-coach/SKILL.md
    ├── ent-cold-email/SKILL.md
    ├── ent-synthesis-coach/SKILL.md
    ├── ent-red-team/SKILL.md
    ├── ent-diligence/SKILL.md
    ├── ent-prompt-troubleshoot/SKILL.md
    └── ent-career-coach/SKILL.md   (off-spine career layer)
```

The counts above are validated against [`library.yaml`](library.yaml) by CI, so they can't quietly drift.

## Integrity, sources & license

- **`library.yaml`** is the machine-readable manifest of every stage, framework, playbook, template, rubric, and skill. It is the source of truth for the counts in this README.
- **CI** (`.github/workflows/content-integrity.yml`) checks the manifest, internal links, skill frontmatter, and the venture-workspace contract on every change. Run the same checks locally with `python tools/manifest.py check && python tools/check_links.py && python tools/check_skills.py && python tools/check_state.py` (needs `pip install pyyaml`).
- **`evals/`** holds behavioural fixtures for the skills (e.g. the stage router must not over-advance; the PMF evaluator must reject weak evidence).
- **`SOURCES.md`** records provenance for every source, tagged synthesis / original adaptation — the repo reproduces no verbatim text. **`NOTICE`** credits adapted, openly licensed material.
- Licensed under the **MIT License** (see [`LICENSE`](LICENSE)).

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

Living document, MIT-licensed (see [`LICENSE`](LICENSE)). PRs and issues welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md).
