# start from an official image
FROM python:3.6

RUN mkdir -p /opt/services/django_app/src
WORKDIR /opt/services/django_app/src

# copy project code
COPY . /opt/services/django_app/src

# install our dependencies
RUN pip install -r requirements.txt

# Collect static files
RUN cd app && python manage.py collectstatic

# expose the port 8000
EXPOSE 8000
