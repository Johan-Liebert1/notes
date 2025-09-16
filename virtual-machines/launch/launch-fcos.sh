#!/bin/bash

set -ex

STREAM="stable"

IGNITION_CONFIG="/home/pragyan/notes/virtual-machines/launch/ignition.ign"
IMAGE="/home/pragyan/notes/bootc/composefs-only.qcow2"
VM_NAME="composefs-only"
VCPUS="2"
RAM_MB="2048"
STREAM="stable"
DISK_GB="15"

# For x86 / aarch64,
IGNITION_DEVICE_ARG=(--qemu-commandline="-fw_cfg name=opt/com.coreos/config,file=${IGNITION_CONFIG}")

# Setup the correct SELinux label to allow access to the config
chcon --verbose --type svirt_home_t ${IGNITION_CONFIG}

mkdir -p ~/.local/share/libvirt/nvram
cp /usr/share/OVMF/OVMF_VARS.fd ~/.local/share/libvirt/nvram/${VM_NAME}_VARS.fd

virt-install \
    --connect="qemu:///session" \
    --name="${VM_NAME}" \
    --vcpus="${VCPUS}" \
    --memory="${RAM_MB}" \
    --os-variant="fedora-coreos-$STREAM" \
    --import --graphics=none \
    --disk="size=${DISK_GB},backing_store=${IMAGE}" \
    --network bridge=virbr0 \
    --boot loader=/usr/share/OVMF/OVMF_CODE.fd,loader.readonly=yes,loader.secure=no,nvram=/home/pragyan/.local/share/libvirt/nvram/${VM_NAME}_VARS.fd \
    "${IGNITION_DEVICE_ARG[@]}"
