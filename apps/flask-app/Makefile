WORKERS ?= 4

gunicorn-start:
	gunicorn -w ${WORKERS} main:app

meinheld-start:
	gunicorn -k egg:meinheld#gunicorn_worker -w ${WORKERS} main:app

uwsqi-start:
	uwsgi --http 127.0.0.1:8881 --processes ${WORKERS} --module main:app
