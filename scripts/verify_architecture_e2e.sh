#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

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

grep -q "Debian Stable" "$ROOT_DIR/docs/architecture/system-model.md"
grep -q "snapper" "$ROOT_DIR/docs/architecture/update-and-rollback.md"
grep -q "grub-btrfs" "$ROOT_DIR/docs/architecture/update-and-rollback.md"
grep -q "unattended-upgrades" "$ROOT_DIR/docs/architecture/update-and-rollback.md"
grep -q "apt pinning" "$ROOT_DIR/docs/architecture/update-and-rollback.md"
grep -q "Curated default catalog" "$ROOT_DIR/docs/architecture/app-center-policy.md"
grep -q "More Apps" "$ROOT_DIR/docs/architecture/app-center-policy.md"

echo "E2E PASS: architecture baseline is coherent"
