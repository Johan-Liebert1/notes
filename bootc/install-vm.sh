curl http://192.168.122.1:8080/bootc -o bootc && chmod +x bootc

IMAGE=192.168.122.1/fedora-bootc-uki

podman run \
--rm --privileged \
--pid=host \
-v /dev:/dev \
-v /var/lib/containers:/var/lib/containers \
-v ./bootc:/usr/bin/bootc:ro,Z \
-v /var/tmp:/var/tmp \
--security-opt label=type:unconfined_t \
--env RUST_LOG=debug \
$IMAGE \
bootc install to-disk --composefs-native --boot=uki --source-imgref=containers-storage:$IMAGE /dev/vdb --filesystem=ext4 --wipe
