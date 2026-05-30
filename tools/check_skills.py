#!/usr/bin/env python3
"""Validate skill frontmatter and detect duplicate skill commands.

Each .claude/skills/<name>/SKILL.md must have YAML frontmatter with a `name`
(matching the folder) and a `description`. Duplicate names (= duplicate slash
commands) fail the check.
"""
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("pyyaml required: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, ".claude", "skills")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def main():
    if not os.path.isdir(SKILLS):
        sys.exit("no .claude/skills directory")

    errors = []
    seen_names = {}
    folders = sorted(d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d)))

    for d in folders:
        skill_md = os.path.join(SKILLS, d, "SKILL.md")
        if not os.path.exists(skill_md):
            errors.append(f"{d}: missing SKILL.md")
            continue
        text = open(skill_md, encoding="utf-8").read()
        m = FRONTMATTER.match(text)
        if not m:
            errors.append(f"{d}: missing YAML frontmatter")
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            errors.append(f"{d}: invalid frontmatter YAML ({e})")
            continue
        name = fm.get("name")
        if not name:
            errors.append(f"{d}: frontmatter missing 'name'")
        elif name != d:
            errors.append(f"{d}: frontmatter name '{name}' != folder '{d}'")
        if not fm.get("description"):
            errors.append(f"{d}: frontmatter missing 'description'")
        if name:
            if name in seen_names:
                errors.append(f"duplicate skill command: /{name}")
            seen_names[name] = True

    if errors:
        print("SKILL CHECK FAILED:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"skills OK: {len(folders)} skills, no duplicate commands")


if __name__ == "__main__":
    main()
