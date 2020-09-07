from typing import Any, Dict

from benchmark_common import db
from flask import Flask

from . import (
    config,
    routes
)


def create_app():
    app = Flask(config.APP_NAME)
    app.register_blueprint(routes.live)
    app.register_blueprint(routes.api_v1)
    app.es = db.DB(config.ES_HOST)
    return app
