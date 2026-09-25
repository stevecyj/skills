# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Link every skill in .agents/skills into .claude/skills when Claude Code is installed.

The source of truth is always <project>/.agents/skills/<name>. When Claude Code is
installed on this machine (CLAUDE_CONFIG_DIR or ~/.claude exists), each skill gets a
relative symlink at <project>/.claude/skills/<name>. Real directories and symlinks that
point elsewhere are never modified; they are reported instead.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

SOURCE_RELATIVE = Path(".agents") / "skills"
LINKS_RELATIVE = Path(".claude") / "skills"


def claude_config_dir() -> Path:
    configured = os.environ.get("CLAUDE_CONFIG_DIR", "").strip()
    return Path(configured).expanduser() if configured else Path.home() / ".claude"


def is_inside(path: Path, directory: Path) -> bool:
    try:
        path.relative_to(directory)
    except ValueError:
        return False
    return True


def raw_link_target(link: Path) -> Path:
    """Absolute, normalized target of a symlink, without requiring the target to exist."""
    target = Path(os.readlink(link))
    if not target.is_absolute():
        target = link.parent / target
    return Path(os.path.normpath(target))


def has_sop(skill_dir: Path) -> bool:
    skill_md = skill_dir / "SKILL.md"
    try:
        lines = skill_md.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return False
    return any(line.strip() == "# SOP" for line in lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Sync relative symlinks from <project>/.claude/skills/<name> to <project>/.agents/skills/<name> "
            "when Claude Code is installed (CLAUDE_CONFIG_DIR or ~/.claude exists). Prints a JSON report."
        )
    )
    parser.add_argument("--project-root", type=Path, required=True, help="Project root that holds .agents/skills.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report only; change nothing. Exit 1 when links are missing or dangling.",
    )
    args = parser.parse_args()

    root: Path = args.project_root.expanduser().resolve()
    if not root.is_dir():
        print(f"{root}: project root is not a directory", file=sys.stderr)
        return 2

    config_dir = claude_config_dir()
    report: dict = {
        "claude_code": "installed" if config_dir.is_dir() else "not_installed",
        "claude_config_dir": config_dir.as_posix(),
        "skills_dir_created": False,
        "created": [],
        "ok": [],
        "removed": [],
        "coexisting": [],
        "conflicts": [],
        "migration_suggestions": [],
        "missing": [],
        "dangling": [],
    }
    sys.stdout.reconfigure(encoding="utf-8")
    if report["claude_code"] == "not_installed":
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    source_dir = root / SOURCE_RELATIVE
    links_dir = root / LINKS_RELATIVE
    skills = (
        sorted(entry.name for entry in source_dir.iterdir() if entry.is_dir() and (entry / "SKILL.md").is_file())
        if source_dir.is_dir()
        else []
    )

    try:
        if not links_dir.is_dir():
            if args.check:
                report["missing"].extend(skills)
                print(json.dumps(report, ensure_ascii=False, indent=2))
                return 1 if skills else 0
            links_dir.mkdir(parents=True)
            report["skills_dir_created"] = True

        for name in skills:
            link = links_dir / name
            source = source_dir / name
            if link.is_symlink():
                if raw_link_target(link) == Path(os.path.normpath(source)):
                    report["ok"].append(name)
                else:
                    report["conflicts"].append({"name": name, "target": os.readlink(link)})
            elif link.exists():
                report["coexisting"].append(name)
            elif args.check:
                report["missing"].append(name)
            else:
                os.symlink(os.path.relpath(source, links_dir), link, target_is_directory=True)
                report["created"].append(name)

        source_norm = Path(os.path.normpath(source_dir))
        for entry in sorted(links_dir.iterdir(), key=lambda path: path.name):
            if entry.is_symlink():
                target = raw_link_target(entry)
                if not target.exists() and is_inside(target, source_norm):
                    if args.check:
                        report["dangling"].append(entry.name)
                    else:
                        entry.unlink()
                        report["removed"].append(entry.name)
            elif entry.is_dir() and entry.name not in skills and has_sop(entry):
                report["migration_suggestions"].append(entry.name)
    except OSError as error:
        print(f"cannot sync skill links: {error}", file=sys.stderr)
        return 1

    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.check and (report["missing"] or report["dangling"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
