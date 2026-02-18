#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-launcher"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Launcher.desktop"

DRY_OUTPUT="$(bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_LAUNCHER_DRY_RUN"
echo "$DRY_OUTPUT" | grep -q "action_browser=firefox-esr"
echo "$DRY_OUTPUT" | grep -q "action_help=xdg-open /usr/share/senior-zero/help/welcome.txt"
echo "$DRY_OUTPUT" | grep -q "action_acceptance=senior-zero-acceptance-runner --dry-run"

RUN_OUTPUT="$(SENIOR_ZERO_LAUNCHER_NO_EXEC=1 bash "$SCRIPT" --action help)"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_LAUNCHER_ACTION_EXECUTED"

RUN_ACCEPTANCE_OUTPUT="$(SENIOR_ZERO_LAUNCHER_NO_EXEC=1 bash "$SCRIPT" --action acceptance)"
echo "$RUN_ACCEPTANCE_OUTPUT" | grep -q "action=acceptance command=senior-zero-acceptance-runner --dry-run"

set +e
INVALID_OUTPUT="$(bash "$SCRIPT" --action not-real 2>&1)"
INVALID_STATUS=$?
set -e
if [[ "$INVALID_STATUS" -eq 0 ]]; then
  echo "Expected invalid action to fail" >&2
  exit 1
fi
echo "$INVALID_OUTPUT" | grep -q "SENIOR_ZERO_LAUNCHER_INVALID_ACTION"

grep -q "Exec=lxterminal -e senior-zero-launcher" "$DESKTOP"

echo "E2E PASS: simple launcher dry-run and action mapping are coherent"
