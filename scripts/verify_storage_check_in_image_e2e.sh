#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-storage-check"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Storage Check.desktop"

DRY_OUTPUT="$(bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_STORAGE_CHECK_DRY_RUN"
echo "$DRY_OUTPUT" | grep -q "planned_checks=btrfs_command,snapper_command,root_fs,root_usage"

RUN_OUTPUT="$(SENIOR_ZERO_STORAGE_CHECK_FAKE=1 bash "$SCRIPT")"
echo "$RUN_OUTPUT" | grep -q "btrfs_command_available=yes"
echo "$RUN_OUTPUT" | grep -q "snapper_command_available=yes"
echo "$RUN_OUTPUT" | grep -q "root_fs_is_btrfs=yes"
echo "$RUN_OUTPUT" | grep -q "root_usage_percent=42"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_STORAGE_CHECK_OK"

grep -q "Exec=lxterminal -e senior-zero-storage-check" "$DESKTOP"

echo "E2E PASS: storage-check dry-run and fake execution are coherent"
