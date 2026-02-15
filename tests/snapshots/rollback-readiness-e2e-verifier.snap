#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="$(bash "$ROOT_DIR/scripts/rollback_readiness.sh" --dry-run)"

echo "$OUTPUT" | grep -q "ROLLBACK_READINESS_DRY_RUN"
echo "$OUTPUT" | grep -q "findmnt -n -o FSTYPE /"
echo "$OUTPUT" | grep -q "snapper list-configs"
echo "$OUTPUT" | grep -q "snapper-timeline.timer"
echo "$OUTPUT" | grep -q "snapper-cleanup.timer"

echo "E2E PASS: rollback readiness dry-run is coherent"
