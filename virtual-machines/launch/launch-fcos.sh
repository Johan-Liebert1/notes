#!/bin/bash

set -eu

STREAM="stable"

IGNITION_CONFIG="/home/pragyan/notes/virtual-machines/launch/ignition.ign"
IMAGE="$HOME/notes/bootc/test.img"
VM_NAME="composefs-only"
VCPUS="2"
RAM_MB="2048"
STREAM="stable"
DISK_GB="10"
SECUREBOOT=false

# For x86 / aarch64,
IGNITION_DEVICE_ARG=(--qemu-commandline="-fw_cfg name=opt/com.coreos/config,file=${IGNITION_CONFIG}")

while [ ! -z "${1:-}" ]; do
    case "$1" in
        "--vm-name" )
            VM_NAME="$2"
            shift
            shift
        ;;

        "--image" )
            IMAGE="$2"
            shift
            shift
        ;;

        "--size" )
            DISK_GB="$2"
            shift
            shift
        ;;

        "--memory" )
            RAM_MB="$2"
            shift
            shift
        ;;

        "--no-ign" )
            IGNITION_DEVICE_ARG=()
            shift
        ;;

        "--secureboot" )
            SECUREBOOT=true
            shift
        ;;


        * )
            echo "Argument $1 not understood"
            exit 1
        ;;
    esac
done

set -ex

# Setup the correct SELinux label to allow access to the config
chcon --verbose --type svirt_home_t ${IGNITION_CONFIG}

# OVMF paths for secure boot
OVMF_CODE="/usr/share/OVMF/OVMF_CODE.secboot.fd"
OVMF_VARS="$HOME/.local/share/libvirt/nvram/${VM_NAME}_VARS.fd"
OVMF_VARS_TEMPLATE="/usr/share/OVMF/OVMF_VARS.secboot.fd"

mkdir -p "$(dirname OVMF_VARS)"
cp /usr/share/OVMF/OVMF_VARS.fd "$OVMF_VARS"

args=()
if [[ "${SECUREBOOT}" == "true" ]]; then
    loader="loader=${OVMF_CODE},loader.readonly=yes,loader.type=pflash"
    nvram="nvram=${OVMF_VARS},nvram.template=${OVMF_VARS_TEMPLATE},loader_secure=yes"
    features="firmware.feature0.name=secure-boot,firmware.feature0.enabled=yes,firmware.feature1.name=enrolled-keys,firmware.feature1.enabled=yes"

    args+=("--boot")
    args+=("uefi,${loader},${nvram},${features}")
    args+=("--tpm")
    args+=("backend.type=emulator,backend.version=2.0,model=tpm-tis")
else
    args+=("--boot")
    args+=("uefi,firmware.feature0.name=secure-boot,firmware.feature0.enabled=no")
fi

# --boot loader=/usr/share/OVMF/OVMF_CODE.fd,loader.readonly=yes,loader.secure=no,nvram=/home/pragyan/.local/share/libvirt/nvram/${VM_NAME}_VARS.fd \

if [[ "$IMAGE" == *.img ]]; then
    disk=(--disk="path=${IMAGE},format=raw")
else
    disk=(--disk="size=${DISK_GB},backing_store=${IMAGE}")
fi

CONNECT="qemu:///session"

if [[ $(whoami) == "root" ]]; then
    CONNECT="qemu:///system"
fi

virt-install \
    --connect="$CONNECT" \
    --name="${VM_NAME}" \
    --vcpus="${VCPUS}" \
    --memory="${RAM_MB}" \
    --os-variant="fedora-coreos-$STREAM" \
    --import --nographics \
    --network bridge=virbr0 \
    --memorybacking=source.type=memfd,access.mode=shared \
    --filesystem /var/lib/containers,containers,driver.type=virtiofs \
    "${disk[@]}" \
    "${args[@]}" \
    "${IGNITION_DEVICE_ARG[@]}"
