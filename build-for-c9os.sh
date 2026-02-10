#!/bin/bash

podman run --rm -it --workdir /bootc --security-opt label=disable -v /home/pragyan/RedHat/bootc:/bootc:rw localhost/bootc-centos9-debug:latest bash # cargo b --release
