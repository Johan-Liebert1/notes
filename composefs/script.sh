#!/bin/bash

set -u

REPO=./examples/bls/tmp/sysroot/composefs
CFSCTL=./target/release/cfsctl

function image_objects {
    local image=$1
    $CFSCTL --repo $REPO image-objects "$image"
}

function main {
    case "$1" in
        'image-objects')
            image_objects "$2"
        ;;
    esac
}

main "$@"
