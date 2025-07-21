IGNITION_CONFIG="/home/pragyan/notes/virtual-machines/launch/ignition.ign"
IGNITION_DEVICE_ARG=(--qemu-commandline="-fw_cfg name=opt/com.coreos/config,file=${IGNITION_CONFIG}")

virt-install \
    --name bootc-lldb \
    --vcpus 2 \
    --memory 2048 \
    --import --disk ~/RedHat/bootc/bootc.img \
    --os-variant fedora-unknown \
    --network bridge=virbr0 \
    "${IGNITION_DEVICE_ARG[@]}"
