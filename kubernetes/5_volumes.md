On-disk files in a container are ephemeral, which presents some problems for non-trivial applications when running in containers.
One problem occurs when a container crashes or is stopped.
Container state is not saved so all of the files that were created or modified during the lifetime of the container are lost.
During a crash, kubelet restarts the container with a clean state.
Another problem occurs when multiple containers are running in a Pod and need to share files. 

# Static Provisioning and Dynamic Provisioning

In Static Provisioning we already have Volumes provisioned and any pod that claims a volume will get one from this pool, provided all conditions match.

Storage Requirement
If we have 3 volumes of 5GB, and a pod asks for 6GB then that won't work with Static Provisioning.

Access Mode
Specifies how many clients can read/write a volume.
RW many - can be used (can be mounted) my multiple client for read/write
RO many - may clients can read but not write
RW only - only one client can read/write

Volumes are claimed by pods/containers.

Provisioning is handled by Persistent Volume controller.


In Dynamic Provisioning we need to enable it on the cluster.

# Storage Class

