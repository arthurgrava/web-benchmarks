HOST ?= http://localhost:7000
USERS ?= 100
SPAWN_RATE ?= 0.05
RUN_TIME ?= 30m
CLASSES ?= "DBCall CalculationCall CompleteCall"

# My personal repo
REPO ?= arthurgrava

run:
	locust -f app/calls.py--config app/base.cfg \
		--host ${HOST} \
		--users ${USERS} \
		--spawn-rate ${SPAWN_RATE} \
		--run-time ${RUN_TIME} \
		${CLASSES}

version:
	$(eval VERSION=$(shell cat VERSION))

build: version
	docker build -t web-benchmarks:locust-${VERSION} -f Dockerfile .

push: build version
	docker tag web-benchmarks:locust-${VERSION} ${REPO}/web-benchmarks:locust-${VERSION}
	docker push ${REPO}/web-benchmarks:locust-${VERSION}
