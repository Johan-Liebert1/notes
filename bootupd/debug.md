```bash
/dev/mapper$ ls -lahi

total 0
115 drwxr-xr-x.  2 root root     160 May 29 09:06 .
  1 drwxr-xr-x. 17 root root    3.1K May 29 09:06 ..
753 lrwxrwxrwx.  1 root root       7 May 29 09:06 0x48accbd7fdc0119b -> ../dm-0
914 lrwxrwxrwx.  1 root root       7 May 29 09:06 0x48accbd7fdc0119b1 -> ../dm-1
879 lrwxrwxrwx.  1 root root       7 May 29 09:06 0x48accbd7fdc0119b2 -> ../dm-2
953 lrwxrwxrwx.  1 root root       7 May 29 09:06 0x48accbd7fdc0119b3 -> ../dm-3
888 lrwxrwxrwx.  1 root root       7 May 29 09:06 0x48accbd7fdc0119b4 -> ../dm-4
116 crw-------.  1 root root 10, 236 May 29 09:06 control
```

# vudevadm version in c9s 252

In bootc/blockdev we have

```rust
pub fn get_esp_partition_number(&self) -> Result<String> {
    let esp_device = self.find_partition_of_esp()?;
    // devname here would be 0x48accbd7fdc0119b2
    let devname = &esp_device.name;

    let partition_path = Utf8PathBuf::from(format!("/sys/class/block/{devname}/partition"));
```

But we don't have 0x48accbd7fdc0119b2 in /sys/class/block

```bash
[root@qemu0 mnt]# ls -lah /sys/class/block
total 0
drwxr-xr-x.  2 root root 0 May 29 09:06 .
drwxr-xr-x. 71 root root 0 May 29 09:06 ..
lrwxrwxrwx.  1 root root 0 May 29 09:06 dm-0 -> ../../devices/virtual/block/dm-0
lrwxrwxrwx.  1 root root 0 May 29 09:06 dm-1 -> ../../devices/virtual/block/dm-1
lrwxrwxrwx.  1 root root 0 May 29 09:06 dm-2 -> ../../devices/virtual/block/dm-2
lrwxrwxrwx.  1 root root 0 May 29 09:06 dm-3 -> ../../devices/virtual/block/dm-3
lrwxrwxrwx.  1 root root 0 May 29 09:06 dm-4 -> ../../devices/virtual/block/dm-4
lrwxrwxrwx.  1 root root 0 May 29 09:06 loop0 -> ../../devices/virtual/block/loop0
lrwxrwxrwx.  1 root root 0 May 29 09:06 sda -> ../../devices/pci0000:00/0000:00:02.0/virtio1/host0/target0:0:0/0:0:0:0/block/sda
lrwxrwxrwx.  1 root root 0 May 29 09:06 sdb -> ../../devices/pci0000:00/0000:00:03.0/virtio2/host1/target1:0:0/1:0:0:0/block/sdb
```

## /etc/multipath.conf

```bash
# device-mapper-multipath configuration file

# For a complete list of the default configuration values, run either:
# # multipath -t
# or
# # multipathd show config

# For a list of configuration options with descriptions, see the
# multipath.conf man page.

defaults {
        user_friendly_names no
        find_multipaths on
}

blacklist {
}
```

# ===============> Getting device info

```bash
udevadm info --query=all --name=/dev/mapper/0x48accbd7fdc0119b2
```
