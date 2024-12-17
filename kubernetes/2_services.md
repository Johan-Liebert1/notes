Services are used to facilitate communication between two pods in a load balanced and abstracted way.

frontend -> backend (IP which is ephemeral)
Ephemeral IPs are the problem

frontend -> service -> backend 1 (IP which is ephemeral)
|
-> backend 2 (IP which is ephemeral)
.
.

Endpoints are created by Services which links a service to a particular Pod's IP

```sh
kubectl get endpoints

NAME                                                        ENDPOINTS                                                           AGE

cluster-27948589-vmss000003-0-service                       10.224.0.151:8080,10.224.0.151:3000,10.224.0.151:3200 + 1 more...   7h40m

cluster-27948589-vmss000003-1-service                       10.224.0.143:8080,10.224.0.143:3000,10.224.0.143:3200 + 1 more...   7h40m
```

If we add more pods to a deployment to which a service is pointing to, the service controller will kick in and add the new pod's IP to the above list.
Controller will match the label defined in the service to check for Deployments/Pods.

If we don't pass selectors to service, then no endpoint resource will be created. We can then create an endpoint resource ourselves.
This is useful if we want to expose another services, say a SQL server, via Kubernetes.

## Accessing Services from Pods

Service DNS CName is of the form

```
service-name.namespace-name.cluster.local
```

DNS server should be installed in our cluster for this to be resolved. Like CoreDns

Types of services

-   ClusterIP:     CANNOT access from outside the cluster
-   NodePort:      CAN access from outside the cluster
-   LoadBalancer:  CAN access from outside the cluster
-   ExternalName : Used when you want the service to resolve to some external domain.

```yaml
apiVersion: v1
kind: Service
metadata:
    name: my-service
    namespace: prod
spec:
    type: ExternalName
    externalName: my.database.example.com
```

## Port forwarding localhost to some service

```sh
kubectl port-forward -n ni-dev svc/my-svc 8080
```

The above will make it so that any request to `:8080` will be proxied to service `svc/my-svc` on namespace `ni-dev`

