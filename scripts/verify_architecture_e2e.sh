#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

check_contains() {
  local pattern="$1"
  local file="$2"
  grep -q "$pattern" "$file" || { echo "E2E FAIL: missing '$pattern' in $file"; exit 1; }
}

required_files=(
  "$ROOT_DIR/docs/architecture/system-model.md"
  "$ROOT_DIR/docs/architecture/update-and-rollback.md"
  "$ROOT_DIR/docs/architecture/app-center-policy.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "E2E FAIL: missing file $file"
    exit 1
  fi
done

check_contains "Debian Stable" "$ROOT_DIR/docs/architecture/system-model.md"
check_contains "snapper" "$ROOT_DIR/docs/architecture/update-and-rollback.md"
check_contains "grub-btrfs" "$ROOT_DIR/docs/architecture/update-and-rollback.md"
check_contains "unattended-upgrades" "$ROOT_DIR/docs/architecture/update-and-rollback.md"
check_contains "apt pinning" "$ROOT_DIR/docs/architecture/update-and-rollback.md"
check_contains "Curated default catalog" "$ROOT_DIR/docs/architecture/app-center-policy.md"
check_contains "More Apps" "$ROOT_DIR/docs/architecture/app-center-policy.md"

echo "E2E PASS: architecture baseline is coherent"
