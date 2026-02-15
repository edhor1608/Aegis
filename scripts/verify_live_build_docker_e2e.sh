#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="$(bash "$ROOT_DIR/scripts/live_build_in_docker.sh" --dry-run)"

echo "$OUTPUT" | grep -q "docker build --platform linux/amd64 -f docker/live-build-builder.Dockerfile"
echo "$OUTPUT" | grep -q "docker run --rm --platform linux/amd64 --privileged"
echo "$OUTPUT" | grep -q "/src:ro"
echo "$OUTPUT" | grep -q "/out"
echo "$OUTPUT" | grep -q "cp -a /src"
echo "$OUTPUT" | grep -q "scripts/live_build_pipeline.sh"

echo "E2E PASS: docker live-build pipeline dry-run is coherent"
