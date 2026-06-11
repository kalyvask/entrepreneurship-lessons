# Changelog

Notable changes to this repository. Versions follow [semver](https://semver.org); the plugin
version in `.claude-plugin/plugin.json` tracks these releases.

## [Unreleased]

## [0.1.0] — 2026-06-01

First versioned release: the library productized into a stateful journey engine.

### Added

- **The journey**: 8 stages (00 prepared mind → 07 pivot-or-persevere), 21 frameworks, 12
  playbooks, 14 templates, and evidence-gated journey rubrics (a gate score of 2–3 requires a
  cited artifact).
- **The venture workspace** (`scaffold/`): `founder-state.yaml`, leap-of-faith ledger,
  `interviews.csv`, experiment log, rubric scores, PMF dashboard, decision dossier — written and
  maintained by the agent, never hand-filled. Filled end-to-end example in
  `examples/example-venture/` (Croplane), plus an illustrative session transcript in
  `examples/example-session.md`.
- **25 coaching skills**, uniform contract: read state first → conversational coaching →
  automatic write-back → plain-English read-back; cold start routes to `/ent-intake` (the
  placement interview). Includes the stage router, PMF evaluator, pivot coach (with death-pivot
  watch), red team (auto-fired before the 06→07 gate), verification-first diligence, and the
  cross-venture thesis ledger (`/ent-thesis`) — the journey's endgame: PMF insights, an
  investment-style memo, and a value-hypothesis stance.
- **Off-spine career layer**: `career/career_strategy.md` + `/ent-career-coach`, deliberately
  separate from the venture journey.
- **A point of view**: `frameworks/conflicts.md` (where the methodologies disagree and which
  wins — the PMF learnings break ties) and `frameworks/judgment_and_pareto.md`.
- **Integrity infrastructure**: `library.yaml` manifest as the source of truth; CI gate
  (`tools/manifest.py`, `check_links.py`, `check_skills.py`, `check_state.py`); 13 behavioural
  eval fixtures with an opt-in LLM-judge runner (`tools/run_evals.py`, weekly workflow).
- **Provenance**: MIT `LICENSE`, `NOTICE`, `SOURCES.md` — synthesis only, no verbatim text,
  sources credited at the idea level (Rachleff/Unusual PMF framework, Blank, Ries, Moore,
  Christensen, Fitzpatrick, Knapp, Brady & Jordan's RDI, Diego Oppenheimer's Applied-AI material,
  Garry Tan's gstack under MIT).
- **Plugin packaging**: installable via `/plugin marketplace add kalyvask/entrepreneurship-lessons`
  then `/plugin install entrepreneurship-lessons@kalyvask`; `plugin.json` maps skills from
  `.claude/skills/` so the clone-and-run and plugin paths share one source of truth.
