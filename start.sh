#!/bin/sh
set -e

echo "Activate venv"
source /opt/venv/bin/activate

echo "Running server "
python manage.py runserver 5000
