FROM python:3.5.1

MAINTAINER "dhilipsiva" <dhilipsiva@gmail.com>

# ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN pip install django==1.9.1 numpy gunicorn networkx

ADD requirements.txt /code/
ADD extra-requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/
