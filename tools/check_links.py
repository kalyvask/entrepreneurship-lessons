#!/usr/bin/env python3
"""Check that internal Markdown links resolve to real files in the repo.

Only local links are checked; http(s)/mailto and pure anchors are skipped.
Exits non-zero if any internal link is broken.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def is_external(target):
    return target.startswith(("http://", "https://", "mailto:", "#", "tel:"))


def main():
    md_files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                md_files.append(os.path.join(dirpath, fn))

    total = 0
    broken = []
    for f in md_files:
        base = os.path.dirname(f)
        text = open(f, encoding="utf-8").read()
        for m in LINK.finditer(text):
            target = m.group(1).strip()
            if not target or is_external(target):
                continue
            path = target.split("#", 1)[0]
            if not path:  # was a pure anchor
                continue
            total += 1
            full = os.path.normpath(os.path.join(base, path))
            if not os.path.exists(full):
                broken.append((os.path.relpath(f, ROOT), target))

    print(f"internal markdown links checked: {total}")
    if broken:
        print(f"BROKEN ({len(broken)}):")
        for f, t in broken:
            print(f"  {f} -> {t}")
        sys.exit(1)
    print("0 broken")


if __name__ == "__main__":
    main()
