# Run a container registry locally

```bash
podman run -d -p 5000:5000 --name registry registry:2
podman tag "<image-id>" localhost:5000/image-name
podman push localhost:5000/image-name
```

# Create the following file to allow insecure registry pulling

```bash
touch /etc/containers/registries.conf.d/insecure-registry.conf
```

```toml
[[registry]]
location = "localhost:5000"
insecure = true
```
