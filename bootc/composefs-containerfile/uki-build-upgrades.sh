#!/bin/bash

set -uex

NUM_IMAGES=$1

for ((i=0; i<NUM_IMAGES; i++)); do
    sudo ./uki-build.sh "localhost/uki-upgrade${i}" ./Containerfile.uki.bootc "upgrade${i}"
done
