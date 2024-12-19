Purpose: Identifies and provides access to a pod.

Usage: When a pod runs, it uses a service account to authenticate with the Kubernetes API.

Default Behavior: Each namespace has a default service account, but you can create custom service accounts for specific workloads.

Service account controllers create a default service account for each namespaces.
Service account basically describe what an Application can access via the API server.

Service account will always refer to one or many secrets or to some Role binding.

If no secret is provided, these tokens are automatically mounted into pods at `/var/run/secrets/kubernetes.io/serviceaccount/token`.
Secrets are no longer needed to store these tokens as they are dynamically generated and managed by the API server.

We can create a role, and bind that role to the service account using rolebindings.

Example

Service Account

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
    name: my-service-acc
    namespace: my-ns
```

Role

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
    name: my-role
    namespace: my-ns
rules:
    - apiGroups:
          - extensions
          - apps
          - ""
          - networking.k8s.io
      resources:
          - replicasets
          - deployments
          - nodes
          - pods
          - services
          - ingresses
      verbs:
          - create
          - update
          - get
          - delete
          - list
```

Role Binding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
    name: my-rb
    namespace: my-ns
roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: Role
    name: my-role
subjects:
    - kind: ServiceAccount
      name: my-service-acc
      namespace: my-ns
```
