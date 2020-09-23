WORKERS ?= 4

gunicorn-start:
	gunicorn -w ${WORKERS} -b 0.0.0.0:8883 main:app

meinheld-start:
	gunicorn -k egg:meinheld#gunicorn_worker -b 0.0.0.0:8882 -w ${WORKERS} main:app

uwsqi-start:
	uwsgi --http 0.0.0.0:8881 --processes ${WORKERS} --module main:app
