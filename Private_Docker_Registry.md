# How to set up a private Docker registry in Kubernetes

This guide is a shortened version of [Deploy Your Private Docker Registry as a Pod in Kubernetes (Medium.com)](https://medium.com/swlh/deploy-your-private-docker-registry-as-a-pod-in-kubernetes-f6a489bf0180)

**Note:** You may need to modify `docker-reg.pv.yml` and `docker-reg.pvc.yml` for your own cluster and setup.

    # Create a namespace for the local/private Docker registry deployment, then change to the new namespace:
    kubectl apply -f docker-reg-ns.yml && kubectl config set-context --current --namespace=docker-reg

    # Generate certificates to use:
    openssl req -x509 -newkey rsa:4096 -days 3650 -nodes -sha256 -keyout docker-registry.key -out docker-registry.crt -subj "/CN=docker-registry" -addext "subjectAltName = DNS:docker-registry"

    # Create those as secrets in Kubernetes:
    kubectl create secret tls docker-reg-certs --cert=docker-registry.crt --key=docker-registry.key --namespace=docker-reg

    # Create a sutable PV (modify if necessary):
    kubectl apply -f docker-reg.pv.yml

    # Bind up a PVC for the newly created PV:
    kubectl apply -f docker-reg.pvc.yml

    # Deploy the Docker Registry pod:
    kubectl apply -f docker-reg.yml

    # Deploy the Docker Registry service:
    kubectl apply -f docker-reg.svc.yml

    # Test if it works:
    kubectl run -i curl --image=curlimages/curl --restart=Never -- curl -k -v https://docker-registry:5000/v2/_catalog
