#!/bin/bash

# This works with k3s.
kubectl expose deployment helloredis --type=LoadBalancer --name=helloredis-web

# TODO
# Expose it properly with ingress, træfik, etc..
