# k8s-n00b

A project to learn Kubernetes. Consists of two main parts:

### webapp

A simple Flask webpage using redis to track hostname, first and last visit, and number of visits. The idea is to run one Redis-server and multiple webapps in the Kubernetes cluster.
This part also contains a `Dockerfile` and `docker-compose.yml` to create the container and verify it using Docker.

The Docker images built are hosted on my public repo at Docker Hub: https://hub.docker.com/r/sitronno/redishello

##### Notes

- I use the `bullseye` and `buster` version of python3-slim and redis Docker images, since my Kubernetes lab consists of Raspberry Pi's, running Raspbian 10.
- To build and upload multi-arch images to Docker Hub, use [buildx](https://github.com/docker/buildx): `docker buildx build --push --platform linux/arm/v7,linux/amd64 --tag sitronno/redishello:v1.0 .`

### k8s

All files related to run the webapp and Redis on my Kubernetes cluster. At the moment, this is my work in progress.

#### How to deploy in a Kubernetes cluster

1. Set up a NFS share and edit `redis-pv.yml` accordingly
1. Create a persistent volume:

        kubectl apply -f redis-pv.yml

1. Create a persistent volume claim:

        kubectl apply -f redis-pvc.yml

1. Deploy a redis server:

        kubectl apply -f redis.deployment.yml 

1. Create a service for the redis server, so helloredis can access it:

        kubectl apply -f redis.svc.yml

1. Deploy helloredis:

        kubectl apply -f helloredis.deployment.yml

1. Try accessing the helloredis webpage by using on of the following:

        kubectl port-forward <PODNAME> 5000:5000
        # curl http://localhost:5000/
        
        kubectl expose deployment helloredis --port 5000 --type NodePort
        # NODE_PORT => kubectl get svc helloredis --output=jsonpath='{range .spec.ports[0]}{.nodePort}'
        curl http://<NODEIP>:<NODEPORT>/

        # Will only work when a loadbalancer is available (k3s, cloud env, etc..)
        kubectl expose deployment helloredis --type=LoadBalancer --name=helloredis-web

    
## Progress

- [x] Create a webapp using Redis
- [x] Create Docker images for amd64 and armv7 and upload to Docker Hub
- [x] Create Kubernetes Pod files for webapp and Redis and deploy to Cluster
- [x] Create Kubernetes Service file for Redis and verify
- [x] Create Kubernetes Deployment for all above
- [x] Update `redishello` to print name of Redis-server and preform rolling update
- [x] Create persistent storge (NFS) for Kubernetes Cluster
- [x] Create PersistentVolumeClaim for Redis to use PV
- [x] Verifiy PVC and PV actually works :-)
- [x] Set up using ["Kubernetes the hard way"](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- [x] Set up a private Docker registry
- [ ] Expose webapp and private Docker registry via ingress/træfik/NGINX-IC
- [ ] Create a dev-user with access only to webapp and redis
- [ ] Send logs to Splunk
- [ ] Metrics to Prometheus
- [ ] Set up Gitlab and a registry
- [ ] Try different databases (k8ssandra, CockroachDB)
- [ ] Try MinIO for bucket storage
