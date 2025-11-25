Issues with coreos (coreos bootc issues)

If root=UUID=<> is set then crypt_LUKS is mounted as /sysroot which doesn't work

Somehow, with grub, /boot's UUID is changed and GRUB doesn't know where to get the /boot parition as `bootuuid.cfg`
has old UUID


Another issue after root uuid change


sh-5.2# blkid
/dev/vda2: LABEL="boot" UUID="b6021e42-aceb-45c7-9353-4a4d6e493366" BLOCK_SIZE="4096" TYPE="ext4" PARTLABEL="boot" PARTUUID="df4705c5-aca1-4159-b729-a9255f31c59a"
/dev/vda3: UUID="4f68bce3-e8cd-4db1-96e7-fbcaf984b709" LABEL="luks-root" TYPE="crypto_LUKS" PARTLABEL="root" PARTUUID="b2e05244-52ff-49dd-981b-8daa53b43aca"
/dev/vda1: UUID="7DEB-7910" BLOCK_SIZE="512" TYPE="vfat" PARTLABEL="EFI-SYSTEM" PARTUUID="73a02bc2-b597-45de-97f0-045afad47696"

sh-5.2# cat /proc/cmdline 
BOOT_IMAGE=(hd0,gpt2)/6a73fabb9b1c5b3c364a497fdcbbc84cc3289259be3177f85f6b61614f903ab6e288319eca6fed0a3d823692ebe480424f7a6a4c97cf304f0018438a86f2d620/vmlinuz console=ttyS0,115000n enforcing=
0 audit=0 ignition.platform.id=qemu root=UUID=910678ff-f77e-4a7d-8d53-86f2ac47a823 composefs=6a73fabb9b1c5b3c364a497fdcbbc84cc3289259be3177f85f6b61614f903ab6e288319eca6fed0a3d823692ebe480424f
7a6a4c97cf304f0018438a86f2d620

[  193.408035] dracut-initqueue[682]: Warning: dracut-initqueue: starting timeout scripts
[  193.193570] dracut-initqueue[682]: Warning: dracut-initqueue: starting timeout scripts
[  193.942668] dracut-initqueue[682]: Warning: dracut-initqueue: timeout, still waiting for following initqueue hooks:
[  193.728704] dracut-initqueue[682]: Warning: dracut-initqueue: timeout, still waiting for following initqueue hooks:
[  193.946383] dracut-initqueue[682]: Warning: /lib/dracut/hooks/initqueue/finished/devexists-\x2fdev\x2fdisk\x2fby-uuid\x2f910678ff-f77e-4a7d-8d53-86f2ac47a823.sh: "if ! grep -q After=remote
-fs-pre.target /run/systemd/generator/systemd-cryptsetup@*.service 2>/dev/null; then
[  193.734580] dracut-initqueue[682]: Warning: /lib/dracut/hooks/initqueue/finished/devexists-\x2fdev\x2fdisk\x2fby-uuid\x2f910678ff-f77e-4a7d-8d53-86f2ac47a823.sh: "if ! grep -q After=remote
-fs-pre.target /run/systemd/generator/systemd-cryptsetup@*.service 2>/dev/null; then
[  193.954846] dracut-initqueue[682]:     [ -e "/dev/disk/by-uuid/910678ff-f77e-4a7d-8d53-86f2ac47a823" ]
[  193.740701] dracut-initqueue[682]:     [ -e "/dev/disk/by-uuid/910678ff-f77e-4a7d-8d53-86f2ac47a823" ]
[  193.958237] dracut-initqueue[682]: fi"
[  193.743314] dracut-initqueue[682]: fi"

Because we set root uuid = 
