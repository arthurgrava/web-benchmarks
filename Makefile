clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "dist" -type d | xargs rm -rf
	@find . -name "htmlcov" | xargs rm -rf
	@find . -name ".coverage" | xargs rm -rf
	@find . -name ".pytest_cache" | xargs rm -rf
	@find . -name ".cache" | xargs rm -rf
	@find . -name "*.log" | xargs rm -rf
	@find . -name "*.egg-info" | xargs rm -rf
	@find . -name "build" | xargs rm -rf

create-redis:
	docker run --name benchmark-redis -p 6379:6379 -d redis:6.0.7

start-redis:
	docker start benchmark-redis

stop-redis:
	docker stop benchmark-redis

create-elastic:
	docker run --name benchmark-elasticsearch \
		-p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -d \
		docker.elastic.co/elasticsearch/elasticsearch:7.9.1

start-elastic:
	docker start benchmark-elasticsearch

stop-elastic:
	docker stop benchmark-elasticsearch

start-flask-app:
	python apps/flask-app/main.py
