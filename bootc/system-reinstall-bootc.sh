#!/bin/bash

growpart /dev/vda 4
btrfs filesystem resize max /

sed -i '/PasswordAuthentication/c\PasswordAuthentication yes' /etc/ssh/sshd_config
sed -i '/PermitEmptyPasswords/c\PermitEmptyPasswords yes' /etc/ssh/sshd_config
sed -i '/PermitRootLogin/c\PermitRootLogin yes' /etc/ssh/sshd_config

systemctl restart sshd

cat >> /etc/containers/registries.conf <<EOF
[[registry]]
location = "192.168.122.1:5000"
insecure = true
EOF

curl http://192.168.122.1:8080/bootc -o bootc && chmod +x bootc

podman build -t bootc-bls-fix --file - . <<EOF
FROM 192.168.122.1:5000/bootc-bls
COPY bootc /usr/bin
EOF

curl http://192.168.122.1:8080/system-reinstall-bootc -o system-reinstall-bootc && chmod +x system-reinstall-bootc

export RUST_LOG=debug
./system-reinstall-bootc bootc-bls-fix
