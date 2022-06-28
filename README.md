# Python Container Environment for local development

## Summary
Running environments on different workstations, different codebases and then deploying to different environments can be a hassle. 

This repo helps me use docker for local development to production

## Prerequisites
* Docker Desktop (or any docker deployment where you can build and run)
* Text editor (vim, vscode, pycharm, etc)

## My Dockerfile

The Dockerfile in the root folder of this repo is run in 3 stages:
* base
* development
* production

The base layer is for basic environment setup that can be used in both development and production layers.

The development layer will be larger than the production layer as we will have more utilities to do our job.

The production layer should be as lean as possible and only hold the runtime of the application you are building for.

## Building my development environment

Run the following command to build your development stage environment from the container.

```
docker build -t my-python-environment:development --target development .
```

This will build a docker image for you to use locally.

Once the container has been built successfully, run the following command to work inside the container.

```
docker run -it \
  -v ~/python-container-environment/:/home/developer/ \ 
  -p 5000:5000 \
  --name my-dev-env \
  my-python-environment:development \
  bash
  
```

* This command would start up the docker image and run it in interactive mode (fancy way of saying allocate a pseudo-tty and keep STDIN open). 
* It would then mount a folder from the host machine (your laptop). In this case I clone the git repo to my home directory on the mac and mounted it into the /home/developer directory. 
* It then opens port 5000
* It names the container for ease of use
* and runs bash

At this point, you should be in the container and able to run python scripts from your project folder in /home/developer/

### Want to be more lazy, docker-compose

Run the following command:

```
docker-compose up
```

This will do everything the previous docker command accomplished and enable you to setup more flexbility, like run two or more container services.

# Building my production environment

Similar to running a development environment, we would run a production build with the production target stage

```
docker build --no-cache -t my-production-python-environment:production --target production .
```

Now, it is not going to be this easy for the production environment. When you work for the man (or woman), there are certain security measures or protocols that need to be followed. Hopefully it will be and easier process to port using this method.

## Bonus content - Your own jupyter environment

Create or extend your docker-compose.yml to be able to run a jypyter lab instance.

After you have built the my-python-environment:development image, add or create a yml file with the following content.

``` docker-compose.yml
version: "3.8"

services:
  development:
    image: my-python-environment:development
    command: jupyter-lab --allow-root --no-browser --ip=0.0.0.0
    ports:
      - "0.0.0.0:8888:8888"
    stdin_open: true
    tty: true
    volumes:
      - ~/my-python-environment/:/home/developer/
```

Now run, ```docker-compose up```


Hope you found this repo useful.
