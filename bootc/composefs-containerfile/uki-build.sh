#!/bin/bash

set -eux

FINAL_NAME=$1
CONTAINERFILE=$2

PODMAN_BUILD="podman build"
CFSCTL='./cfsctl --repo tmp/sysroot/composefs'

mkdir -p tmp/sysroot/composefs

cp -f ~/RedHat/bootc/target/release/bootc .
cp -f ~/RedHat/bootc/systemd/composefs-finalize-staged.service .

${PODMAN_BUILD} \
    --iidfile=tmp/STEP1.iid \
    --pull=newer \
    --target=STEP1 \
    -f "$CONTAINERFILE" \
    -t "$FINAL_NAME-stage1" \
    .

STEP1_ID="$(sed s/sha256:// tmp/STEP1.iid)"
${CFSCTL} oci pull containers-storage:"${STEP1_ID}"
STEP1_IMAGE_FSVERITY="$(${CFSCTL} oci compute-id --bootable "${STEP1_ID}")"

${PODMAN_BUILD} \
    --iidfile=tmp/final.iid \
    -t "$FINAL_NAME:latest" \
    --build-context=STEP1="container-image://${STEP1_ID}" \
    --build-arg=COMPOSEFS_FSVERITY="${STEP1_IMAGE_FSVERITY}" \
    --label=containers.composefs.fsverity="${STEP1_IMAGE_FSVERITY}" \
    -f "$CONTAINERFILE" \
    .
