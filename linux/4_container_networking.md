### Run apache webserver in docker container and map 8080 to host to 80 in container

```bash
docker run -p 8080:80 -d httpd
```

We can see in network setting by doing `docker inspect <container_id>`

```json
"NetworkSettings": {
    "Ports": {
        "80/tcp": [
            {
                "HostIp": "0.0.0.0",
                "HostPort": "8080"
            },
            {
                "HostIp": "::",
                "HostPort": "8080"
            }
        ]
    },
    "Gateway": "172.17.0.1",
    "IPAddress": "172.17.0.2",
    // ... other fields
    "Networks": {
        // This container is in this network called bridge which is the default network
        // for all containers that docker creates
        "bridge": {
            "MacAddress": "02:42:ac:11:00:02",
            "NetworkID": "499dc11d60dd20287a1e2d405cdb8b5a4c0ea7539b06fa5b75abce34d56172e5",
            "EndpointID": "4a4d9b75de443437a94cf75bad8dd9d0dd7b9b19ffb1cdf88fa9ed94d7069696",
            "Gateway": "172.17.0.1",
            "IPAddress": "172.17.0.2", // IP Address of container
            "DNSNames": null
        }
        // ... other fields
    }
}
```

### Spin two more containers `s1` and `s2`

```bash
docker run --name s1 -d nhttpd
docker run --name s2 -d nhttpd
```

`docker inspect network bridge` Gives me

```json
{
    "Name": "bridge",
    "Id": "499dc11d60dd20287a1e2d405cdb8b5a4c0ea7539b06fa5b75abce34d56172e5",
    "Created": "2024-12-22T13:54:55.057310634+05:30",
    "Scope": "local",
    "Driver": "bridge",
    "IPAM": {
        "Driver": "default",
        "Options": null,
        "Config": [
            {
                "Subnet": "172.17.0.0/16",
                "Gateway": "172.17.0.1"
            }
        ]
    },
    "Containers": {
        "65c51120358b35b396947755b67a6968528e8c454e337d102a637b46bea3528f": {
            "Name": "s2",
            "EndpointID": "e8765e873e52f3c2c41c9c8addb79593b387f66c7509463d83d13529cd5fbbc3",
            "MacAddress": "02:42:ac:11:00:03",
            "IPv4Address": "172.17.0.3/16",
            "IPv6Address": ""
        },
        "a9841a3fc826fbc800de32511f44e09ae09a744dd1ad15a08e3804d6a26a6859": {
            "Name": "s1",
            "EndpointID": "274c39cb5dbc78784ad86f6a619389966c4e2d63bf1b6a311bfb4aac6e56e126",
            "MacAddress": "02:42:ac:11:00:02",
            "IPv4Address": "172.17.0.2/16",
            "IPv6Address": ""
        }
    },
    "Options": {
        "com.docker.network.bridge.default_bridge": "true",
        "com.docker.network.bridge.enable_icc": "true",
        "com.docker.network.bridge.enable_ip_masquerade": "true",
        "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
        "com.docker.network.bridge.name": "docker0",
        "com.docker.network.driver.mtu": "1500"
    },
}
```

Hostname of s1 = `a9841a3fc826`

We cannot resolve this hostname even from inside the containers as the DNS resolution query goes to the host
and the host does not have information for this network. We cannot access containers by hostname. 


### Accessing containers by hostname

- We'll create a docker network ourselves named `backend`

```bash
docker network create backend --subnet 10.0.0.0/24

# out c3cdfed3c816fd00d773a834c41cd90c7ecf393ffb1a28fc287fe7f51a2000ea
```

This network doesn't have any contianers right now. We'll connect `s1` and `s2` to it.

```bash
docker network connect backend s1
docker network connect backend s2
```

`s1` and `s1` now belong to two networks, and our network now has two containers

```json
"Networks": {
    "backend": {
        "IPAMConfig": {},
        "Links": null,
        "Aliases": [],
        "MacAddress": "02:42:0a:00:00:02",
        "DriverOpts": {},
        "NetworkID": "c3cdfed3c816fd00d773a834c41cd90c7ecf393ffb1a28fc287fe7f51a2000ea",
        "EndpointID": "51ca6ac4ed5283200da04ab36baeda9f1901398daced8d0d26c9be085fffad85",
        "Gateway": "10.0.0.1",
        "IPAddress": "10.0.0.2",
        "DNSNames": [
            "s1",
            "a9841a3fc826"
        ]
    },
    "bridge": {
        "IPAMConfig": null,
        "Links": null,
        "Aliases": null,
        "MacAddress": "02:42:ac:11:00:02",
        "DriverOpts": null,
        "NetworkID": "499dc11d60dd20287a1e2d405cdb8b5a4c0ea7539b06fa5b75abce34d56172e5",
        "EndpointID": "274c39cb5dbc78784ad86f6a619389966c4e2d63bf1b6a311bfb4aac6e56e126",
        "Gateway": "172.17.0.1",
        "IPAddress": "172.17.0.2",
        "DNSNames": null
    }
}

//  backend network

"Containers": {
    "65c51120358b35b396947755b67a6968528e8c454e337d102a637b46bea3528f": {
        "Name": "s2",
        "MacAddress": "02:42:0a:00:00:03",
        "IPv4Address": "10.0.0.3/24",
        "IPv6Address": ""
    },
    "a9841a3fc826fbc800de32511f44e09ae09a744dd1ad15a08e3804d6a26a6859": {
        "Name": "s1",
        "MacAddress": "02:42:0a:00:00:02",
        "IPv4Address": "10.0.0.2/24",
        "IPv6Address": ""
    }
}
```

Now, we remove `s1` and `s2` from the bridge network.


```bash
docker network disconnect bridge s1
docker network disconnect bridge s2
```

Now, both containers are on the same `backend` network, they're visible to each other by hostname.
Notice how the DNS server is a local DNS server this time and not the host's.

```bash
$ nslookup s1
Server:         127.0.0.11
Address:        127.0.0.11#53

Non-authoritative answer:
Name:   s1
Address: 10.0.0.2

$ nslookup s2
Server:         127.0.0.11
Address:        127.0.0.11#53

Non-authoritative answer:
Name:   s2
Address: 10.0.0.3
```

## Different networks

Create new network called `frontend` and add `s2` to it and remove it from backend.

```bash
docker network create frontend --subnet 10.0.1.0/24

docker network connect frontend s2  
docker network disconnect backend s2
```

Now `s2`  is not accessible from `s1`, not even by IP.


- We will create a gateway container `gate` and attach it to both `backend` and `frontend` networks.

```bash
docker run -it --name gate --network backend -d httpd
docker network connect frontend gate
```

Now `gate` can access `s1` and `s2` as `gate` is in both `frontend` and `backend` networks.

We'll add a rule in `s1` and `s2` saying to route all traffic to `10.0.0.0/24` via the gateway i.e. `10.0.1.0/24`
To update routing rules we need to start containers with `--cap-add=NET_ADMIN`


```bash
docker run --name s1 --network frontend --cap-add=NET_ADMIN -d nhttpd
docker run --name s2 --network backend --cap-add=NET_ADMIN -d nhttpd


# ================================== Now in S1 (in network frontend) =====================================
$ nslookup gate # our gateway name

Server:         127.0.0.11
Address:        127.0.0.11#53

Non-authoritative answer:
Name:   gate
Address: 10.0.0.3

# We add a rule saying route all traffic to 10.0.1.0/24 (our backend network) through 10.0.0.3 (gateway IP)
ip route add 10.0.1.0/24 via 10.0.0.3

# ================================== Now in S2 (in network backend) ==================================
$ nslookup gate # our gateway name

Server:         127.0.0.11
Address:        127.0.0.11#53

Non-authoritative answer:
Name:   gate
Address: 10.0.1.3

# We add a rule saying route all traffic to 10.0.0.0/24 (our frontend network) through 10.0.1.3 (gateway IP)
ip route add 10.0.0.0/24 via 10.0.1.3   

```

