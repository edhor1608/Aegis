#!/usr/bin/env bash
set -euo pipefail

DRY_RUN=0

if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=1
elif [[ $# -gt 0 ]]; then
  echo "Usage: $0 [--dry-run]" >&2
  exit 2
fi

PRECHECKS=(
  "command -v snapper >/dev/null 2>&1"
  "command -v btrfs >/dev/null 2>&1"
)

ROOT_FS_CHECK="findmnt -n -o FSTYPE /"

BTRFS_CHECKS=(
  "snapper list-configs | awk 'NR>1 {print \$1}' | grep -qx 'root'"
  "systemctl is-enabled snapper-timeline.timer | grep -qx 'enabled'"
  "systemctl is-enabled snapper-cleanup.timer | grep -qx 'enabled'"
)

if [[ "$DRY_RUN" -eq 1 ]]; then
  printf '%s\n' "ROLLBACK_READINESS_DRY_RUN"
  printf '%s\n' "${PRECHECKS[@]}"
  printf '%s\n' "$ROOT_FS_CHECK"
  printf '%s\n' "${BTRFS_CHECKS[@]}"
  exit 0
fi

for check_cmd in "${PRECHECKS[@]}"; do
  if bash -c "$check_cmd"; then
    printf 'PASS: %s\n' "$check_cmd"
  else
    printf 'FAIL: %s\n' "$check_cmd" >&2
    exit 1
  fi
done

root_fs="$(findmnt -n -o FSTYPE /)"
printf 'INFO: root filesystem: %s\n' "$root_fs"

if [[ "$root_fs" != "btrfs" ]]; then
  printf '%s\n' "NOT_APPLICABLE: rollback validation requires installed btrfs root"
  exit 0
fi

for check_cmd in "${BTRFS_CHECKS[@]}"; do
  if bash -c "$check_cmd"; then
    printf 'PASS: %s\n' "$check_cmd"
  else
    printf 'FAIL: %s\n' "$check_cmd" >&2
    exit 1
  fi
done

printf '%s\n' "ROLLBACK_READINESS_PASS"
