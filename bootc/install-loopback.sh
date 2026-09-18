#!/bin/bash

set -eux

INSECURE=false
FILESYSTEM="ext4"
IMAGE=""

BOOTC_BIN=$(find /home/*/RedHat/bootc/target/release -type f -executable -name bootc)
BOOTUPD_BIN=$(find /home/*/RedHat/bootupd/target/release -type f -executable -name bootupd)

BOOTC_VOL_MNT=(-v "${BOOTC_BIN}:/usr/bin/bootc:ro,Z")
BOOTUPD_VOL_MNT=(-v "${BOOTUPD_BIN}:/usr/sbin/bootupctl:ro")

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

        '--bootloader')
            shift
            BOOTLOADER=$1
            shift
        ;;

        '--image')
            shift
            IMAGE=$1
            shift
        ;;

        '--no-bootc-vol-mnt')
            BOOTC_VOL_MNT=()
            shift
        ;;

        *) echo "Unknown option $1"; exit 1;
    esac
done

# for context in system session; do 
#     for name in $(virsh -c "qemu:///$context" list --all --name); do 
#         if virsh -c "qemu:///$context" dumpxml "$name" | grep -q "notes/bootc/uki-cleanup.img"; then
#             echo "test.img used by $name in context $context"
#             exit 1
#         fi
#     done
# done
#
# exit 0

rm -f test.img composefs-only.qcow2
truncate test.img -s 15G

sudo podman run --rm --net=host --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    --env IMAGE="$IMAGE" \
    --env BOOTC_BOOTLOADER_DEBUG=vvvv \
    -v /dev:/dev \
    "${BOOTC_VOL_MNT[@]}" \
    -v /etc/containers/policy.json:/etc/containers/policy.json \
    "${BOOTUPD_VOL_MNT[@]}" \
    -v /var/lib/containers:/var/lib/containers \
    -v .:/output \
    "$IMAGE" \
    /output/script.sh  "$COMPOSEFS" "$INSECURE" "$BOOTLOADER" "$FILESYSTEM"
