#!/bin/bash

set -eux

# rm -rf /etc
# mkdir -p /etc/repart.d

# cat <<EOF > /etc/repart.d/00-bios.conf
# [Partition]
# Type=21686148-6449-6e6f-744e-656564454649
# Label=BIOS-BOOT
# SizeMinBytes=1M
# SizeMaxBytes=1M
# EOF

cat <<EOF > /etc/repart.d/00-esp.conf
[Partition]
Type=esp
Format=vfat
SizeMinBytes=1024M
SizeMaxBytes=1024M
EOF

cat <<'EOF'  > /etc/repart.d/01-root.conf
[Partition]
Type=root
Format=ext4
SizeMinBytes=7168M
SizeMaxBytes=7168M
EOF

cat <<'EOF'  > /etc/repart.d/20-home.conf
[Partition]
Type=home
Format=ext4
SizeMinBytes=1024M
SizeMaxBytes=1024M
EOF

cat <<'EOF' > /etc/repart.d/30-swap.conf
[Partition]
Type=swap
Format=swap
SizeMinBytes=100M
SizeMaxBytes=100M
EOF

cat <<'EOF' > /usr/repart.d/20-swap.conf
[Partition]
Type=swap
Format=swap
SizeMinBytes=100M
SizeMaxBytes=100M
EOF

truncate -s10G /etc/repart-disk.img

IGNORE_DEFS=()
# IGNORE_DEFS=("--include-partitions=root,esp,21686148-6449-6e6f-744e-656564454649")

systemd-repart --json=pretty --no-pager --dry-run=no --empty=force --root=/ /etc/repart-disk.img
