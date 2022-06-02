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
- [ ] Set up using ["Kubernetes the hard way"](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- [ ] Create a dev-user with access only to webapp and redis
- [ ] Expose it via ingress/træfik
- [ ] Send logs to Splunk
- [ ] Metrics to Prometheus

