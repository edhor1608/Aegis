#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-self-check"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Self Check.desktop"
TMP_HOME="$ROOT_DIR/out/tmp-self-check-home"

rm -rf "$TMP_HOME"
mkdir -p "$TMP_HOME"

DRY_OUTPUT="$(HOME="$TMP_HOME" bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_SELF_CHECK_DRY_RUN"
echo "$DRY_OUTPUT" | grep -q "check_preflight=senior-zero-preflight-report --dry-run"

RUN_OUTPUT="$(HOME="$TMP_HOME" SENIOR_ZERO_SELF_CHECK_FAKE=1 bash "$SCRIPT")"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_SELF_CHECK_RESULTS=$TMP_HOME/Documents/senior-zero-self-check.txt"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_SELF_CHECK_OK"

RESULTS_FILE="$TMP_HOME/Documents/senior-zero-self-check.txt"
test -f "$RESULTS_FILE"
grep -q "check_update_policy=pass" "$RESULTS_FILE"

grep -q "Exec=lxterminal -e senior-zero-self-check" "$DESKTOP"

echo "E2E PASS: self-check dry-run and summary generation are coherent"
