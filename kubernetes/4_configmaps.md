# Configmaps

They are basically key/value stores. Have some config for a pod, like DB host, port, username etc.

We can also, in the pod spec, specify that some env should come configmap.

We can also mount configmaps as a volume inside a pod.

When we update a config map, if it is mounted as a volume, kubelet will sync and the pod will see new values.
But, configmaps set as ENV are not updated.

Configmaps are not available across namespaces.

```yaml
# Configmap
apiVersion: v1
kind: ConfigMap
metadata:
    name: example-config
    namespace: default
data:
    # File like config maps. Can be used to set configmap as a file
    app_properties: |
        key1=value1
        key2=value2

    log_level: "DEBUG"
```

```yaml
# Pod
apiVersion: v1
kind: Pod
metadata:
    name: example-pod
    namespace: default
spec:
    containers:
        - name: app-container
          image: busybox
          command: ["sh", "-c", "cat /etc/config/app.properties && sleep 3600"]

          volumeMounts:
              - name: config-volume
                mountPath: /etc/config

        # Using confimaps as env vars
        - env:
              - name: LOG_LEVEL
                valueFrom:
                    configMapKeyRef:
                        name: example-config # The configmap this value comes from
                        key: log_level # The key to fetch

    # Mounting the configmap as a volume
    volumes:
        - name: config-volume
          configMap: # The volume is going to be a configmap
              name: example-config

              # if we don't specify this list, the entire configmap will be mounted as a volume
              items:
                  - key: app_properties
                    path: app_properties
```


# Secrets

Similar to configmaps but are base64 encoded.
Nothing is encypted. We can use these similar to confimaps.
