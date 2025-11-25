#!/bin/bash

set -eu

cat >> /etc/containers/registries.conf <<-EOF
        [[registry]]
        location = "localhost:5000"
        insecure = true
EOF

bootc install to-disk \
    --composefs-backend \
    --bootloader=systemd \
    --source-imgref "containers-storage:$IMAGE" \
    --target-imgref "${IMAGE/localhost/192.168.122.1}"  \
    --generic-image --via-loopback --filesystem=ext4 --wipe \
    --karg console=ttyS0,115000n \
    --karg enforcing=0 \
    --karg audit=0 \
    /output/test.img
