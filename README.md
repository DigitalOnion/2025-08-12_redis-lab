# 2025-08-12_redis-lab

## actions:

- build docker image with:
    `docker build -t python-api:latest --debug .`

- create the 'redis-lab' kubernetes cluster in KinD with:
    `kind create cluster --config cluster/kind-cluster-config.yaml`

- Load the docker image into the new cluster
    `kind load docker-image python-api:latest --name redis-lab`

    > the image should appear in the docker.desktop images


