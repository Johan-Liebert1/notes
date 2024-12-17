Used to allow applications to connect to the K8s cluster.

Helpful for path based routing, example /api/books can be redirected to service books-svc, /api/movies can be redirected to service movies-svc.

Ingresses can also act as LBs.
Can be used for SSL termination.

Ingress controllers are required to manage ingress resources.

Any ingress controller will create a Service of type LoadBalancer and have a public IP. We can create DNS record for that public IP.

If more than one rule match, the longer match is preferred.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
    annotations:
        nginx.ingress.kubernetes.io/proxy-read-timeout: "86400"
        nginx.ingress.kubernetes.io/proxy-send-timeout: "86400"
spec:
    ingressClassName: nginx
    rules:
        - host: uuid.apps.example.live # Domain based routing
          # We have multiple paths. This is called fanout
          http:
              paths:
                  - backend:
                        service:
                            name: svc-1
                            port:
                                number: 1234
                    path: /
                    pathType: Prefix

                  - backend:
                        service:
                            name: svc-2
                            port:
                                number: 5678
                    path: /api
                    pathType: Prefix

        - host: uuid-8080.apps.example.live # Another domain based route
          http:
              paths:
                  - backend:
                        service:
                            name: svc-3
                            port:
                                number: 8080
                    path: /
                    pathType: Prefix

    tls:
        - hosts:
              - uuid.apps.example.live
        - hosts:
              - uuid-8080.apps.example.live
status:
    loadBalancer:
        ingress:
            - ip: 20.219.180.220
```
