# Control plane components
1. Etcd
2. Kube API server
3. Controller manager (node contorller, replication controller, deployment controller etc)
4. Kube Scheduler

5. Worker and master nodes
6. Container Runtime Engine (CRE) Docker, Containerd
7. Kubelet. Runs on each node in the server. Kube API server periodically fetches info from kubelet to monitor nodes and containers on them
8. kube-proxy service. Allows containers/pods to reach each other

When API server gets a request, it'll store it in Etcd. API server is the entrypoint.

Controller and Scheduler check with API server if there are requests in queue. 
Controller manager tries to match the current state of the cluster with the requested state, i.e. try to make it eventually consistent.

If say only 2 replicas of a Pod are running when 3 were asked, contorller manager (or a subset of controller manager) will try to increase the replicas. This is called reconciliation.

Both the scheduler and controllers operate in reconciliation loops, where they compare the actual state of the cluster to the desired state and take action to resolve discrepancies.

The Scheduler and Controllers use watches to establish a long-lived connection to the API server.
Kubernetes uses informers (built on top of watches) to cache API server data locally in memory.

Controller manager contains all controllers
- Deployment controller
- Replicaset controller
- Daemonset controller
- Service controller


Kube Scheduler will specify on the pod itself, that this pod should be scheduled on, say, Node/Worker 1. It does not schedule, only mention which node this can be scheduled on.


### Worker node components (Are present in all worker nodes)
1. Kubelet
2. Kube Proxy

Now, scheduler has updated the pod manifest with the scheduling information. Kubelet talks to the API server, sees that a pod has been scheduled on its node. 
It talks to the CRI (Container Runtime Interface) to run the container.

## Setting up a k8s cluster
Now, how do we run API server, Controller manager etc as pods when there is no cluster. We use static pods or we can use linux services.
