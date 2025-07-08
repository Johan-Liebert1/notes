#!/bin/bash

set -eux

STREAM="stable"

# or as a container:
# podman run --pull=newer --rm -v "${HOME}/.local/share/libvirt/images/:/data" -w /data \
#     quay.io/coreos/coreos-installer:release download -s $STREAM -p qemu -f qcow2.xz --decompress


IGNITION_CONFIG="/home/pragyan/notes/virtual-machines/launch/ignition.ign"
IMAGE="${HOME}/.local/share/libvirt/images/fedora-coreos-42.qcow2"
VM_NAME="fedora-coreos"
VCPUS="2"
RAM_MB="2048"
STREAM="stable"
DISK_GB="10"

# For x86 / aarch64,
IGNITION_DEVICE_ARG=(--qemu-commandline="-fw_cfg name=opt/com.coreos/config,file=${IGNITION_CONFIG}")

# Setup the correct SELinux label to allow access to the config
# chcon --verbose --type svirt_home_t ${IGNITION_CONFIG}

virt-install \
    --connect="qemu:///session" \
    --name="${VM_NAME}" \
    --vcpus="${VCPUS}" \
    --memory="${RAM_MB}" \
    --os-variant="fedora-coreos-$STREAM" \
    --import --graphics=none \
    --disk="size=${DISK_GB},backing_store=${IMAGE}" \
    --network bridge=virbr0 \
    "${IGNITION_DEVICE_ARG[@]}"
