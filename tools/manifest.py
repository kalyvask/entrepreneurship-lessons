#!/usr/bin/env python3
"""Validate library.yaml against the filesystem and the README counts.

library.yaml is the single source of truth for what the library contains. This
check is what prevents drift (e.g. the README claiming 10 playbooks when there
are 11).

Usage:
  python tools/manifest.py check       # CI gate: every path exists, counts agree
  python tools/manifest.py counts      # print counts by kind
"""
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("pyyaml required: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "library.yaml")
README = os.path.join(ROOT, "README.md")

# kind -> (directory, is the artifact a folder?)
KIND_DIRS = {
    "stage": ("stages", False),
    "framework": ("frameworks", False),
    "playbook": ("playbooks", False),
    "rubric": ("rubrics", False),
    "template": ("templates", False),
    "skill": (".claude/skills", True),
}

# README count claims -> kind
README_CLAIMS = {
    "framework": r"frameworks/\s*\((\d+) reference docs\)",
    "playbook": r"playbooks/\s*\((\d+) operational how-tos\)",
    "template": r"templates/\s*\((\d+) fillable artifacts\)",
    "skill": r"\.claude/skills/\s*\((\d+) Claude Code skills\)",
}


def load():
    with open(MANIFEST, encoding="utf-8") as f:
        return yaml.safe_load(f)


def counts_by_kind(data):
    counts = {}
    for a in data.get("artifacts", []):
        counts[a.get("kind")] = counts.get(a.get("kind"), 0) + 1
    return counts


def check():
    data = load()
    errors = []
    seen_ids = set()

    for a in data.get("artifacts", []):
        aid, path, kind = a.get("id"), a.get("path"), a.get("kind")
        if not (aid and path and kind):
            errors.append(f"artifact missing id/path/kind: {a!r}")
            continue
        if aid in seen_ids:
            errors.append(f"duplicate id: {aid}")
        seen_ids.add(aid)
        if not os.path.exists(os.path.join(ROOT, path)):
            errors.append(f"path does not exist: {path} (id {aid})")
        if kind == "skill":
            folder = os.path.basename(os.path.dirname(path))
            if a.get("command") != "/" + folder:
                errors.append(f"skill {aid}: command {a.get('command')!r} != /{folder}")

    counts = counts_by_kind(data)

    # declared counts: map agreement
    for kind, n in counts.items():
        key = (kind or "") + "s"
        declared = data.get("counts", {})
        if key in declared and declared[key] != n:
            errors.append(f"counts.{key}={declared[key]} but artifacts list {n}")

    # filesystem agreement
    for kind, (d, is_dir) in KIND_DIRS.items():
        dpath = os.path.join(ROOT, d)
        if not os.path.isdir(dpath):
            errors.append(f"missing directory: {d}")
            continue
        if is_dir:
            disk = len([x for x in os.listdir(dpath) if os.path.isdir(os.path.join(dpath, x))])
        else:
            disk = len([x for x in os.listdir(dpath) if x.endswith(".md")])
        if disk != counts.get(kind, 0):
            errors.append(f"{d}: {disk} on disk but {counts.get(kind, 0)} in manifest")

    # README count claims
    if os.path.exists(README):
        txt = open(README, encoding="utf-8").read()
        for kind, pat in README_CLAIMS.items():
            m = re.search(pat, txt)
            if m and int(m.group(1)) != counts.get(kind, 0):
                errors.append(
                    f"README claims {m.group(1)} {kind}s but manifest has {counts.get(kind, 0)}"
                )

    if errors:
        print("MANIFEST CHECK FAILED:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("manifest OK: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))


def counts_cmd():
    for k, v in sorted(counts_by_kind(load()).items()):
        print(f"{k}: {v}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    {"check": check, "counts": counts_cmd}.get(mode, check)()
