# djangoProject

A implementation fo RESTfuls API using Django REST framework

## Setup

### using python virtual environment

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

### using docker compose

1. start server:

```
  docker compose up -d
```

2. stop server:

```
  docker compose down
```

## Endpoints

- get all users / create users: http://127.0.0.1:8080/v1/users/
- get / update / delete user by id: http://127.0.0.1:8080/v1/user/{UUID}
- get user active: http://127.0.0.1:8080/v1/users/active/true
- get user not active: http://127.0.0.1:8080/v1/users/active/false
- get user less than age: http://127.0.0.1:8080/v1/users/age/lte/{age}
- get user greater than age: http://127.0.0.1:8080/v1/users/age/gte/{age}
