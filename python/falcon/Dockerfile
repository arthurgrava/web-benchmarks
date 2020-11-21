FROM python:3.7-slim-stretch

LABEL author "Arthur Grava"

RUN apt update
RUN apt install gcc -y

RUN mkdir /application

COPY ./falcon /application/falcon
WORKDIR /application/falcon

COPY ./common /application/common
RUN pip install -r /application/falcon/requirements.txt

CMD ["./run.sh"]
