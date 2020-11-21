#!/bin/bash

if [[ -z "${PORT}" ]]; then
    echo "Missing PORT environment variable"
    exit 1
fi

if [[ -z "${WORKERS}" ]]; then
    echo "Default workers chosen: 4"
    WORKERS=4
fi

echo "Starting with ${FRAMEWORK}"
if [[ ${FRAMEWORK} == "uwsgi" ]]; then
    uwsgi --http 0.0.0.0:${PORT} --processes ${WORKERS} --module app:app
elif [[ ${FRAMEWORK} == "meinheld" ]]; then
    gunicorn -b 0.0.0.0:${PORT} -w ${WORKERS} -k egg:meinheld#gunicorn_worker app:app
else
    gunicorn -b 0.0.0.0:${PORT} -w ${WORKERS} app:app
fi
