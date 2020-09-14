ENV ?= test

select-env:
	kubectl config use-context ${ENV}

apply-common: select-env
	kubectl apply -f common/namespace.yml
	kubectl apply -f common/elasticsearch.yml
	kubectl apply -f common/redis.yml

destroy-common: select-env
	kubectl delete -f common/elasticsearch.yml
	kubectl delete -f common/redis.yml
	kubectl delete -f common/namespace.yml
