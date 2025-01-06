# DevOps-Engineer-Home-Exercise-Final
## step1-scipt.py
 * filter all human and alive charcters on earth and export to csv 

## step2 - Dockerized application
to run the api container you'll need to run the following commands in the terminal:
## accessing the api
'''
    curl http://<host machine ip/ hostname>:5000
'''
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
