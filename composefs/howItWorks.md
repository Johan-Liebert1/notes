# From a container
We take an OCI container image and split it into splitstreams.

Each splitstream's name is its own `fs-verity` digest.

## The filesystem layout

```bash
sysroot
├── composefs
│   ├── images
│   │   └── 15ba6ca9c42948ee95ef77750d44414cc73f81c07391146cd4b35f73b3a84cf4 -> ../objects/15/ba6ca9c42948ee95ef77750d44414cc73f81c07391146cd4b35f73b3a84cf4
│   ├── objects
│   │   ├── 00
│   │   ├── 01
│   │   ├── ..
│   │   ├── ..
│   │   └── ff
│   └── streams
│       ├── 2b25234ed00e46b639556d8c3885aff7561d54acef01cdee37d9d544b727271d -> ../objects/2c/720fbd37cbceecac5ddd4743f00eb3b3038722024bc400db06dda714a077c1
│       ├── 4742bf6e92741468887eff046764c81ecb9f72f94524781e4a10bc161075d21e -> ../objects/ef/e80157d3ceb38f0fbc2e01b961b6a2cafb4787c0e0a8eb5dbee59048561493
│       ├── 552ff06f421efcd2b29abb67a14f9a95935e06e8d62e33d4c312846a231faa0a -> ../objects/08/816d61468d0ee5bf389e167d98ab488c82c0c0b6e60057652d1f7833bbfdf9
│       ├── 8e430830d2460dc0bc13fa8824feb183708aa4c1500044a9d6c1222846df6d0e -> ../objects/b6/bd2d0c2eb75ff3cf8cef0cf6ea68ba65de371423082769cc2aa08e6b9c287f
│       ├── e94a6a7415decc92201d6ce06244df1956b2c0b42bfd39a8ed01c3e7d6478f35 -> ../objects/dd/7f22c45e5e96f894d7d499b15c8349afd2327fb2e4695ae2d1ccaf081303ec
│       └── f2c27bde537d43d7b05bdfc382e07211380f660af2cf03847a5c98c423f5f347 -> ../objects/3b/44f95cf2f941984b34d0d8f1420c91fc625703c3062ac1fb8bda6869e7ae8a
└── state
    └── 15ba6ca9c42948ee95ef77750d44414cc73f81c07391146cd4b35f73b3a84cf4
        ├── etc
        └── var
```

The above is made using the following image 

```dockerfile
FROM fedora:41
COPY extra /
RUN --mount=type=cache,target=/var/cache/libdnf5 <<EOF
    set -eux

    dnf --setopt keepcache=1 install --allowerasing -y \
        composefs \
        dosfstools \
        kernel \
        openssh-server \
        skopeo \
        strace \
        util-linux \
        systemd

    systemctl enable systemd-networkd
    passwd -d root
    mkdir /sysroot
EOF
COPY cfsctl /usr/bin
```

Which has the following layers

```json
"RootFS": {
   "Type": "layers",
   "Layers": [
        "sha256:2b25234ed00e46b639556d8c3885aff7561d54acef01cdee37d9d544b727271d",
        "sha256:4742bf6e92741468887eff046764c81ecb9f72f94524781e4a10bc161075d21e",
        "sha256:552ff06f421efcd2b29abb67a14f9a95935e06e8d62e33d4c312846a231faa0a",
        "sha256:e94a6a7415decc92201d6ce06244df1956b2c0b42bfd39a8ed01c3e7d6478f35",
        "sha256:f2c27bde537d43d7b05bdfc382e07211380f660af2cf03847a5c98c423f5f347",
   ]
},
```

All of these layers are present in the `sysroot/composefs/streams` directory

```bash
└── streams
    ├── 2b25234ed00e46b639556d8c3885aff7561d54acef01cdee37d9d544b727271d -> ../objects/2c/720fbd37cbceecac5ddd4743f00eb3b3038722024bc400db06dda714a077c1
    ├── 4742bf6e92741468887eff046764c81ecb9f72f94524781e4a10bc161075d21e -> ../objects/ef/e80157d3ceb38f0fbc2e01b961b6a2cafb4787c0e0a8eb5dbee59048561493
    ├── 552ff06f421efcd2b29abb67a14f9a95935e06e8d62e33d4c312846a231faa0a -> ../objects/08/816d61468d0ee5bf389e167d98ab488c82c0c0b6e60057652d1f7833bbfdf9
    ├── 8e430830d2460dc0bc13fa8824feb183708aa4c1500044a9d6c1222846df6d0e -> ../objects/b6/bd2d0c2eb75ff3cf8cef0cf6ea68ba65de371423082769cc2aa08e6b9c287f
    ├── e94a6a7415decc92201d6ce06244df1956b2c0b42bfd39a8ed01c3e7d6478f35 -> ../objects/dd/7f22c45e5e96f894d7d499b15c8349afd2327fb2e4695ae2d1ccaf081303ec
    └── f2c27bde537d43d7b05bdfc382e07211380f660af2cf03847a5c98c423f5f347 -> ../objects/3b/44f95cf2f941984b34d0d8f1420c91fc625703c3062ac1fb8bda6869e7ae8a
```

The files they point to have, `splitstreams`, not actual data but they have maps pointing to each and every file in the particular layer


## The EROFS Image

In the `sysroot/composefs/images` directory, we have the `EROFS` image created using the container image

```bash
├── composefs
│   ├── images
│   │   └── 15ba6ca9c42948ee95ef77750d44414cc73f81c07391146cd4b35f73b3a84cf4 -> ../objects/15/ba6ca9c42948ee95ef77750d44414cc73f81c07391146cd4b35f73b3a84cf4


file ../objects/15/ba6ca9c42948ee95ef77750d44414cc73f81c07391146cd4b35f73b3a84cf4

../objects/15/ba6ca9c42948ee95ef77750d44414cc73f81c07391146cd4b35f73b3a84cf4: EROFS filesystem, compat: MTIME, blocksize=12, exslots=0, uuid=00000000-0000-0000-0000-000000000000
```


This `EROFS` image is created by the `cfsctl` binary.

### Mounting the EROFS image

```bash
cp  ../objects/15/ba6ca9c42948ee95ef77750d44414cc73f81c07391146cd4b35f73b3a84cf4 ~/erofs-image
mount -t erofs ~/erofs-image /mnt

# We can see it contains metadata about the filesystem
ls /mnt

total 96K
dr-xr-xr-x  20 root root  401 Apr 30 14:02 ./
dr-xr-xr-x.  1 root root  180 Apr  9 17:49 ../
dr-xr-xr-x   2 root root   27 Jul 17  2024 afs/
lrwxrwxrwx   1 root root    7 Jul 17  2024 bin -> usr/bin/
drwxr-xr-x   2 root root   27 Apr 30 14:02 boot/
drwxr-xr-x   3 root root   43 Apr 30 14:02 composefs-meta/
drwxr-xr-x   2 root root   27 Apr 30 11:18 dev/
drwxr-xr-x  60 root root 4.0K Apr 30 14:02 etc/
drwxr-xr-x   2 root root   27 Jul 17  2024 home/
lrwxrwxrwx   1 root root    7 Jul 17  2024 lib -> usr/lib/
lrwxrwxrwx   1 root root    9 Jul 17  2024 lib64 -> usr/lib64/
drwxr-xr-x   2 root root   27 Jul 17  2024 media/
drwxr-xr-x   2 root root   27 Jul 17  2024 mnt/
drwxr-xr-x   2 root root   27 Jul 17  2024 opt/
drwxr-xr-x   2 root root   27 Apr 30 11:18 proc/
-rw-r--r--   1 root root 1.1K Apr 30 11:18 .profile
drwxr-xr-x   3 root root  148 Apr 27 10:18 root/
drwxr-xr-x  15 root root  272 Apr 30 14:02 run/
lrwxrwxrwx   1 root root    8 Jul 17  2024 sbin -> usr/sbin/
drwxr-xr-x   2 root root   27 Jul 17  2024 srv/
drwxr-xr-x   2 root root   27 Apr 30 11:18 sys/
drwxr-xr-x   2 root root   27 Apr 30 14:02 sysroot/
drwxrwxrwt   2 root root   27 Apr 30 14:02 tmp/
drwxr-xr-x  12 root root  209 Apr 27 10:18 usr/
drwxr-xr-x  18 root root  332 Apr 30 11:18 var/
```

The files are stored sparsely. What does that mean? This means that the file metadata, size, creation time etc, is all 
correct in the EROFS image, but the data is all NULL, i.e. all `\0` bytes.

NOTE: We mask out `/boot` while creating the erofs image

```bash
ls -lah ./composefs-meta/boot/loader/entries/d594b915350142a5ab0f5a80a9c6316c-6.14.4-200.fc41.x86_64.conf

-rw-r--r-- 1 root root 496 Apr 30 14:02 ./composefs-meta/boot/loader/entries/d594b915350142a5ab0f5a80a9c6316c-6.14.4-200.fc41.x86_64.conf


# Looking inside this file

hexdump ./composefs-meta/boot/loader/entries/d594b915350142a5ab0f5a80a9c6316c-6.14.4-200.fc41.x86_64.conf

0000000 0000 0000 0000 0000 0000 0000 0000 0000
*
00001f0
```

That's how redirect files work in the overlayfs setup.
The upper files must be the correct size but are stored sparse
If we look at the xattrs we'll see the redirect attribute


## Overall layout concept

The composefs header and superblock are the only things that need to be at
fixed offsets.

Generally speaking, we perform these steps:
*    collect the filesystem into a flat list of inodes
*    collect and "share" xattrs, as appropriate
*    write the composefs header and the superblock
*    write the inodes directly following the superblock
*    write the shared xattrs directly following the inodes
*    then the blocks (only for directories)


## Collecting inodes

We collect the inodes into a flat list according to the following algorithm:
*   our goal is to visit each inode, collecting it into the inode list as we
    visit it, in the order that we visited it
*   start at the root directory
*   for each directory that we visit:
    -   the directory is stored first, then the children
    -   we visit the children in asciibetical order, regardless of file type
        (ie: we interleave directories and regular files)
    -   when visiting a child directory, we store all content of the child
        directory before returning to the parent directory (ie: depth first)
*   in the case of hardlinks, the inode gets added to the list at the spot that
    the first link was encountered

Consider a filesystem tree

```sh
 /
   bin/
     cfsctl
   usr/
     lib/
       libcomposefs.so
       libglib-2.0.so
     libexec/
       cfsctl
```

where `/bin/cfsctl` and `/usr/libexec/cfsctl` are hardlinks.

In that case, we'd collect the inodes in this order:
1.  `/`
2.  `/bin/`
3.  `/bin/cfsctl` (aka `/usr/libexec/cfsctl`)
4.  `/usr/`
5.  `/usr/lib/`
6.  `/usr/lib/libcomposefs.so`
7.  `/usr/lib/libglib-2.0.so`
8.  `/usr/libexec/`

(skipping `/usr/libexec/ctlctl` because we already had it by the time we encountered it).

So that's 8 inodes, in that order.


