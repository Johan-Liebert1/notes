#!/bin/bash

set -eux

COMPOSEFS=$1
shift
INSECURE=$1
shift

IMAGE="localhost:5000/bootc-bls"

rm -f test.img composefs-only.qcow2
truncate test.img -s 15G

sudo podman run --rm --net=host --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    --env IMAGE=$IMAGE \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v /home/pragyan/RedHat/bootc/target/release/bootc:/usr/bin/bootc:ro,Z \
    -v .:/output \
    $IMAGE \
    /output/script.sh  "$COMPOSEFS" "$INSECURE"
