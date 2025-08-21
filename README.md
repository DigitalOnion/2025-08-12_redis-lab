# 2025-08-12_redis-lab

## actions:

We start by building the docker image, 
then creating the 'redis-lab' kubernetes cluster in KinD,
and finally Loading the docker image into the cluster by:

- at the command line:
    
    ```
    docker build -t python-api:latest --debug .
    kind create cluster --config cluster/kind-cluster-config.yaml
    kind load docker-image python-api:latest --name redis-lab
    ```

> the image should appear in the docker.desktop images

- create the deployment - and pods -, and the service

    ```
    kubectl --apply -f k8s/deployment.yaml
    kubectl --apply -f k8s/service.yaml
    ```

    we are not using ingress just yet.


- verify everything is running with:

    ```
    kubectl get deploy
    kubectl get pod
    kubectl get svc
    ```

- since this is a NodePort service, we need to open the cluster to the outside (internet) by means of port-forwarding:

    ```
    kubectl port-forward svc/python-api-service 30080:80
    ```
    
- we can see it working by:

    ```
    $ curl http://localhost:30080
    {"message":"FastAPI is working - request URL:$http://localhost:30080/"}
    ```
    
- check the pod's logs:

    ```
    $ kubectl logs pod/python-api-5fb45d75d5-m22l8 
    INFO:     Started server process [1]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
    ```


