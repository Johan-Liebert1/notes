#!/bin/bash

PODMAN_BUILD="podman build"
CFSCTL='./cfsctl --repo tmp/sysroot/composefs'

mkdir -p tmp/sysroot/composefs

${PODMAN_BUILD} \
    --iidfile=tmp/STEP1.iid \
    --target=STEP1 \
    -f "Containerfile" \
    .

STEP1_ID="$(sed s/sha256:// tmp/STEP1.iid)"
${CFSCTL} oci pull containers-storage:"${STEP1_ID}"
STEP1_IMAGE_FSVERITY="$(${CFSCTL} oci compute-id --bootable "${STEP1_ID}")"

${PODMAN_BUILD} \
    --iidfile=tmp/final.iid \
    -t bootc-composefs-upgrade:latest \
    --build-context=STEP1="container-image://${STEP1_ID}" \
    --build-arg=COMPOSEFS_FSVERITY="${STEP1_IMAGE_FSVERITY}" \
    --label=containers.composefs.fsverity="${STEP1_IMAGE_FSVERITY}" \
    -f "Containerfile" \
    .
