REPO ?= arthurgrava
DOCKERFILE ?= flask-app/imgs/Dockerfile.gunicorn
APP ?= flask-app
IMG ?= flask-bench-app


version:
	$(eval VERSION=$(shell cat ${APP}/VERSION))

build:
	docker build -t ${IMG} -f ${DOCKERFILE} ./

tag: version
	docker tag ${IMG}:latest ${REPO}/${IMG}:${VERSION}

push: version
	docker push ${REPO}/${IMG}:${VERSION}

build-push:
	make build
	make tag
	make push

flask-build:
	make build-push APP=flask-app IMG=flask-bench-gunicorn REPO=arthurgrava DOCKERFILE=flask-app/imgs/Dockerfile.gunicorn
	make build-push APP=flask-app IMG=flask-bench-meinheld REPO=arthurgrava DOCKERFILE=flask-app/imgs/Dockerfile.meinheld
	make build-push APP=flask-app IMG=flask-bench-uwsgi REPO=arthurgrava DOCKERFILE=flask-app/imgs/Dockerfile.uwsgi
