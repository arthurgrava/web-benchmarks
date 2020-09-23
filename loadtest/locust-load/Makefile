CONFIG ?= "base.cfg"
FILE ?= locustfiles/cached.py
HOST ?= http://localhost:7000
USERS ?= 100
STEP_SIZE ?= 10
STEP_TIME ?= 5s
TIME ?= 3m
OUTFILE ?= execution

include .local.env

run:
	locust -f ${FILE} \
		--config ${CONFIG} \
		--host ${HOST} \
		--users ${USERS} \
		--step-load \
		--step-users ${STEP_SIZE} \
		--spawn-rate ${STEP_SIZE} \
		--step-time ${STEP_TIME} \
		--run-time ${TIME} \
		--csv ${OUTFILE} \
		GetUser SearchUser

local-run:
	make run TIME=12m USERS=100 STEP_SIZE=10 STEP_TIME=1m
