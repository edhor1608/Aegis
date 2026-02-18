#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-diagnostics-report"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Diagnostics Report.desktop"
TMP_HOME="$ROOT_DIR/out/tmp-diagnostics-home"

rm -rf "$TMP_HOME"
mkdir -p "$TMP_HOME"

DRY_OUTPUT="$(HOME="$TMP_HOME" bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_DIAGNOSTICS_REPORT_DRY_RUN"

echo "$DRY_OUTPUT" | grep -q "output_file=$TMP_HOME/Documents/senior-zero-diagnostics.txt"

RUN_OUTPUT="$(HOME="$TMP_HOME" SENIOR_ZERO_DIAGNOSTICS_REPORT_FAKE=1 bash "$SCRIPT")"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_DIAGNOSTICS_REPORT_WRITTEN=$TMP_HOME/Documents/senior-zero-diagnostics.txt"

REPORT_FILE="$TMP_HOME/Documents/senior-zero-diagnostics.txt"
test -f "$REPORT_FILE"
grep -q "SENIOR_ZERO_DIAGNOSTICS_REPORT_V1" "$REPORT_FILE"
grep -q "networkmanager_active=yes" "$REPORT_FILE"

grep -q "Exec=lxterminal -e senior-zero-diagnostics-report" "$DESKTOP"

echo "E2E PASS: diagnostics report dry-run and file generation are coherent"
