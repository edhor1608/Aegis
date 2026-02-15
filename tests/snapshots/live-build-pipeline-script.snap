#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$ROOT_DIR/build/live-build"

if [[ "${1:-}" == "--dry-run" ]]; then
  python3 "$ROOT_DIR/tools/live_build_pipeline.py" --dry-run
  exit 0
fi

if ! command -v lb >/dev/null 2>&1; then
  echo "ERROR: live-build command 'lb' not found. Install package: live-build"
  exit 1
fi

python3 "$ROOT_DIR/tools/live_build_pipeline.py" --execute
