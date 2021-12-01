#!/bin/sh
set -e

if [ -z "${POSTGRES_USER}" ]; then
    base_postgres_image_default_user='postgres'
    export POSTGRES_USER="${base_postgres_image_default_user}"
fi

postgres_ready() {
python << END
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
        port="${POSTGRES_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  echo ${POSTGRES_DB} ${POSTGRES_USER} ${POSTGRES_PASSWORD} ${POSTGRES_HOST}
  sleep 1
done
>&2 echo 'PostgreSQL is available'

source /opt/venv/bin/activate

echo "Making migrations and migrating the database. "
python manage.py migrate --noinput

for language in pt_BR es de
do
  echo "Compile translations. $language "
  python manage.py compilemessages -l $language
done

exec "$@"
