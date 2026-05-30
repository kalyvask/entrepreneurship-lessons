# Contributing

PRs and issues welcome. This is a synthesis-and-practice library; the bar is accuracy,
attribution, and the PMF discipline.

## Before you open a PR

- If you add, remove, or rename a stage / framework / playbook / template / rubric / skill,
  update **`library.yaml`** — it is the source of truth, and the README counts and CI are
  checked against it.
- Run the checks locally:
  ```bash
  pip install pyyaml
  python tools/manifest.py check
  python tools/check_links.py
  python tools/check_skills.py
  ```
- New skills: the folder name must equal the frontmatter `name`, and `description` is
  required (it's how the skill is triggered).
- Cite your sources. In `SOURCES.md`, mark new material as a **quotation**, **synthesis**, or
  **original adaptation**, and attribute quotations at the point of use.

## House style

- Plain and concrete. Behaviour over opinions. No vanity metrics presented as progress.
- Keep the founder from being overwhelmed: the next one or two steps, not the whole library.
- When sources disagree, the **PMF learnings win** — see `frameworks/conflicts.md`.

## What CI runs

On every pull request: the three Python checks above (the gate), plus markdown-lint and a
spellcheck (advisory, non-blocking).
