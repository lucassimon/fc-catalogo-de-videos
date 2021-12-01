#!/bin/sh
set -e

source /opt/venv/bin/activate

echo "Static files. "
python manage.py collectstatic --noinput

echo "Running server "
python manage.py runserver 5000
