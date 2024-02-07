#!/bin/bash

set -e

PID=$(lsof -ti:8080)

# Check if PID is not empty
if [ -n "$PID" ]; then
    # Kill the process
    kill $PID
    echo "Process with PID $PID killed."
else
    echo "No process found using port 8080."
fi


python3 manage.py makemigrations && 
python3 manage.py migrate && 
python3 manage.py runserver 0.0.0.0:8080 &

# sleep 5

# python manage.py qcluster