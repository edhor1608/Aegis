#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/sbin/senior-zero-rollback-rehearsal"
OUTPUT="$(bash "$SCRIPT" --dry-run)"

echo "$OUTPUT" | grep -q "ROLLBACK_REHEARSAL_DRY_RUN"
echo "$OUTPUT" | grep -q "findmnt -n -o FSTYPE /"
echo "$OUTPUT" | grep -q "snapper list-configs"
echo "$OUTPUT" | grep -q "snapper -c root create"
echo "$OUTPUT" | grep -q "snapper -c root list"
echo "$OUTPUT" | grep -q "snapper -c root delete"

echo "E2E PASS: rollback rehearsal dry-run is coherent"
