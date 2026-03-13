# cat files with names

```bash
find . -type f -exec sh -c 'for f; do echo "==> $f <=="; cat "$f"; echo; done' _ {} +
```

# copy file from podman container

```bash
podman cp <container_id>:/path/in/container /path/on/host
```

```bash
PS1="\[\e[32m\]\u@\h:\[\e[36m\]\w:\[\e[0m\]\$ "

PS1="\[\e[32m\]ostree:\[\e[36m\]\w:\[\e[0m\]\$ "

PS1="\[\e[32m\]composefs:\[\e[36m\]\w:\[\e[0m\]\$ "
```

# building ostree

```bash
./configure --prefix=/usr --disable-libsoup-client-certs --disable-libsoup
make && make install DESTDIR=/home/pragyan/RedHat/ostree/usr
```
