ENV ?= test
APP ?= flask

select-env:
	kubectl config use-context ${ENV}

apply-common: select-env
	kubectl apply -f common/namespace.yml
	kubectl apply -f common/elasticsearch.yml
	kubectl apply -f common/redis.yml
	kubectl apply -f common/python.yml

destroy-common: select-env
	kubectl delete -f common/elasticsearch.yml
	kubectl delete -f common/redis.yml
	kubectl delete -f common/namespace.yml
	kubectl delete -f common/python.yml

apply-app: select-env
	kubectl apply -f ${APP}/

destroy-app: select-env
	kubectl delete -f ${APP}/
