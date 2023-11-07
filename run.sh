#!/bin/bash

set -e

exec python3 manage.py makemigrations &
exec python3 manage.py migrate &
exec python3 manage.py runserver 0.0.0.0:8080