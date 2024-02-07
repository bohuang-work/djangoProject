#!/bin/bash

set -e

python3 manage.py makemigrations && 
python3 manage.py migrate && 
python3 manage.py runserver 0.0.0.0:8080 &

# sleep 5

# python manage.py qcluster