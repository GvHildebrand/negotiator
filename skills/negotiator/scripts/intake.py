#!/usr/bin/env python3
"""Matter intake and integrity verification for the negotiator skill.

Copies source documents into a read-only, hash-stamped intake folder, scaffolds
the matter, and creates the working branch. Also verifies that source has not
drifted.

This is deterministic on purpose. Hashing and copying are not model judgment.

    intake.py new    <workspace> <slug> <file> [<file> ...]
    intake.py verify <matter-dir>
"""

import hashlib
import os
import shutil
import stat
import subprocess
import sys
from datetime import date
from pathlib import Path

STAGES = [
    "01_intake/source",
    "01_intake/output",
    "02_exposure/output",
    "03_redline/output",
    "04_review_gate",
    "05_rounds/output",
]

MANIFEST = "MANIFEST.md"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def read_only(path: Path) -> None:
    """Strip every write bit. Owner, group, other."""
    mode = path.stat().st_mode
    path.chmod(mode & ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH)


def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True,
    )


def parse_manifest(manifest: Path) -> dict[str, str]:
    """Recover {filename: sha256} from the manifest table."""
    entries: dict[str, str] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[1].startswith("`") and len(cells[1]) == 66:
            entries[cells[0].strip("`")] = cells[1].strip("`")
    return entries


def cmd_new(workspace: str, slug: str, files: list[str]) -> int:
    ws = Path(workspace).expanduser().resolve()
    if not ws.is_dir():
        print(f"HALT: workspace not found: {ws}", file=sys.stderr)
        return 1

    sources = [Path(f).expanduser().resolve() for f in files]
    missing = [p for p in sources if not p.is_file()]
    if missing:
        for p in missing:
            print(f"HALT: source not found: {p}", file=sys.stderr)
        return 1

    matter = ws / "matters" / f"{date.today().isoformat()}_{slug}"
    if matter.exists():
        print(f"HALT: matter already exists: {matter}", file=sys.stderr)
        print("Refusing to overwrite. Choose another slug.", file=sys.stderr)
        return 1

    for stage in STAGES:
        (matter / stage).mkdir(parents=True, exist_ok=True)

    # Branch first: if the repo is dirty in a way that blocks us, stop before copying.
    branch = f"matter/{date.today().isoformat()}-{slug}"
    inside = git(ws, "rev-parse", "--is-inside-work-tree")
    if inside.returncode == 0 and inside.stdout.strip() == "true":
        made = git(ws, "checkout", "-b", branch)
        if made.returncode != 0:
            existing = git(ws, "checkout", branch)
            if existing.returncode != 0:
                print(f"WARNING: could not switch to {branch}:", file=sys.stderr)
                print(existing.stderr.strip(), file=sys.stderr)
            else:
                print(f"branch      {branch} (existing)")
        else:
            print(f"branch      {branch} (created)")
    else:
        print(f"WARNING: {ws} is not a git repository — no branch isolation.",
              file=sys.stderr)

    dest_dir = matter / "01_intake" / "source"
    rows = []
    for src in sources:
        dest = dest_dir / src.name
        if dest.exists():
            print(f"HALT: duplicate filename in intake: {src.name}", file=sys.stderr)
            return 1
        shutil.copy2(src, dest)
        digest = sha256(dest)
        if digest != sha256(src):
            print(f"HALT: copy mismatch for {src.name}", file=sys.stderr)
            return 1
        rows.append((src.name, digest, dest.stat().st_size, str(src)))
        read_only(dest)

    lines = [
        "# Source manifest — READ ONLY",
        "",
        "These files are the originals as received. They are never edited, never",
        "regenerated, and never overwritten. All work happens on copies elsewhere",
        "in this matter. Any drift in these hashes is a HALT condition.",
        "",
        f"**Sealed:** {date.today().isoformat()}",
        "",
        "| File | SHA-256 | Bytes | Origin |",
        "|---|---|---|---|",
    ]
    for name, digest, size, origin in rows:
        lines.append(f"| `{name}` | `{digest}` | {size} | `{origin}` |")
    lines.append("")
    lines.append("Verify with: `intake.py verify <matter-dir>`")
    lines.append("")

    manifest = dest_dir / MANIFEST
    manifest.write_text("\n".join(lines), encoding="utf-8")
    read_only(manifest)
    read_only(dest_dir)

    print(f"matter      {matter}")
    print(f"sealed      {len(rows)} file(s), read-only")
    print("next        fill CONTEXT.md — parties, side, value, BATNA, walk-away")
    return 0


def cmd_verify(matter_dir: str) -> int:
    matter = Path(matter_dir).expanduser().resolve()
    source = matter / "01_intake" / "source"
    manifest = source / MANIFEST

    if not manifest.is_file():
        print(f"HALT: no manifest at {manifest}", file=sys.stderr)
        return 2

    expected = parse_manifest(manifest)
    if not expected:
        print("HALT: manifest contains no entries", file=sys.stderr)
        return 2

    problems = []
    for name, digest in expected.items():
        path = source / name
        if not path.is_file():
            problems.append(f"MISSING  {name}")
            continue
        actual = sha256(path)
        if actual != digest:
            problems.append(f"MODIFIED {name}\n           expected {digest}\n           actual   {actual}")

    known = set(expected) | {MANIFEST}
    for path in sorted(source.iterdir()):
        if path.name not in known:
            problems.append(f"UNTRACKED {path.name} — added to source after sealing")

    if problems:
        print("HALT — SOURCE INTEGRITY FAILED", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        print("\nDo not sign off. Do not deliver. Restore the originals.", file=sys.stderr)
        return 2

    print(f"OK — {len(expected)} source file(s) intact and unmodified")
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 1
    cmd = sys.argv[1]
    if cmd == "new" and len(sys.argv) >= 5:
        return cmd_new(sys.argv[2], sys.argv[3], sys.argv[4:])
    if cmd == "verify" and len(sys.argv) == 3:
        return cmd_verify(sys.argv[2])
    print(__doc__, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
