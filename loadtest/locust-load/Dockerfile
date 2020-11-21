FROM locustio/locust:1.3.2

LABEL author="Arthur Grava <arthur.grava@gmail.com>"

RUN mkdir app

COPY app/ app/

CMD [ "locust", "-f", "app/calls.py" ]
