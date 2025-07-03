#!/bin/bash


if [[ ! -d "secureboot" ]]; then
    echo "Generating test Secure Boot keys"
    mkdir secureboot
    pushd secureboot > /dev/null
    uuidgen --random > GUID.txt
    openssl req -newkey rsa:4096 -nodes -keyout PK.key -new -x509 -sha256 -days 3650 -subj "/CN=Test Platform Key/" -out PK.crt
    openssl x509 -outform DER -in PK.crt -out PK.cer
    openssl req -newkey rsa:4096 -nodes -keyout KEK.key -new -x509 -sha256 -days 3650 -subj "/CN=Test Key Exchange Key/" -out KEK.crt
    openssl x509 -outform DER -in KEK.crt -out KEK.cer
    openssl req -newkey rsa:4096 -nodes -keyout db.key -new -x509 -sha256 -days 3650 -subj "/CN=Test Signature Database key/" -out db.crt
    openssl x509 -outform DER -in db.crt -out db.cer
    popd > /dev/null
fi

sbsign --key secureboot/db.key --cert secureboot/db.crt \
    ./uki.efi \
    --output uki-signed.efi
