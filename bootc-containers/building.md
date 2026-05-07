# Building images for centos-stream, centos-bootc, bootc-centos

```sh
podman build -t containers-bootc-c10s -v "$(pwd):/buildcontext" --security-opt=label=disable --cap-add=all --device /dev/fuse .
```
