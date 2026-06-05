## Check signatures in binaries 

```bash
# Grub
$ sbverify --list grubx64.efi

signature 1
image signature issuers:
 - /CN=CentOS Secure Boot CA 8/emailAddress=security@centos.org
image signature certificates:
 - subject: /CN=CentOS Secure Boot Signing 802/emailAddress=security@centos.org
   issuer:  /CN=CentOS Secure Boot CA 8/emailAddress=security@centos.org

# Shim
$ sbverify --list shimx64.efi

warning: data remaining[908096 vs 1036104]: gaps between PE/COFF sections?
signature 1
image signature issuers:
 - /C=US/ST=Washington/L=Redmond/O=Microsoft Corporation/CN=Microsoft Corporation UEFI CA 2011
image signature certificates:
 - subject: /C=US/ST=Washington/L=Redmond/O=Microsoft Corporation/CN=Microsoft Windows UEFI Driver Publisher
   issuer:  /C=US/ST=Washington/L=Redmond/O=Microsoft Corporation/CN=Microsoft Corporation UEFI CA 2011
 - subject: /C=US/ST=Washington/L=Redmond/O=Microsoft Corporation/CN=Microsoft Corporation UEFI CA 2011
   issuer:  /C=US/ST=Washington/L=Redmond/O=Microsoft Corporation/CN=Microsoft Corporation Third Party Marketplace Root
signature 2
image signature issuers:
 - /C=US/O=Microsoft Corporation/CN=Microsoft UEFI CA 2023
image signature certificates:
 - subject: /C=US/ST=Washington/L=Redmond/O=Microsoft Corporation/CN=Microsoft UEFI CA 2023 signer
   issuer:  /C=US/O=Microsoft Corporation/CN=Microsoft UEFI CA 2023
 - subject: /C=US/O=Microsoft Corporation/CN=Microsoft UEFI CA 2023
   issuer:  /C=US/O=Microsoft Corporation/CN=Microsoft RSA Devices Root CA 2021
```

## Get vendor cert section from shim

- shim_cert.pem
The X509 certificate embedded in shim, used to verify the images either directly or indirectly loaded by shim.

- shim_cert.key
The private key corresponding to shim_cert.pem, used to sign the images either directly or indirectly loaded by shim.

- vendor_cert.pem
Used in the same way as shim_cert.pem. In addition, vendor certificate is the switch to enable shim verification protocol, which facilitates the verification for the SELoader.

- vendor_cert.key
The private key corresponding to vendor_cert.pem, Same fuction as shim_cert.key.

```bash
objcopy --dump-section .vendor_cert=vendor_cert.bin shimx64.efi

# Get cert header
# NOTE: binwalk is pattern based and can produce bad results
# In this case the second result is not a valid cert
$ binwalk vendor_cert.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
60            0x3C            Certificate in DER format (x509 v3), header length: 4, sequence length: 866
974           0x3CE           Certificate in DER format (x509 v3), header length: 4, sequence length: 1372


# Extract the certs
dd if=vendor_cert.bin of=cert1.der bs=1 skip=60 count=886
dd if=vendor_cert.bin of=cert2.der bs=1 skip=974 count=1372 # this one is not valid
                                                            # Openssl throws "Could not find certificate from cert2.der"


# Getting openssl to inform about the certs
openssl x509 -inform DER -in cert1.der -text -noout

# Extract .pem from cert1.der
openssl x509 -inform DER -in cert1.der -out cert1.pem

# Use sbverify to verify integrity
sbverify --cert cert1.pem grubx64.efi
```

# ================= DER vs PEM ===========================

Encodings not different certificate types. The same certificate can exist as either.

### DER (Distinguished Encoding Rules)

- Binary ASN.1 encoding.
- Looks like garbage in a text editor.
 
### PEM (Privacy-Enhanced Mail)

- Base64 representation of DER.

Looks like:

```rust
-----BEGIN CERTIFICATE-----
MIIC3DCCAcSgAwIBAg...
...
-----END CERTIFICATE-----
```

PEM is just:

Base64(DER)

Many OpenSSL tools prefer PEM.

Convert:

```bash
openssl x509 -inform DER -in cert.der -out cert.pem
```

or back:

```bash
openssl x509 -inform PEM -outform DER \
    -in cert.pem -out cert.der
```
