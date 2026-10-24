# VM Stuck in initramfs

Usually can happen due to the sizes differing

`~/notes/virtual-machines/launch/launch-fcos.sh` has size hardcoded to 10G, but  the actual
disk was 16GB

```bash
Disk /dev/nbd0: 16 GiB, 17179869184 bytes, 33554432 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 131072 bytes
Disklabel type: gpt
Disk identifier: 2BFC1D47-388C-4934-9847-BE0B05710816

Device        Start      End  Sectors Size Type
/dev/nbd0p1    2048     4095     2048   1M BIOS boot
/dev/nbd0p2    4096  2101247  2097152   1G Linux filesystem
/dev/nbd0p3 2101248 33552383 31451136  15G Linux filesystem
```

Doing the following fixes it

```bash
~/notes/virtual-machines/launch/launch-fcos.sh \
    --vm-name rhcos-410.81.20200520.0-qemu.qcow2 \
    --image ~/Downloads/rhcos-410.81.20200520.0-qemu.qcow2 \
    --bios --size 16
```
