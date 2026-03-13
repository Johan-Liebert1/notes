#!/bin/bash

set -eux

INSECURE=false
FILESYSTEM="ext4"
IMAGE=""

while [ ! -z "${1:-}" ]; do
    case "$1" in
        'composefs') 
            COMPOSEFS=true
            shift 
        ;;

        'ostree') 
            COMPOSEFS=false 
            shift 
        ;;

        'insecure') INSECURE=true
            shift 
        ;;

        '--filesystem')
            shift
            FILESYSTEM=$1
            shift
        ;;

        '--image')
            shift
            IMAGE=$1
            shift
        ;;

        *) echo "Unknown option $1"; exit 1;
    esac
done

rm -f test.img composefs-only.qcow2
truncate test.img -s 15G

sudo podman run --rm --net=host --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    --env IMAGE="$IMAGE" \
    -v /dev:/dev \
    -v /home/pragyan/RedHat/bootc/target/release/bootc:/usr/bin/bootc:ro,Z \
    -v /var/lib/containers:/var/lib/containers \
    -v .:/output \
    "$IMAGE" \
    /output/script.sh  "$COMPOSEFS" "$INSECURE" "$FILESYSTEM"
