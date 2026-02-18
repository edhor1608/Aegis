#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shlex
import subprocess
from pathlib import Path


def default_build_config() -> dict[str, str]:
    return {
        "mode": "debian",
        "distribution": "stable",
        "arch": "amd64",
        "debian_installer": "live",
        "archive_areas": "main contrib non-free-firmware",
    }


def build_commands(cfg: dict[str, str]) -> list[list[str]]:
    return [
        ["lb", "clean", "--purge"],
        [
            "lb",
            "config",
            "noauto",
            "--mode",
            cfg["mode"],
            "--distribution",
            cfg["distribution"],
            "--architectures",
            cfg["arch"],
            "--debian-installer",
            cfg["debian_installer"],
            "--archive-areas",
            cfg["archive_areas"],
            "--apt-indices",
            "false",
            "--apt-recommends",
            "false",
            "--memtest",
            "none",
        ],
        ["lb", "build"],
    ]


def format_commands(commands: list[list[str]]) -> str:
    return "\n".join(" ".join(shlex.quote(part) for part in cmd) for cmd in commands)


def run_commands(commands: list[list[str]], cwd: Path) -> None:
    for command in commands:
        subprocess.run(command, cwd=cwd, check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Senior Zero live-build pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Print commands only")
    parser.add_argument("--execute", action="store_true", help="Run lb commands")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = default_build_config()
    commands = build_commands(cfg)
    root = Path(__file__).resolve().parents[1]
    build_dir = root / "build" / "live-build"

    if args.dry_run or not args.execute:
        print(f"BUILD_DIR: {build_dir}")
        print(format_commands(commands))
        print("VM_READY_INSTRUCTION: after building, boot build/live-build/live-image-amd64.hybrid.iso in a VM.")
        return 0

    run_commands(commands, build_dir)
    print("BUILD_DONE: live-build produced artifacts in build/live-build")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
