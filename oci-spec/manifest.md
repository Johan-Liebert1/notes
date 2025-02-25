Save an image as tar archive

```sh
podman images

REPOSITORY                                 TAG         IMAGE ID      CREATED            SIZE
localhost/test                             latest      d5fb4ee62789  About an hour ago  4.51 MB

# Save the `localhost/test` image
podman save --format oci-archive -o test-docker.tar "d5fb4ee62789"
```

Extract the file `test-docker.tar`. Review contents

```sh
.
├── blobs
│   └── sha256
│       ├── 06f89e4548f8744f6fc4ec9c9b21b6f86b0745423cd0e17dca0b227fb4683bdf
│       ├── 54b9607e19cdd0045cd6d2b12b04563fd1c9784bf1e378df9f7582f23c757e84
│       ├── 6b019f48672447f54180353cc2feedc243928a647779e8ee0a40ba6636d6bbe6
│       └── d5fb4ee62789ac7112258a466e1bc76aae44db25d2c62b5bac7ada533b028644
├── index.json
└── oci-layout

3 directories, 6 files
```

Contents of `index.json`

```json
{
  "schemaVersion": 2,
  "manifests": [
    {
      "mediaType": "application/vnd.oci.image.manifest.v1+json",
      "digest": "sha256:06f89e4548f8744f6fc4ec9c9b21b6f86b0745423cd0e17dca0b227fb4683bdf",
      "size": 885
    }
  ]
}
```


This tells us that the `manifest` file is in `blobs/06f89e4548f8744f6fc4ec9c9b21b6f86b0745423cd0e17dca0b227fb4683bdf`.

```json
# manifest file
{
    "schemaVersion": 2,
    "mediaType": "application/vnd.oci.image.manifest.v1+json",

    # Also called descriptor
    "config": {
        "mediaType": "application/vnd.oci.image.config.v1+json",
        # Points to another file inside blobs/sha256
        "digest": "sha256:d5fb4ee62789ac7112258a466e1bc76aae44db25d2c62b5bac7ada533b028644",
        "size": 658
    },

    "layers": [
        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "digest": "sha256:6b019f48672447f54180353cc2feedc243928a647779e8ee0a40ba6636d6bbe6",
            "size": 2280485
        },

        {
            "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
            "digest": "sha256:54b9607e19cdd0045cd6d2b12b04563fd1c9784bf1e378df9f7582f23c757e84",
            "size": 249
        }
    ],

    "annotations": {
        "org.opencontainers.image.base.digest": "sha256:42279ede3600b4e63af075a5e27d68232ff837d9cdcaba74feffc7ab0dfec0dc",
        "org.opencontainers.image.base.name": "docker.io/library/busybox:latest",
        "org.opencontainers.image.url": "https://github.com/docker-library/busybox",
        "org.opencontainers.image.version": "1.37.0-glibc"
    }
}
```

## Config

File `blobs/sha256:d5fb4ee62789ac7112258a466e1bc76aae44db25d2c62b5bac7ada533b028644` 
(Value of `digest` field in the `config` object of the `manifest`)

Basically this is the config. The SHA256 hash of this config json is the image id

```json
{
    "created": "2025-02-25T06:21:05.420489881Z",
    "architecture": "amd64",
    "os": "linux",
    "config": {
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "Cmd": [
            "sh"
        ],
        "Labels": {
            "io.buildah.version": "1.38.1"
        }
    },
    "rootfs": {
        "type": "layers",
        "diff_ids": [
            # This is the SHA sum of the Layer0, but when it's uncompressed
            "sha256:59654b79daad74c77dc2e28502ca577ba8ce73276720002234a23fc60ee92692",

            # This is the SHA sum of the Layer1, but when it's uncompressed
            # Layer1, is the diff between Layer0, and Layer1,
            "sha256:141c9c2f7ac15d28b51c83177265c84f9771c3ea8159f4e7383735b76110b764"
        ]
    },
    "history": [
        {
            "created": "2024-09-26T21:31:42Z",
            "created_by": "BusyBox 1.37.0 (glibc), Debian 12"
        },
        {
            "created": "2025-02-25T06:21:05.421234067Z",
            "created_by": "/bin/sh -c echo \"hello\" | tee /hello.txt",
            "comment": "FROM docker.io/library/busybox:latest"
        }
    ]
}
```


## Layers

There are two layers in the image, viz

```json
"layers": [
    {
        "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
        "digest": "sha256:6b019f48672447f54180353cc2feedc243928a647779e8ee0a40ba6636d6bbe6",
        "size": 2280485
    },

    {
        "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",
        "digest": "sha256:54b9607e19cdd0045cd6d2b12b04563fd1c9784bf1e378df9f7582f23c757e84",
        "size": 249
    }
]
```

Both of these are in the blobs folder

```sh

ls -lah blobs/sha256


total 2.2M
-rw-r--r--. 1 ppoudyal ppoudyal  885 Feb 25 12:52 06f89e4548f8744f6fc4ec9c9b21b6f86b0745423cd0e17dca0b227fb4683bdf  # manifest
-rw-r--r--. 1 ppoudyal ppoudyal  249 Feb 25 12:52 54b9607e19cdd0045cd6d2b12b04563fd1c9784bf1e378df9f7582f23c757e84  # Layer 1
-rw-r--r--. 1 ppoudyal ppoudyal 2.2M Feb 25 12:52 6b019f48672447f54180353cc2feedc243928a647779e8ee0a40ba6636d6bbe6  # Layer 0, from the `FROM` line
-rw-r--r--. 1 ppoudyal ppoudyal  658 Feb 25 12:52 d5fb4ee62789ac7112258a466e1bc76aae44db25d2c62b5bac7ada533b028644  # config
```

These layers are gzipped archives. Layer0, `6b01` is busybox and contains the entire contents of that.  

The dockerfile is 


```dockerfile
FROM busybox

RUN echo "hello" | tee /hello.txt
```

Two commands so two layers. We can unzip the `Layer 1`

```sh
gunzip -c 54b9607e19cdd0045cd6d2b12b04563fd1c9784bf1e378df9f7582f23c757e84 > layer.tar
tar -xf layer.tar --directory layer1

# After unzipping
tree layer1

layer1
├── etc
│   ├── hostname
│   ├── hosts
│   └── resolv.conf
├── hello.txt # The file we created
├── proc
├── run
└── sys

5 directories, 4 files
```



