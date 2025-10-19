#!/bin/bash

set -u

REPO_PATH=$1

objects="$REPO_PATH/objects"

for file in $(find "$objects" -type f); do
    file_name=$(echo "$file" | awk -F/ '{print $NF}')

    file_type=$(file "$file")

    file_path=$file
    
    if [[ $(echo "$file_type" | grep zstd) == 0 ]]; then
        zstd -d "$file" -o "/tmp/$file_name"
        file_path="/tmp/$file_name"
    fi

    if [[ $(grep thing "$file_path") == 0 ]]; then 
        echo "Found in $file_path"
    else
        if [[ -f "/tmp/$file_name" ]]; then
            rm -f "/tmp/$file_name"
        fi
    fi
done
