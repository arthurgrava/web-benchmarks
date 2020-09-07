ENV ?= test

select-env:
	kubectl config use-context ${ENV}

apply-common: select-env
	kubectl apply -f ${ENV}/namespace.yml
	kubectl apply -f ${ENV}/elasticsearch.yml
	kubectl apply -f ${ENV}/redis.yml

destry-common: select-env
	kubectl delete -f ${ENV}/elasticsearch.yml
	kubectl delete -f ${ENV}/redis.yml
	kubectl delete -f ${ENV}/namespace.yml
