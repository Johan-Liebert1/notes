set -eux

echo "Starting three devices partial ESP test"

vg_name="test_three_dev_vg"
mountpoint="/var/mnt/test_three_dev"
disk1="/var/tmp/disk1_three.img"
disk2="/var/tmp/disk2_three.img"
disk3="/var/tmp/disk3_three.img"

# Setup disks
# DISK1: ESP + LVM partition
# DISK2: Full LVM partition (no ESP)
# DISK3: ESP + LVM partition
loop1=$(setup_disk_with_partitions $disk1 true)
loop2=$(setup_disk_with_partitions $disk2 false)
loop3=$(setup_disk_with_partitions $disk3 true)

# Create LVM spanning all three devices
pvcreate $"($loop1)p2" $"($loop2)p1" $"($loop3)p2"
vgcreate $vg_name $"($loop1)p2" $"($loop2)p1" $"($loop3)p2"
lvcreate -l "100%FREE" -n test_lv $vg_name

let lv_path=$"/dev/($vg_name)/test_lv"

# Create filesystem and mount
mkfs.ext4 -q $lv_path
mkdir $mountpoint
mount $lv_path $mountpoint

# Create boot directory
mkdir $"($mountpoint)/boot"

# Show block device hierarchy
lsblk --pairs --paths --inverse --output NAME,TYPE $lv_path

run_install $mountpoint

# Validate ESP installed on disk1 and disk3, disk2 has no ESP
validate_esp $"($loop1)p1"
validate_esp $"($loop3)p1"

# Cleanup
cleanup $vg_name ["$loop1", "$loop2", "$loop3"] $mountpoint
rm -f $disk1 $disk2 $disk3

echo "Three devices partial ESP test completed successfully"
