from http import HTTPStatus

from benchmark_common import models, utils
from elasticsearch.exceptions import NotFoundError
from flask import abort, Blueprint, current_app, jsonify, request

from .config import ES_INDEX, REDIS_HOST, REDIS_PORT
from . import control


live = Blueprint("Liveness", __name__, url_prefix="/")
api_v1 = Blueprint("V1 api", __name__, url_prefix="/v1")
schema = models.UserSchema()


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


@api_v1.route("/users/<user_id>", methods=("GET",))
def get_user(user_id):
    try:
        cache_result = bool(request.args.get("cache"))
        print(cache_result)
        if cache_result:
            user = control.get_user_chached_if_possible_cached(
                current_app.es,
                user_id,
            )
        else:
            user = control.get_user_chached_if_possible(
                current_app.es,
                user_id,
            )
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
    cache_result = bool(request.args.get("cache"))
    print(cache_result)
    if cache_result:
        results = control.search_users_cached(
            current_app.es,
            name,
            limit,
            offset,
        )
    else:
        results = control.search_users(
            current_app.es,
            name,
            limit,
            offset,
        )
    
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

@api_v1.route("/sleep/users/<user_id>")
def get_user_performing_sleep(user_id):
    return {
        "user": control.give_it_some_sleep_return_dict()
    }

@api_v1.route("/sleep/users")
def get_users_performing_sleep():
    limit = int(request.args.get("limit", 10))
    return {
        "users": control.give_it_some_sleep_return_list_of_dict(limit)
    }
