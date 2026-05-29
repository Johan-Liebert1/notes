#!/bin/bash

set -eux

if [[ ! -f test-img ]]; then

    cat <<-EOF > sfdisk-buf
        label: gpt
        label-id:  65be9332-59ba-11f1-9b26-6a8e2ab625e4
        size=1Gib, type=C12A7328-F81F-11D2-BA4B-00A0C93EC93B, name="EFI-SYSTEM"
                   type=4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709, name="root"
EOF

    truncate -s4G test-img

    cat sfdisk-buf | sfdisk --wipe=always test-img

fi

set +e

umount -R /var/mnt
losetup -j /var/test-img | cut -d: -f1 | xargs -r losetup -d

set -e

mkdir -p /var/mnt

# Also update kernel partition tables
loopdev=$(losetup --find --show --partscan test-img)

mount "${loopdev}p2" /var/mnt

mkdir -p /var/mnt/efi

mount "${loopdev}p1" /var/mnt/efi


podman run --rm -it 192.168.122.1:5000/bootupd-test bootupctl status
