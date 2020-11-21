#!/bin/bash

#####
## An example on how to run a locust test command can be found here.
#####

HELP="./sample.sh {config-path} {host} {users} {spawn-rate} {run-time} {file} [{classes}]"

CONFIG=$1
if [[ -z "${CONFIG}" ]]; then
    echo "${HELP}"
    exit 1
fi

HOST=$2
if [[ -z "${HOST}" ]]; then
    echo "${HELP}"
    exit 1
fi

USERS=$3
if [[ -z "${USERS}" ]]; then
    echo "${HELP}"
    exit 1
fi

SPAWN_RATE=$4
if [[ -z "${SPAWN_RATE}" ]]; then
    echo "${HELP}"
    exit 1
fi

RUN_TIME=$5
if [[ -z "${RUN_TIME}" ]]; then
    echo "${HELP}"
    exit 1
fi

FILE=$6
if [[ -z "${FILE}" ]]; then
    echo "${HELP}"
    exit 1
fi

CLASSES=$7
if [[ -z "${CLASSES}" ]]; then
    CLASSES="DBCall CalculationCall CompleteCall"
    echo "Using default value of ${CLASSES} for classes"
fi

locust -f ${FILE} --config ${CONFIG} \
    --host ${HOST} \
    --users ${USERS} \
    --spawn-rate ${SPAWN_RATE} \
    --run-time ${RUN_TIME} \
    ${CLASSES}
