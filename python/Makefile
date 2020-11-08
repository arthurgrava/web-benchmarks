APP ?= flask
IMAGE ?= web-benchmarks
REPO ?= arthurgrava


version:
	$(eval VERSION=$(shell cat ${APP}/VERSION))

echo: version
	@echo ${APP}
	@echo ${IMAGE}
	@echo ${REPO}
	@echo ${VERSION}
	@echo ${REPO}/${IMAGE}:${APP}-${VERSION}

build: version
	docker build -t ${IMAGE}:${APP}-${VERSION} -f ${APP}/Dockerfile ./

push: version
	docker tag ${IMAGE}:${APP}-${VERSION} ${REPO}/${IMAGE}:${APP}-${VERSION}
	docker push ${REPO}/${IMAGE}:${APP}-${VERSION}

start:
	make -C ${APP} start

flask-build:
	make build APP=flask
	make push APP=flask

