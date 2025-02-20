# ==================================== /etc/shadow =================================

- Stores user account information related to passwords. Access to this file is restricted for security reasons, as it contains sensitive data.

```bash
pragyan    :  $6$JS6z2tdz8bzzpsukklfjslkfjslfjsklfjslfjsdlfakasdfasf           :19615:0:99999:7:::

# username    hashed password (* or !) if account disabled or passwordless    password age, acc expiry etc
```


# ==================================== /etc/passwd =================================

- Stores basic information about user accounts.

```bash
pragyan:  x                      :1000:1000:pragyan:   /home/pragyan:     /bin/zsh

# name: password in /etc/shadow    uid  gid  userinfo   home dir       defaualt login shell
```


# ==================================== /etc/group =================================

- Stores group account information.

```bash
wheel:x:998:pragyan
audio:x:996:brltty,pragyan
input:x:994:brltty,pragyan
sudo:x:998:brltty,pragyan

# Group Name : Password Placeholder : Group ID : Comma separated group members
```


# =================================== /etc/fstab ===================================

Contains mount point information that's used in the boot process.


```bash
# Use 'blkid' to print the universally unique identifier for a device; this may
# be used with UUID= as a more robust way to name devices that works even if
# disks are added and removed. See fstab(5).

# <file system>                           <mount point>  <type>  <options>               <dump>  <pass>
UUID=7E03-D611                            /boot/efi      vfat    umask=0077                 0       2
UUID=57b9a314-3091-401a-8c58-e6d96b9019f9 swap           swap    defaults,noatime           0       0
UUID=50e8f28a-3a5c-4922-88ab-11e31f993299 /              ext4    defaults,noatime           0       1
UUID=f8260a25-008b-4f19-b968-2003e56c8a0c /home          ext4    defaults,noatime           0       2
tmpfs                                     /tmp           tmpfs   defaults,noatime,mode=1777 0       0
```


# ===================================== /etc/subuid | /etc/subgid ==================================

These contain information about subordinate UIDs and subordinate GIDs that a user is permitted to use in a user namespace.

```bash
# username:Subuid start:Subuid range
pragyan:1000:99
```

In the above example, the user `pragyan` is allowed to use UIDs 1000, 1001, 1002 ... 1098 in user namespaces.

If you run out of these UIDs, then creating users in user namespaces is not possible.

`/etc/subgid` serves a similar purpose but for GIDs


