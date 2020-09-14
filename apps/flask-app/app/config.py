import os


APP_NAME = "FlaskAPP"
ES_INDEX = os.getenv("ES_INDEX", "flask-users")
ES_HOST = os.getenv("ES_HOST", "http://localhost:9200")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
