FROM python:3.7-slim-stretch

LABEL author="Arthur Grava <arthur.grava@gmail.com>"

RUN apt update
RUN apt install gcc -y

RUN mkdir -p /app

COPY . /app

RUN pip install -r /app/requirements.txt
