FROM python:3.9

WORKDIR /code

COPY ../requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

# celery -A test worker -l INFO  --concurrency 1 -n app2
CMD ["celery", "--app", "test",  "worker", "-l", "INFO",  "--concurrency", "1"]