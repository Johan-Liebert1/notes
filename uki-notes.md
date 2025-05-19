Add 

```sh
# Install the actual target directly
inst "$systemdutildir"/system-generators/systemd-fstab-generator \
     "$systemdutildir"/systemd-sysroot-fstab-check
```

to dractu modules

```sh
objcopy -O binary --only-section=.initrd <uki.efi> initrd.img
```

In place UKI edit

```bash
objcopy -O binary --only-section=.cmdline uki.efi cmdline.txt

# edit cmdline.txt
sed -i "s;6d4d6891-6640-49fc-83cb-81ccf81fd184;$ROOT_UUID;g" cmdline.txt

objcopy --update-section .cmdline=cmdline.txt uki.efi patched-uki.efi

rm -f uki.efi
mv patched-uki.efi uki.efi
```

```bash
#!/bin/bash

cd /mnt/boot/EFI/Linux

objcopy -O binary --only-section=.cmdline uki.efi cmdline.txt

export ROOT_UUID=$(blkid | grep vdb3 | grep '\bUUID\b="\([a-z0-9\-]*\)"' -o | awk -FUUID=\" '{print $2}' | sed 's;";;')

# edit cmdline.txt
sed -i "s;6d4d6891-6640-49fc-83cb-81ccf81fd184;$ROOT_UUID;g" cmdline.txt

objcopy --update-section .cmdline=cmdline.txt uki.efi patched-uki.efi

rm -f uki.efi
mv patched-uki.efi uki.efi

# Also need to fix the composefs=<image_id> cmdline param as that also changes
```


Always exclude the UKI form the erofs
