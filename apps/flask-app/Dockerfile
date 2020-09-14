FROM python:3.7-slim-stretch

LABEL author="Arthur Grava <arthur.grava@gmail.com>"

RUN apt update
RUN apt install gcc -y

COPY ./common ./common
COPY ./flask-app ./flask-app

RUN pip install -r ./flask-app/requirements.txt
