REPO ?= arthurgrava
APP ?= flask-app
IMG ?= flask-bench-app


version:
	$(eval VERSION=$(shell cat ${APP}/VERSION))

build:
	docker build -t ${IMG} -f ${APP}/Dockerfile ./

tag: version
	docker tag ${IMG}:latest ${REPO}/${IMG}:${VERSION}

push: version
	docker push ${REPO}/${IMG}:${VERSION}

flask-build:
	make build APP=flask-app IMG=flask-bench-app
	make tag APP=flask-app IMG=flask-bench-app
	make push APP=flask-app IMG=flask-bench-app
