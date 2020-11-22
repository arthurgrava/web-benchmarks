FROM locustio/locust:1.3.2

LABEL author="Arthur Grava <arthur.grava@gmail.com>"

RUN mkdir app

COPY app/ app/
COPY requirements/base.txt app/requirements.txt
COPY run.py app/run.py

RUN pip install -r app/requirements.txt

CMD [ "locust", "-f", "app/calls.py" ]
