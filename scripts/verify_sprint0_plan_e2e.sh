#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPRINT_FILE="$ROOT_DIR/docs/plan/sprint-0.md"
RISK_FILE="$ROOT_DIR/docs/plan/risk-register.md"

check_contains() {
  local pattern="$1"
  local file="$2"
  grep -q "$pattern" "$file" || { echo "E2E FAIL: missing '$pattern' in $file"; exit 1; }
}

[[ -f "$SPRINT_FILE" ]] || { echo "E2E FAIL: missing $SPRINT_FILE"; exit 1; }
[[ -f "$RISK_FILE" ]] || { echo "E2E FAIL: missing $RISK_FILE"; exit 1; }

check_contains "Debian image build pipeline" "$SPRINT_FILE"
check_contains "Btrfs rollback integration" "$SPRINT_FILE"
check_contains "security auto-update policy implementation" "$SPRINT_FILE"
check_contains "low-end hardware validation matrix" "$SPRINT_FILE"
check_contains "DE/EN localization baseline" "$SPRINT_FILE"
check_contains "Build reproducibility drift" "$RISK_FILE"
check_contains "Low-end hardware compatibility gaps" "$RISK_FILE"

echo "E2E PASS: sprint-0 plan and risk register are coherent"
