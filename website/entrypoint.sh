#!/usr/bin/env bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations --settings=website.settings.dev
python manage.py migrate --settings=website.settings.dev
python manage.py collectstatic --noinput --clear --settings=website.settings.dev

exec "$@"