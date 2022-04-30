#!/bin/zsh
set -e


echo "Running runserver"
python manage.py runserver 0.0.0.0:5000
