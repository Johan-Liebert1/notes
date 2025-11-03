# Resizing a qcow2 image

```bash
# Add 20GB to the image
qemu-img resize image.qcow +20G
```

The above will not show up on disk as `prev image size + 20GB`, it'll still show up as `prev image size`


We need to resize the partition using this image to actually allocate the space.
QCOW2 is sparse — it only uses space for what’s actually written, even if its virtual size is larger.


## Getting the actual size

1. Start the VM, then we'll resize the partition we want

```bash
# If filesystem is mounted as read only, remount it as read/write
mount -o remount,rw /sysroot

# Grow the 4th partition of /dev/vda (to the end I guess since we didn't specify size here)
growpart /dev/vda 4

# Running growpart /dev/vda 4 only resizes the partition table, not the filesystem itself.
# To finish expanding the space, we now need to resize the filesystem inside the partition.
resize2fs /dev/vda4

# NOTE: the above works for etx4/3, etc, if xfs do this
xfs_growfs /

# NOTE: For btrfs
btrfs filesystem resize max /

```
