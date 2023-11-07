# djangoProject

A implementation fo RESTfuls API using Django REST framework

## Pre-requirements

- python >= 3.11
- pip
- docker
- ansible

#### ubuntu

```
   python3 -m pip install ansible
```

#### mac os

make sure you have brew installed on mac.

```
   brew install ansible
```

## Setup

#### using python virtual environment

1. create a python virtual environment.

```
   python3 -m venv venv
```

2. active the virtual environment.

```
   source venv/bin/activate
```

3. install all dependencies.

```
   pip3 install -r requirements.txt
```

4. run migrations then start server.

```
  ./run.sh
```

#### using docker compose

1. start server:

```
  docker compose up -d
```

2. stop server:

```
  docker compose down
```

## Deployments

1. create a folder named djangoProject for deployments:

```
ansible-playbook ansible/deployment.yaml  --extra-vars "deployment_folder=/<find the full path>/djangoProject"
```

2. start the server:

```
ansible-playbook ansible/start_server.yaml  --extra-vars "deployment_folder=/<find the full path>/djangoProject"
```

3. stop the server:

```
ansible-playbook ansible/stop_server.yaml --extra-vars "deployment_folder=/<find the full path>/djangoProject"
```

## Endpoints

- get all users / create users: http://127.0.0.1:8080/v1/users/
- get / update / delete user by id: http://127.0.0.1:8080/v1/user/{UUID}
- get user active: http://127.0.0.1:8080/v1/users/active/true
- get user not active: http://127.0.0.1:8080/v1/users/active/false
- get user less than age: http://127.0.0.1:8080/v1/users/age/lte/{age}
- get user greater than age: http://127.0.0.1:8080/v1/users/age/gte/{age}

## Swagger

![alt text](https://github.com/bohuang-work/djangoProject/blob/main/static/django_rest_api.png)
