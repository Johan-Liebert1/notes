```bash
# 1. Create a blank disk image
truncate -s 100M test.img

# 2. Associate it with a loop device
LOOPDEV=$(sudo losetup --find --show test.img)
```

### Partition the disk using parted

```bash
# 3. Partition it (create one partition with GPT label "ROOT")
sudo parted -s "$LOOPDEV" mklabel gpt
sudo parted -s "$LOOPDEV" mkpart primary ext4 1MiB 100%
sudo parted -s "$LOOPDEV" name 1 ROOT
```

### Use kpartx to partition the device

```bash
# 4. Map the partitions to /dev/mapper using kpartx
sudo kpartx -a "$LOOPDEV"

# 5. Check the partition path
ls /dev/mapper/  # e.g., loopXp1
```

`/dev/mapper` is a directory containing device nodes managed by the device-mapper subsystem in the Linux kernel.

* Used by LVM (Logical Volume Manager): `/dev/mapper/vgname-lvname`
* dm-crypt/LUKS encrypted devices show up here
* kpartx: Creates partition mappings for loop or device files (e.g. /dev/mapper/loop0p1)

Device-mapper provides a framework for virtual block devices — `/dev/mapper/*` is where those virtual devices appear.

```bash
# before running kpartx on $LOOPDEV
ll /dev/mapper

crw-------. 1 root root 10, 236 Jun 26 09:18 /dev/mapper/control


# After running kpartx on $LOOPDEV
ll /dev/mapper

crw-------.  1 root root 10, 236 Jun 26 09:18 control
lrwxrwxrwx.  1 root root       7 Jun 26 11:10 loop0p1 -> ../dm-0
```

Device-mapper `/dev/dm-*` only appears if a virtual device is being used, like

* LVM (Logical Volume Manager)
* dm-crypt/LUKS encrypted partitions
* kpartx for partition mapping
* RAID or multipath

SSD (e.g., /dev/nvme0n1, /dev/sda) is a real physical device, so its partitions appear directly as /dev/nvme0n1p1, /dev/sda1, etc., not as /dev/dm-*.

If `LVM` or `encryption` is used on that SSD, then `dm-*` devices will appear.


### /dev/disk/by-partlabel

```bash
# Look for /dev/disk/by-partlabel/ROOT
ll /dev/disk/by-partlabel # may exist or point to the wrong device

lrwxrwxrwx.  1 root root  15 Jun 26 09:18 'EFI\x20System\x20Partition' -> ../../nvme0n1p1
lrwxrwxrwx.  1 root root  10 Jun 26 11:10  ROOT -> ../../dm-0

# The ROOT partition points to /dev/dm-0, which is not correct
realpath /dev/disk/by-partlabel/ROOT

/dev/dm-0

# Compare with the actual partition created
realpath /dev/mapper/$(basename "$LOOPDEV")p1

/dev/dm-0

# 8. Clean up
kpartx -d "$LOOPDEV"
losetup -d "$LOOPDEV"
rm test.img
```

MBR supports partition type IDs, not labels, but some tools (like udev) synthesize labels for EFI System Partitions (ESP) based on well-known type IDs.

The ESP often gets mapped to `/dev/disk/by-partlabel/EFI-SYSTEM` due to its type ID 0xEF (FAT32, ESP).

Actual ROOT partition doesn't have a recognized special type, so no label is generated.

Only GPT allows custom, named partition labels (PARTLABEL), which are stored in the GPT header.
MBR has no space for user-defined names — just numeric type codes.

