# Run a container registry locally

```bash
podman run -d -p 5000:5000 --name registry registry:2
podman tag "<image-id>" localhost:5000/image-name
podman push localhost:5000/image-name
```

# Create the following file to allow insecure registry pulling

```bash
cat > /etc/containers/registries.conf.d/insecure-registry.conf <<EOF
[[registry]]
location = "localhost:5000"
insecure = true
EOF

# If the above doesn't work
# This might override some stuff in the .conf file
cat >> /etc/containers/registries.conf <<EOF
[[registry]]
location = "localhost:5000"
insecure = true
EOF

# Virsh 
cat >> /etc/containers/registries.conf <<EOF
[[registry]]
location = "192.168.122.1:5000"
insecure = true
EOF
```

what the finalize should do

1. staged
2. /etc merge

3. maybe GC?
