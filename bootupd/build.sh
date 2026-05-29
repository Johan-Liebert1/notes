#!/bin/bash

set -eux

# grub-cc sha
# 659bf0a47d1e0c45341fb6089ec045ba5e893da6580c1f79699318e0b8cd6116  /usr/lib/efi/grub2/1:2.12-58.fc44/EFI/fedora/grubx64.efi

pushd /home/pragyan/RedHat/bootupd || exit
cargo b --release
popd

rm -rfv bootupd
cp /home/pragyan/RedHat/bootupd/target/release/bootupd .

podman build -t localhost:5000/bootupd-test -f ./Containerfile.bootupd
