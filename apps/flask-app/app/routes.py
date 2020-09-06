from http import HTTPStatus

from benchmark_common import cached, models, utils
from elasticsearch.exceptions import NotFoundError
from flask import abort, Blueprint, current_app, jsonify, request

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


@cache.get("flask_users_search")
def _search_users(name, limit, offset):
    results = current_app.es.search_user(ES_INDEX, name, offset, limit)
    return [
        schema.dump(res) for res in results
    ]


@api_v1.route("/users/<user_id>", methods=("GET",))
def get_user(user_id):
    try:
        user = _get_user_chached_if_possible(user_id)
        return {
            "user": user,
        }
    except NotFoundError as e:
        abort(HTTPStatus.NOT_FOUND.value, description=str(e))


@api_v1.route("/users", methods=("GET",))
def get_users():
    name = request.args.get("name", "*")
    limit = request.args.get("limit", 10)
    offset = request.args.get("offset", 0)
    results = _search_users(name, limit, offset)
    if not results:
        msg = f"No users for search with term {name}"
        abort(HTTPStatus.NOT_FOUND.value, description=msg)
    return {
        "users": results,
    }


@api_v1.route("/users", methods=("PUT",))
def put_user():
    user_data = request.json
    current_app.es.put_user(
        index=ES_INDEX,
        user=schema.dump(user_data),
    )
    return {
        "message": "created",
        "user": user_data,
    }, HTTPStatus.CREATED.value


@api_v1.route("/users/put-random-user", methods=("GET",))
def put_random_user():
    user = utils.build_random_user()
    current_app.es.put_user(
        index=ES_INDEX,
        user=schema.dump(user),
    )
    return {
        "message": "created"
    }
