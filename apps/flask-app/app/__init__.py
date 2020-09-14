from typing import Any, Dict

from benchmark_common import db
from flask import Flask

from . import (
    config,
    routes
)


def register_blueprints(app: Flask):
    blueprints = [
        routes.live,
        routes.api_v1,
    ]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def create_app():
    app = Flask(config.APP_NAME)
    register_blueprints(app)
    app.es = db.DB(config.ES_HOST)
    return app
