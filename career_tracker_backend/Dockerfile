FROM python:3.9

WORKDIR /app

RUN pip install gunicorn==20.1.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir 

COPY . .

RUN chmod +x run.sh

ENTRYPOINT ["/app/run.sh"]

# CMD python manage.py migrate && python manage.py collectstatic --noinput && python manage.py loaddata user.json && python manage.py loaddata students.json && manage.py loaddata token.json && cp -r /app/collected_static/. /backend_static/static/ && gunicorn --bind 0:8000 career_tracker_backend.wsgi
