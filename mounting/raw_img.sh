# mount .img file

# find out partitions
fdisk -l test.img

# setup loopback device
sudo losetup /dev/loop0 test.img 

# set up partitions
sudo partprobe /dev/loop0

# mount the wanted partition
sudo mount /dev/loop0p2 /mnt

# detach the loopdev
sudo losetup -d /dev/loop0
