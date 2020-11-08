FROM python:3.7-slim-stretch

LABEL author="Arthur Grava <arthur.grava@gmail.com>"

RUN apt update
RUN apt install gcc -y

RUN mkdir /application

COPY ./common /application/common
COPY ./flask /application/flask

WORKDIR /application/flask

CMD ["/application/flask/run.sh"]
