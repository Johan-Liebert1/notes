#!/bin/bash
set -euo pipefail

echo "Calculating PCR 8:"
part1="$(printf "set timeout=5" | sha256sum | cut -f1 -d\ | tr '[:lower:]' '[:upper:]')"
echo "part1: ${part1}"
part2="$(printf "blscfg" | sha256sum | cut -f1 -d\ | tr '[:lower:]' '[:upper:]')"
echo "part2: ${part2}"

# part1=71a5b3b21ac3862f40fabb745a9649c3a1d34249b9706524c90b2480c298beb0
# part2=05a5577cb6b242b7b5aff400fd90224598d1e354937fadc90f954cab3dc78519

PCR_zero="0000000000000000000000000000000000000000000000000000000000000000"
EXT="$( (echo -n "${PCR_zero}" | xxd -r -ps ; echo -n "${part1}" | xxd -r -ps ) | sha256sum | cut -f1 -d\  | tr '[:lower:]' '[:upper:]')"
EXT="$( (echo -n "${EXT}" | xxd -r -ps ; echo -n "${part2}" | xxd -r -ps )| sha256sum | cut -f1 -d\ | tr '[:lower:]' '[:upper:]')"
echo "PCR 8: ${EXT}"
