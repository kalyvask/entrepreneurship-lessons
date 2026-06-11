# CLAUDE.md

Working conventions for this repository — for contributors and for Claude Code sessions opened here.

## What this repo is

A practitioner's library and Claude Code agent partner for the journey from a curious mind to
product-market fit: 8 stages, frameworks, playbooks, templates, rubrics, the `ent-*` skills, and a
stateful venture workspace (`scaffold/`). The full map is in `README.md`. (Counts in this file
defer to `library.yaml` — the manifest is the source of truth.)

## The through-line (when guidance conflicts, this wins)

Every skill, rubric, and eval fixture enforces the same PMF discipline:

- **Desperation, not need** — behavioural markers (pre-pays, built a workaround, raises it
  unprompted, wants it now), never compliments.
- **Behaviour, not opinions** — what people did and paid, not what they said.
- **Narrow, not broad** — a *who* you can name 10 real members of; iterate the who, not the what.
- **Retention and organic pull, not signups** — Sean Ellis ≥ 40% in the narrow who, retention flat
  above zero, organic > 40% of new customers.
- **Learning rate over shipping rate** — pre-registered pass thresholds; make being wrong cheap.

Where the named methodologies give opposite advice at the same moment, `frameworks/conflicts.md`
names the conflict and which side to follow. The tie-breaker is always: **the PMF learnings win.**

## Source of truth and checks

- `library.yaml` is the manifest of every stage, framework, playbook, rubric, template, career doc,
  and skill. Adding or removing content means updating it (and its counts) in the same change — CI
  asserts manifest ↔ filesystem ↔ README parity.
- Before committing, run the gate locally (CI runs the same):

  ```bash
  python tools/manifest.py check     # paths exist, counts agree with the README
  python tools/check_links.py        # internal markdown links resolve
  python tools/check_skills.py       # skill frontmatter valid, no duplicate commands
  python tools/check_state.py        # venture-workspace contract (example + scaffold)
  ```

- `tools/run_evals.py` is the opt-in LLM-judge eval runner (needs `ANTHROPIC_API_KEY`); it is
  deliberately **not** the PR gate. See `evals/README.md`.

## Provenance rules

- **Synthesis only — no verbatim quotations.** Ideas are credited to their originators in
  `SOURCES.md`; the words are this repo's own. A passage that reads as a quote is a bug.
- New material derived from a book, talk, or course gets a `SOURCES.md` row and a short Source
  footer in the file itself.

## Skill conventions

- One folder per skill: `.claude/skills/<name>/SKILL.md`; the folder name must equal the
  frontmatter `name`, and `description` says when the skill triggers.
- State-aware skills follow **read-first → write-back → read-back**, and on cold start route to
  `/ent-intake` (you can't read state that doesn't exist). The founder never hand-edits workspace
  files — the agent keeps the records.
- A rubric/gate score of 2–3 requires a **cited artifact** in the workspace — never a checkbox or a
  self-rating.
- `/ent-career-coach` and `career/` are deliberately **off-spine**: career decisions never read or
  write the venture workspace.
- Skills reference repo files by repo-root-relative path; when installed as a plugin, the same
  files ship with the plugin and resolve under the plugin root (`CLAUDE_PLUGIN_ROOT`).
- Plugin packaging: `.claude-plugin/plugin.json` maps `skills` to `./.claude/skills/` (one source
  of truth for both the clone-and-run and plugin paths), and `.claude-plugin/marketplace.json`
  makes the repo installable via `/plugin marketplace add kalyvask/entrepreneurship-lessons`.
  Releases are tagged and logged in `CHANGELOG.md`; bump the plugin `version` with each release.

## Workspace and the worked example

`scaffold/` is the venture-workspace contract; `examples/example-venture/` (Croplane) is the filled
reference, validated by `tools/check_state.py` in CI. If you change the workspace schema, update
the scaffold, the example, and the validator together — the example is not allowed to drift.

## Misc

- Line endings: git stores LF; Windows checkouts may print CRLF warnings — harmless.
- Push model: small, checked commits straight to `main`; CI must stay green.
