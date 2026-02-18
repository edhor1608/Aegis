#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-network-check"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Network Check.desktop"

DRY_OUTPUT="$(bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_NETWORK_CHECK_DRY_RUN"
echo "$DRY_OUTPUT" | grep -q "planned_checks=networkmanager,default_route,dns,internet_ping"

RUN_OUTPUT="$(SENIOR_ZERO_NETWORK_CHECK_FAKE=1 bash "$SCRIPT")"
echo "$RUN_OUTPUT" | grep -q "networkmanager_active=yes"
echo "$RUN_OUTPUT" | grep -q "default_route_present=yes"
echo "$RUN_OUTPUT" | grep -q "dns_resolution_ok=yes"
echo "$RUN_OUTPUT" | grep -q "internet_ping_ok=yes"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_NETWORK_CHECK_OK"

grep -q "Exec=lxterminal -e senior-zero-network-check" "$DESKTOP"

echo "E2E PASS: network-check dry-run and fake execution are coherent"
