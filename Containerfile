FROM quay.io/centos-bootc/centos-bootc:stream9
RUN dnf install -y rust cargo
RUN dnf install -y openssl-devel
RUN dnf install -y tree
RUN passwd -d root
