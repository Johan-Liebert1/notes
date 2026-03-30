#!/bin/bash

set -xeu

echo "" > /etc/containers/registries.conf
cat >> /etc/containers/registries.conf <<-EOF
        [[registry]]
        location = "localhost:5000"
        insecure = true
EOF

kargs=()

if [[ $IMAGE != *uki* ]]; then
    kargs+=(--karg)
    kargs+=("console=ttyS0,115000n")

    kargs+=(--karg)
    kargs+=("enforcing=0")

    kargs+=(--karg)
    kargs+=("audit=0")

    kargs+=(--karg)
    kargs+=("ignition.platform.id=qemu")

    kargs+=(--karg)
    kargs+=("ignition.firstboot")
fi

COMPOSEFS=$1
INSECURE=$2
BOOTLOADER=$3
FILESYSTEM=$4

if [[ $COMPOSEFS == "true" ]]; then
    options+=("--composefs-backend")
    options+=("--bootloader=$BOOTLOADER")
    options+=("--filesystem=$FILESYSTEM")

    options+=("--uki-addon=ignition")
else
    options=("--filesystem=$FILESYSTEM")
fi

if [[ $INSECURE == "true" ]]; then
    options+=("--allow-missing-verity")
fi

bootc install to-disk \
    --source-imgref "containers-storage:$IMAGE" \
    --target-imgref "${IMAGE/localhost/localhost}"  \
    "${options[@]}" \
    --generic-image --via-loopback --wipe \
    "${kargs[@]}" \
    /output/test.img
