# cat files with names

```bash
find . -type f -exec sh -c 'for f; do echo "==> $f <=="; cat "$f"; echo; done' _ {} +
```

# copy file from podman container

```bash
podman cp <container_id>:/path/in/container /path/on/host
```
