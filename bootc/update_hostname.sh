#!/bin/bash

set -eux

ip=$1
name=$2

if grep -q "$name" /etc/hosts; then
    # already exists
    sudo sed -i "\;$name;c\\$ip $name" /etc/hosts
else
    echo "$ip $name" | sudo tee -a /etc/hosts
fi
