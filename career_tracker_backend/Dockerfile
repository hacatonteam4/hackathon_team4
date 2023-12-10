FROM python:3.9

WORKDIR /backend

RUN pip install gunicorn==20.1.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir 

COPY . .

# COPY run.sh .

# RUN chmod +x run.sh

# ENTRYPOINT ["/backend/run.sh"]


# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "career_tracker_backend.wsgi"]
CMD python manage.py collectstatic --noinput && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 career_tracker_backend.wsgi:application --reload

