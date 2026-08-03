#!/bin/bash

if [[ "$PWD" != "$HOME/notes/bootc" ]]; then
    echo "Run this command from $HOME/notes/bootc"
    exit 1
fi

sudo umount -R /mnt

set -ex

rm -f test.img composefs-only.qcow2
truncate -s 10G test.img

BOOTFS_UUID="96d15588-3596-4b3c-adca-a2ff7279ea63"
# ROOTFS_UUID="4f68bce3-e8cd-4db1-96e7-fbcaf984b709"

cat > sfdisk-buf <<EOF
    label: gpt
    label-id: $(uuidgen)
    size=512MiB, type=C12A7328-F81F-11D2-BA4B-00A0C93EC93B, name="EFI-SYSTEM"
    size=512MiB, type=0FC63DAF-8483-4772-8E79-3D69D8477DE4, name="boot"
                 type=4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709, name="root"
EOF

loopdev=$(losetup -f)

sudo losetup "${loopdev}" test.img
cat sfdisk-buf | sudo sfdisk --wipe=always "${loopdev}"

# To make sure kernel updates
sudo partprobe "${loopdev}"

sudo mkfs.fat  "${loopdev}"p1
sudo mkfs.ext4 "${loopdev}"p2  -L boot -U $BOOTFS_UUID
sudo mkfs.ext4 "${loopdev}"p3  -L root

sudo mount "${loopdev}"p3 /mnt
sudo mkdir -p /mnt/boot
sudo mount "${loopdev}"p2 /mnt/boot
sudo mkdir -p /mnt/boot/efi

IMAGE="localhost/bootc-bls"
BOOTLOADER=systemd

./install-to-fs.sh $IMAGE $BOOTLOADER

sudo umount -R /mnt

sudo losetup -d "${loopdev}"

# qemu-img convert -f raw -O qcow2 test.img composefs-only.qcow2
