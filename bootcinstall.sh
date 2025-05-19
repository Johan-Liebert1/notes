
curl http://192.168.122.1:8080/bootc -o bootc
chmod +x bootc

# curl http://192.168.122.1:8080/skopeo -o skopeo
# chmod +x skopeo
# 
# -v /var/skopeo:/var/skopeo:ro,Z \

TARGET=containers-storage
IMAGE=localhost/bls-latest:latest

# -v $IMAGE:$IMAGE \

podman run \
--rm --privileged \
--pid=host \
-v /dev:/dev \
-v /var/lib/containers:/var/lib/containers \
-v /var/bootc:/usr/bin/bootc:ro,Z \
-v /var/tmp:/var/tmp \
-v /var/symlink:/var/symlink \
--security-opt label=type:unconfined_t \
--env RUST_LOG=debug \
--env RUST_BACKTRACE=1 \
localhost/bootc-new:latest \
bootc install to-disk --composefs --target-transport=$TARGET --target-imgref=$IMAGE /dev/vdb --filesystem=ext4 --wipe

# --------- thi sone

curl http://192.168.122.1:8080/bootc -o bootc
chmod +x bootc

# curl http://192.168.122.1:8080/skopeo -o skopeo
# chmod +x skopeo
# 
# -v /var/skopeo:/var/skopeo:ro,Z \

TARGET=containers-storage
IMAGE=localhost/bootc-uki:latest

# -v $IMAGE:$IMAGE \

podman run \
--rm --privileged \
--pid=host \
-v /dev:/dev \
-v /var/lib/containers:/var/lib/containers \
-v /var/bootc:/usr/bin/bootc:ro,Z \
-v /var/tmp:/var/tmp \
-v /var/symlink:/var/symlink \
--security-opt label=type:unconfined_t \
--env RUST_LOG=debug \
--env RUST_BACKTRACE=1 \
$IMAGE \
bootc install to-disk --composefs --target-transport=$TARGET --target-imgref=$IMAGE /dev/vdb --filesystem=ext4 --wipe
curl http://192.168.122.1:8000/bootc -o bootc
chmod +x bootc

IMAGE=/var/bls-old.tar

podman run \
--rm --privileged \
--pid=host \
-v /dev:/dev \
-v /var/lib/containers:/var/lib/containers \
-v /var/bootc:/usr/bin/bootc:ro,Z \
-v /var/tmp:/var/tmp \
-v $IMAGE:$IMAGE \
-v /var/symlink:/var/symlink \
--security-opt label=type:unconfined_t \
--env RUST_LOG=debug \
--env RUST_BACKTRACE=1 \
--env C_STORAGE=oci-archive \
--env C_IMAGE=$IMAGE \
localhost/bootc-new:latest \
bootc install to-disk /dev/vdc --filesystem=ext4 --wipe
