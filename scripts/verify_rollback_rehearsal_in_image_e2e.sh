#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/sbin/senior-zero-rollback-rehearsal"
OUTPUT="$(bash "$SCRIPT" --dry-run)"

assert_contains() {
  local pattern="$1"
  if ! echo "$OUTPUT" | grep -q "$pattern"; then
    echo "E2E FAIL: expected output to contain '$pattern'" >&2
    echo "E2E FAIL: dry-run output was:" >&2
    echo "$OUTPUT" >&2
    exit 1
  fi
}

assert_contains "ROLLBACK_REHEARSAL_DRY_RUN"
assert_contains "findmnt -n -o FSTYPE /"
assert_contains "snapper list-configs"
assert_contains "snapper -c root create"
assert_contains "snapper -c root list"
assert_contains "snapper -c root delete"

echo "E2E PASS: rollback rehearsal dry-run is coherent"
