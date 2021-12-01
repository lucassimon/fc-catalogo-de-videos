#!/bin/sh
set -e

source /opt/venv/bin/activate

echo "Running server "
python manage.py runserver 5000
