```bash
# c\ means change the entire line. Notice how there is no 's' at the beginning as we're changing the entire line
sed -i '/PasswordAuthentication/c\PasswordAuthentication yes' /etc/ssh/sshd_config
sed -i '/PermitEmptyPasswords/c\PermitEmptyPasswords yes' /etc/ssh/sshd_config
sed -i '/PermitRootLogin/c\PermitRootLogin yes' /etc/ssh/sshd_config

systemctl restart sshd
```



cp -r /usr/lib/bootupd/updates/EFI /usr/lib/ostree-boot/efi/

cp -r /usr/efi/EFI /usr/lib/ostree-boot/efi/

rm -rf /usr/lib/bootupd/updates/EFI

/var/bootupd generate-update-metadata -vvv
