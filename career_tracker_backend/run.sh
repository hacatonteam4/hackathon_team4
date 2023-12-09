#!/bin/sh
python manage.py migrate;
python manage.py collectstatic --noinput;
python manage.py loaddata user.json;
python manage.py loaddata specialties.json;
python manage.py loaddata students.json;
cp -r /app/collected_static/. /backend_static/static/
gunicorn --bind 0:8000 career_tracker_backend.wsgi;