#!/bin/bash

set -o errexit
set -o nounset

echo "Change location"
cd /home/api/app


echo "Start celery"
celery -A main.celery worker -l DEBUG
