# k8s-n00b

A project to learn Kubernetes. Consists of two main parts:

#### webapp

A simple Flask webpage using redis to track hostname, first and last visit, and number of visits. The idea is to run one Redis-server and multiple webapps in the Kubernetes cluster.
This part also contains a `Dockerfile` and `docker-compose.yml` to create the container and verify it using Docker.

The Docker images built are hosted on my public repo at Docker Hub: https://hub.docker.com/repository/docker/sitronno/k8s-n00b

**Note:** I use the `bullseye` and `buster` version of python3-slim and redis Docker images, since my Kubernetes lab consists of Raspberry Pi's, running Raspbian 10.

#### k8s

All files related to run the webapp and Redis on my Kubernetes cluster. At the moment, this is my work in progress.


## Progress

- [x] Create a webapp using Redis
- [ ] Create Docker images for amd64 and armv7 and upload to Docker Hub
- [ ] Create Kubernetes Pod files for webapp and Redis and deploy to Cluster
- [ ] Create Kubernetes Service file for Redis and verify
- [ ] Create Kubernetes Deployment for all above
- [ ] Create persistent storge (NFS) for Kubernetes Cluster
- [ ] Create PersistentVolumeClaim for Redis to use PV
- [ ] Verifiy PVC and PV actually works :-)
- [ ] Create a dev-user with access only to webapp and redis
