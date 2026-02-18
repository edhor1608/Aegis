#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="$(bash "$ROOT_DIR/scripts/live_build_pipeline.sh" --dry-run)"

check_output_contains() {
  local pattern="$1"
  echo "$OUTPUT" | grep -q "$pattern" || { echo "E2E FAIL: missing '$pattern' in output"; exit 1; }
}

check_output_contains "lb clean --purge"
check_output_contains "lb config noauto"
check_output_contains "lb build"
check_output_contains "VM_READY_INSTRUCTION:"

echo "E2E PASS: live-build pipeline dry-run is coherent"
