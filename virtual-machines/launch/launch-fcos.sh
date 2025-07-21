#!/bin/bash

set -ex

STREAM="stable"

# or as a container:
# podman run --pull=newer --rm -v "${HOME}/.local/share/libvirt/images/:/data" -w /data \
#     quay.io/coreos/coreos-installer:release download -s $STREAM -p qemu -f qcow2.xz --decompress

if [[ "$1" == "uefi" ]]; then
    qemu_args=(
        '-drive' 'if=pflash,format=raw,unit=0,readonly=on,file=/usr/share/edk2/ovmf/OVMF_CODE.fd'
        '-drive' 'if=pflash,format=raw,unit=1,file=./QEMU_VARS.fd'
    )
else
    qemu_args=()
fi

IGNITION_CONFIG="/home/pragyan/notes/virtual-machines/launch/ignition.ign"
IMAGE="${HOME}/.local/share/libvirt/images/bootc-only.qcow2"
VM_NAME="bootc-only"
VCPUS="2"
RAM_MB="2048"
STREAM="stable"
DISK_GB="10"

# For x86 / aarch64,
IGNITION_DEVICE_ARG=(--qemu-commandline="-fw_cfg name=opt/com.coreos/config,file=${IGNITION_CONFIG}")

qemu_args+=($IGNITION_DEVICE_ARG)

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
    --boot \
loader=/usr/share/edk2-ovmf/x64/OVMF_CODE.4m.fd,\
loader.readonly=yes,loader.secure=no,\
loader.type=pflash,\
nvram.template=/usr/share/edk2/x64/OVMF_VARS.4m.fd,\
nvram=/home/pragyan/notes/virtual-machines/launch/OVMF_VARS.4m.fd \
    "${IGNITION_DEVICE_ARG[@]}"
