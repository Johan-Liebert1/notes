#!/bin/bash

set -ex

IMAGE="localhost:5000/bootc-bls"

rm -f test.img composefs-only.qcow2
truncate test.img -s 15G

sudo podman run --rm --net=host --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v /home/pragyan/RedHat/bootc/target/release/bootc:/usr/bin/bootc:ro,Z \
    -v .:/output \
    quay.io/fedora/fedora-bootc:42 \
        bootc install to-disk \
        --composefs-native \
        --bootloader=systemd \
        --source-imgref "docker://$IMAGE" \
        --target-imgref "${IMAGE/localhost/192.168.122.1}"  \
        --generic-image --via-loopback --filesystem=ext4 --wipe \
        --karg console=ttyS0,115000n \
        --karg enforcing=0 \
        --karg audit=0 \
        /output/test.img

sudo losetup /dev/loop0 ./test.img
sudo partprobe /dev/loop0
sudo mount /dev/loop0p2 /mnt
sudo cp /usr/lib/systemd/boot/efi/systemd-bootx64.efi /mnt/EFI/fedora/grubx64.efi

sudo umount /mnt
sudo losetup -d /dev/loop0

# qemu-img convert -f raw -O qcow2 test.img composefs-only.qcow2
