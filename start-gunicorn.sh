#!/bin/sh
set -e


echo "Running gunicorn"
python manage.py runserver 5000
