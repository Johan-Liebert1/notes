#!/bin/bash

set -eu

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
fi

COMPOSEFS=false

options=("--filesystem=ext4")

if [[ $COMPOSEFS == "true" ]]; then
    options+=("--composefs-backend")
    options+=("--bootloader=grub")
    options+=("--insecure")
fi

bootc install to-disk \
    --source-imgref "docker://$IMAGE" \
    --target-imgref "${IMAGE/localhost/localhost}"  \
    "${options[@]}" \
    --generic-image --via-loopback --wipe \
    "${kargs[@]}" \
    /output/test.img
