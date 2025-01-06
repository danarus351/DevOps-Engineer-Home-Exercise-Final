# DevOps-Engineer-Home-Exercise-Final
## step1-scipt.py
 * filter all human and alive charcters on earth and export to csv 

## step2 - Dockerized application
to run the api container you'll need to run the following commands in the terminal:
## accessing the api
    curl http://<host machine ip/ hostname>:5000
## Api endpoints:
    /            - get filtered human charachters from Earth
    /healthcheck -  to check server is responsive
### Build the container
    cd ./step2-Dockrized-api
    docker build -t rickandmorty_api . 
### Run the container 
    docker run -d -p 5000:5000 --name rickandmorty_api  rickandmorty_api 
### stop the container 
    docker kill rickandmorty_api
    docker rm rickandmorty_api
## step3 -  K8S deployment 
### deploy ingress controller 
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
### run the following on you k8s cluster
    cd step3-k8s
    kubectl apply -f .
### get ingress external ip and add it to hosts file 
    kubectl get ingress -n rickandmorty
### add this line to hosts file 
    < ingress adress > rickandmorty.com
now you are able to access the api:
     curl http://rickandmorty.com
     
## in k8s you are accessing the api through port 80
