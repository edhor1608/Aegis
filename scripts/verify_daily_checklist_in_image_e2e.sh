#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-daily-checklist"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Daily Checklist.desktop"
TMP_HOME="$ROOT_DIR/out/tmp-daily-checklist-home"

rm -rf "$TMP_HOME"
mkdir -p "$TMP_HOME"

DRY_OUTPUT="$(HOME="$TMP_HOME" bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_DAILY_CHECKLIST_DRY_RUN"

echo "$DRY_OUTPUT" | grep -q "checklist_items=network,updates,storage,help"

RUN_OUTPUT="$(HOME="$TMP_HOME" SENIOR_ZERO_DAILY_CHECKLIST_FAKE=1 bash "$SCRIPT")"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_DAILY_CHECKLIST_WRITTEN=$TMP_HOME/Documents/senior-zero-daily-checklist.txt"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_DAILY_CHECKLIST_READY"

REPORT_FILE="$TMP_HOME/Documents/senior-zero-daily-checklist.txt"
test -f "$REPORT_FILE"
grep -q "item_updates=ready" "$REPORT_FILE"

grep -q "Exec=lxterminal -e senior-zero-daily-checklist" "$DESKTOP"

echo "E2E PASS: daily-checklist dry-run and fake execution are coherent"
