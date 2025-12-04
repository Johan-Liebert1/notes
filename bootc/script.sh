#!/bin/bash

set -eu

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

bootc install to-disk \
    --composefs-backend \
    --bootloader=systemd \
    --source-imgref "docker://$IMAGE" \
    --target-imgref "${IMAGE/localhost/192.168.122.1}"  \
    --generic-image --via-loopback --filesystem=ext4 --wipe \
    "${kargs[@]}" \
    /output/test.img
