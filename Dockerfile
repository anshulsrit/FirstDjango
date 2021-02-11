#base image
FROM python:3.8.7-alpine

RUN mkdir -p /FirstDjango
COPY . /FirstDjango
WORKDIR /FirstDjango
RUN apk update
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations \
    && python manage.py makemigrations polls \
    && python manage.py makemigrations simpleform \
    && python manage.py migrate

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

