#!/bin/bash

set -eux

FINAL_NAME=$1
CONTAINERFILE=$2

if [[ "$CONTAINERFILE" == *sealed* ]]; then
    SEALED=true
else
    SEALED=false
fi

mkdir -p tmp/sysroot/composefs
SECUREBOOT_KEYS=()

if [[ $SEALED ]]; then
    /home/pragyan/notes/virtual-machines/secureboot.sh
    SECUREBOOT_KEYS=("--secret=id=secureboot_key,src=secureboot/db.key" "--secret=id=secureboot_cert,src=secureboot/db.crt")
fi


# shellcheck disable=SC2086
sudo podman build \
    --iidfile=tmp/STEP1.iid \
    --pull=never \
    --net=host \
    --security-opt label=type:unconfined_t \
    --target=step1 \
    "${SECUREBOOT_KEYS[@]}" \
    -f "$CONTAINERFILE" \
    -t "$FINAL_NAME-stage1" \
    .

STEP1_ID="$(cat tmp/STEP1.iid)"
sudo ./bootc internals cfs --repo tmp/sysroot/composefs init  --erofs-version 2
sudo ./bootc internals cfs --repo tmp/sysroot/composefs oci pull containers-storage:"${STEP1_ID}"
STEP1_IMAGE_FSVERITY="$(sudo ./bootc internals cfs --repo tmp/sysroot/composefs oci compute-id --bootable "containers-storage:${STEP1_ID}" | tail -1)"

sudo podman build \
    --iidfile=tmp/final.iid \
    --net=host \
    -t "$FINAL_NAME:latest" \
    --security-opt label=type:unconfined_t \
    "${SECUREBOOT_KEYS[@]}" \
    --build-context=step1="container-image://${STEP1_ID}" \
    --build-arg=COMPOSEFS_FSVERITY="${STEP1_IMAGE_FSVERITY/I::IS_MUTATING: true\\n/}" \
    --label=containers.composefs.fsverity="${STEP1_IMAGE_FSVERITY}" \
    -f "$CONTAINERFILE" \
    .
