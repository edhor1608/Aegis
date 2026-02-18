#!/usr/bin/env bash
set -euo pipefail

DRY_RUN=0
EXPECTED_USER="${VM_SMOKE_USER:-user}"
EXPECTED_UID="${VM_SMOKE_UID:-1000}"

if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=1
elif [[ $# -gt 0 ]]; then
  echo "Usage: $0 [--dry-run]" >&2
  exit 2
fi

CHECKS=(
  "whoami | grep -qx '${EXPECTED_USER}'"
  "id -u | grep -qx '${EXPECTED_UID}'"
  "systemctl is-enabled unattended-upgrades | grep -qx 'enabled'"
  "systemctl is-active NetworkManager | grep -qx 'active'"
  "locale -a | grep -Eiq 'en_US.utf8'"
  "locale -a | grep -Eiq 'de_DE.utf8'"
)

if [[ "$DRY_RUN" -eq 1 ]]; then
  printf '%s\n' "VM_SMOKE_DRY_RUN"
  printf '%s\n' "${CHECKS[@]}"
  exit 0
fi

for check_cmd in "${CHECKS[@]}"; do
  if bash -lc "$check_cmd"; then
    printf 'PASS: %s\n' "$check_cmd"
  else
    printf 'FAIL: %s\n' "$check_cmd" >&2
    exit 1
  fi
done

printf '%s\n' "VM_SMOKE_PASS"
