#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="$(bash "$ROOT_DIR/scripts/rollback_readiness.sh" --dry-run)"

check_output_contains() {
  local pattern="$1"
  echo "$OUTPUT" | grep -q "$pattern" || { echo "E2E FAIL: missing '$pattern' in output" >&2; exit 1; }
}

check_output_contains "ROLLBACK_READINESS_DRY_RUN"
check_output_contains "findmnt -n -o FSTYPE /"
check_output_contains "snapper list-configs"
check_output_contains "snapper-timeline.timer"
check_output_contains "snapper-cleanup.timer"

echo "E2E PASS: rollback readiness dry-run is coherent"
