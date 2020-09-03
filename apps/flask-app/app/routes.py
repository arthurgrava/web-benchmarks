from http import HTTPStatus

from benchmark_common import cached, models
from elasticsearch.exceptions import NotFoundError
from flask import abort, Blueprint, current_app, jsonify

from .config import ES_INDEX


live = Blueprint("Liveness", __name__, url_prefix="/")
api_v1 = Blueprint("V1 api", __name__, url_prefix="/v1")
schema = models.UserSchema()
cache = cached.Cacher()


@live.route("/", methods=("GET",))
@live.route("/live", methods=("GET",))
def am_i_alive():
    return {
        "message": "I'm alive!",
    }


@api_v1.errorhandler(HTTPStatus.NOT_FOUND.value)
def not_found_handler(err):
    return jsonify(message=str(err)), HTTPStatus.NOT_FOUND.value


@api_v1.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR.value)
def not_found_handler(err):
    return jsonify(message=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


@cache.get("flask_users")
def _get_user_chached_if_possible(user_id):
    user = current_app.es.get_user(ES_INDEX, str(user_id))
    dict_user = schema.dump(user)
    return dict_user


@api_v1.route("/user/<user_id>", methods=("GET",))
def get_user(user_id):
    try:
        return _get_user_chached_if_possible(user_id)
    except NotFoundError as e:
        abort(HTTPStatus.NOT_FOUND.value, description=str(e))
