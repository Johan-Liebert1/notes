#!/bin/bash

set -euo pipefail
# set -x

main() {
    # if [[ "${uefi}" == "true" ]]; then
        # args+=("--boot")
        # args+=("")
        # # Skip TPM setup until we have sorted out swtpm support via a sysext
        # args+=("--tpm")
        # args+=("none")
    # fi
    #
    IGNITION_DEVICE_ARG=(--qemu-commandline="-fw_cfg name=opt/com.coreos/config,file=/home/pragyan/notes/ignition.ign")

    virt-install --connect="qemu:///session" \
        --name="fcos-bootc-uki" \
        --vcpus="3" \
        --memory="4096" \
        --osinfo="fedora-coreos-stable" \
        --disk="$HOME/.local/share/libvirt/images/fedora-coreos-usethis-fornew.qcow2" \
        --network bridge=virbr0 \
        --graphics spice,listen=127.0.0.1 \
        --boot uefi,firmware.feature0.name=secure-boot,firmware.feature0.enabled=no \
        --tpm none \
        "${IGNITION_DEVICE_ARG[@]}"
}

main "${@}"
