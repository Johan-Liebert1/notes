what does it mean conf cluster
we want to be able to run some workload and have reasonable guarantee that what we are running are what we want to have run
like the os we are runnig are the version of os we are running, meaning cloud provider hasn't updated it
relying on smv/smp for amd. the motherboard will encrypt of the system  
this makes os hypervisor difficult to look inside a VM


how to know if VM is running under smv/smp? it could be faked by the provider
this is where remote attestation comes into the picture

there is an API for this attestation

this is testing if we are running in smv/smp


we send some random data to VM, and ask the VM to ask the processor to sign it. We have public key


^^ this is for hardware, but it doesn't tell us about the OS


now we have TPM for the booting part. We have nonce value and send it to remote system which sends it to the tpm

shim -> systemd boot -> uki

tpm2_pcrread

if tpm logs give the same value as tpm2_pcrread then it's correct

we also need LUKS

hardware security module for uki signing



how does the API work.
what's the diff btw erofs and btrfs with ro mode
