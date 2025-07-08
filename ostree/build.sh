podman run --rm \
    -v /home/pragyan/RedHat/ostree:/ostree:rw,Z \
    -w /ostree \
    localhost/ostree-builder \
    bash -c 'cd /ostree && ./autogen.sh && \
            ./configure --prefix=/ostree/usr && \
            make && \
            make install DESTDIR=/ostree/usr'
