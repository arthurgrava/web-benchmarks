FROM python:3.7-slim-stretch

LABEL author="Arthur Grava <arthur.grava@gmail.com>"

RUN apt update
RUN apt install gcc -y

RUN mkdir /application

COPY ./common /application/common
COPY ./flask /application/flask

RUN pip install -e /application/common
RUN pip install -r /application/flask/requirements.txt

WORKDIR /application/flask

CMD ["./run.sh"]
