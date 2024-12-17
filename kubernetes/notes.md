# Why use service?

Service

```yaml
apiVersion: v1
kind: Service
metadata:
    labels:
        type: ClusterIP
        user-app-operator/controlled-by: cluster-westeuropespot-prod
        uuid: default-uuid
    name: cluster-25970774-vmss00001l-1-service
    namespace: ni-prod
spec:
    clusterIP: 10.0.133.108
    clusterIPs:
        - 10.0.133.108
    internalTrafficPolicy: Cluster
    ipFamilies:
        - IPv4
    ipFamilyPolicy: SingleStack
    ports:
        - name: signalling
          port: 30001
          protocol: TCP
          targetPort: 30001
        - name: 8080-tcp
          port: 8080
          protocol: TCP
          targetPort: 8080
        - name: 3000-tcp
          port: 3000
          protocol: TCP
          targetPort: 3000
        - name: container-commit-service
          port: 3200
          protocol: TCP
          targetPort: 3200
    selector:
        deployment-name: cluster-25970774-vmss00001l-1-deployment
    sessionAffinity: None
    type: ClusterIP
status:
    loadBalancer: {}
```

# Control plane components
1. Etcd
2. Kube API server
3. Worker and master nodes
4. Container Runtime Engine (CRE) Docker, Containerd
5. Controller manager (node contorller, replication controller, deployment controller etc)
6. Kubelet. Runs on each node in the server. Kube API server periodically fetches info from kubelet to monitor nodes and containers on them
7. kube-proxy service. Allows containers/pods to reach each other
