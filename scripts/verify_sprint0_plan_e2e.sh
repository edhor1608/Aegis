#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPRINT_FILE="$ROOT_DIR/docs/plan/sprint-0.md"
RISK_FILE="$ROOT_DIR/docs/plan/risk-register.md"

[[ -f "$SPRINT_FILE" ]] || { echo "E2E FAIL: missing $SPRINT_FILE"; exit 1; }
[[ -f "$RISK_FILE" ]] || { echo "E2E FAIL: missing $RISK_FILE"; exit 1; }

grep -q "Debian image build pipeline" "$SPRINT_FILE"
grep -q "Btrfs rollback integration" "$SPRINT_FILE"
grep -q "security auto-update policy implementation" "$SPRINT_FILE"
grep -q "low-end hardware validation matrix" "$SPRINT_FILE"
grep -q "DE/EN localization baseline" "$SPRINT_FILE"
grep -q "Build reproducibility drift" "$RISK_FILE"
grep -q "Low-end hardware compatibility gaps" "$RISK_FILE"

echo "E2E PASS: sprint-0 plan and risk register are coherent"
