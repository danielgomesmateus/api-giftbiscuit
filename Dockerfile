FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/www/html
WORKDIR /var/www/html

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
python3-dev

RUN pip install --upgrade pip

COPY requeriments.txt /var/www/html/

RUN pip install -r /var/www/html/requeriments.txt

ADD . /var/www/html/