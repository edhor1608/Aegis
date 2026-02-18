#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shlex
import subprocess
from pathlib import Path


def default_docker_config() -> dict[str, str]:
    return {
        "image_tag": "senior-zero-live-build:bookworm",
        "dockerfile": "docker/live-build-builder.Dockerfile",
        "workspace_mount": "/tmp/repo",
    }


def build_docker_commands(cfg: dict[str, str]) -> list[list[str]]:
    workspace = cfg["workspace_mount"]
    return [
        [
            "docker",
            "build",
            "--platform",
            "linux/amd64",
            "-f",
            cfg["dockerfile"],
            "-t",
            cfg["image_tag"],
            ".",
        ],
        [
            "docker",
            "run",
            "--rm",
            "--platform",
            "linux/amd64",
            "--privileged",
            "-v",
            "${ROOT_DIR}:/src:ro",
            "-v",
            "${ROOT_DIR}/out/live-build:/out",
            "-w",
            "/tmp",
            cfg["image_tag"],
            "bash",
            "-lc",
            f"set -euo pipefail; rm -rf {workspace}; mkdir -p {workspace}; cp -a /src/. {workspace}/; "
            f"cd {workspace}; ./scripts/live_build_pipeline.sh; cp build/live-build/live-image-amd64.hybrid.iso /out/",
        ],
    ]


def format_commands(commands: list[list[str]]) -> str:
    return "\n".join(" ".join(shlex.quote(part) for part in cmd) for cmd in commands)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Senior Zero live-build in Docker")
    parser.add_argument("--dry-run", action="store_true", help="Print docker commands only")
    parser.add_argument("--execute", action="store_true", help="Run docker commands")
    return parser.parse_args()


def execute_commands(root_dir: Path, commands: list[list[str]]) -> None:
    output_dir = root_dir / "out" / "live-build"
    output_dir.mkdir(parents=True, exist_ok=True)
    expanded = []
    for cmd in commands:
        expanded.append([part.replace("${ROOT_DIR}", str(root_dir)) for part in cmd])
    for command in expanded:
        subprocess.run(command, cwd=root_dir, check=True)


def main() -> int:
    args = parse_args()
    cfg = default_docker_config()
    root_dir = Path(__file__).resolve().parents[1]
    commands = build_docker_commands(cfg)

    if args.dry_run or not args.execute:
        print(format_commands(commands))
        print("DOCKER_ISO_PATH: build/live-build/live-image-amd64.hybrid.iso")
        return 0

    execute_commands(root_dir, commands)
    print("DOCKER_BUILD_DONE: build/live-build/live-image-amd64.hybrid.iso")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
