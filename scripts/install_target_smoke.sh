#!/usr/bin/env bash
set -euo pipefail

DRY_RUN=0

if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=1
elif [[ $# -gt 0 ]]; then
  echo "Usage: $0 [--dry-run]" >&2
  exit 2
fi

CHECKS=(
  "command -v snapper >/dev/null 2>&1"
  "findmnt -n -o FSTYPE / | grep -qx 'btrfs'"
  "systemctl is-enabled unattended-upgrades | grep -qx 'enabled'"
  "test -f /etc/apt/apt.conf.d/52unattended-upgrades-senior-zero"
  "test -f /etc/apt/preferences.d/90-senior-zero-security.pref"
  "systemctl is-enabled snapper-timeline.timer | grep -qx 'enabled'"
  "systemctl is-enabled snapper-cleanup.timer | grep -qx 'enabled'"
  "systemctl is-active snapper-timeline.timer | grep -qx 'active'"
  "systemctl is-active snapper-cleanup.timer | grep -qx 'active'"
  "test -f /var/lib/senior-zero/rollback-bootstrap.done"
  "locale -a | grep -Eiq 'de_DE.utf8'"
  "locale -a | grep -Eiq 'en_US.utf8'"
)

if [[ "$DRY_RUN" -eq 1 ]]; then
  printf '%s\n' "INSTALL_TARGET_SMOKE_DRY_RUN"
  printf '%s\n' "${CHECKS[@]}"
  exit 0
fi

for check_cmd in "${CHECKS[@]}"; do
  if bash -c "$check_cmd"; then
    printf 'PASS: %s\n' "$check_cmd"
  else
    printf 'FAIL: %s\n' "$check_cmd" >&2
    exit 1
  fi
done

root_fs="$(findmnt -n -o FSTYPE /)"
printf 'INFO: root filesystem: %s\n' "$root_fs"

if snapper list-configs | awk 'NR>1 {print $1}' | grep -qx 'root'; then
  printf '%s\n' "PASS: snapper root config present"
else
  printf '%s\n' "FAIL: snapper root config missing" >&2
  exit 1
fi

printf '%s\n' "INSTALL_TARGET_SMOKE_PASS"
