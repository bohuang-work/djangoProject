# djangoProject

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Ansible](https://img.shields.io/badge/ansible-%231A1918.svg?style=for-the-badge&logo=ansible&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white)

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
ansible-playbook ansible/setup.yaml  --extra-vars "deployment_folder=/<find the full path>/djangoProject"
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

- get all users / create users: http://0.0.0.0:8080/v1/users/
- get / update / delete user by id: http://0.0.0.0:8080/v1/user/{UUID}
- get user active: http://0.0.0.0:8080/v1/users/active/true
- get user not active: http://0.0.0.0:8080/v1/users/active/false
- get user less than age: http://0.0.0.0:8080/v1/users/age/lte/{age}
- get user greater than age: http://0.0.0.0:8080//v1/users/age/gte/{age}

## Swagger

- visite swagger: http://0.0.0.0:8080/docs

![alt text](https://github.com/bohuang-work/djangoProject/blob/main/static/swagger.png)
