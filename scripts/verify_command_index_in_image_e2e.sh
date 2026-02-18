#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-command-index"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Command Index.desktop"

DRY_OUTPUT="$(bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_COMMAND_INDEX_DRY_RUN"
echo "$DRY_OUTPUT" | grep -q "planned_commands=senior-zero-preflight-report,senior-zero-update-check,senior-zero-runtime-profile,senior-zero-network-check,senior-zero-storage-check,senior-zero-self-check,senior-zero-session-report,senior-zero-support-bundle,senior-zero-daily-checklist,senior-zero-command-doctor,senior-zero-acceptance-runner"

RUN_OUTPUT="$(SENIOR_ZERO_COMMAND_INDEX_FAKE=1 bash "$SCRIPT")"
echo "$RUN_OUTPUT" | grep -q "cmd_preflight_report=available"
echo "$RUN_OUTPUT" | grep -q "cmd_self_check=available"
echo "$RUN_OUTPUT" | grep -q "cmd_session_report=available"
echo "$RUN_OUTPUT" | grep -q "cmd_support_bundle=available"
echo "$RUN_OUTPUT" | grep -q "cmd_daily_checklist=available"
echo "$RUN_OUTPUT" | grep -q "cmd_command_doctor=available"
echo "$RUN_OUTPUT" | grep -q "cmd_acceptance_runner=available"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_COMMAND_INDEX_READY"

grep -q "Exec=lxterminal -e senior-zero-command-index" "$DESKTOP"

echo "E2E PASS: command-index dry-run and fake execution are coherent"
