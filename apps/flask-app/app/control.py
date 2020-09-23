import time
import random

from benchmark_common import cached, models, utils
from flask import current_app

from .config import ES_INDEX, REDIS_HOST, REDIS_PORT


cache = cached.Cacher(REDIS_HOST, REDIS_PORT)
schema = models.UserSchema()


def _sleep():
    time_to_sleep = (random.random() * .1) + .1
    time.sleep(time_to_sleep)


@cache.get("flask_users")
def get_user_chached_if_possible_cached(es_conn, user_id):
    return get_user_chached_if_possible(es_conn, user_id)


def get_user_chached_if_possible(es_conn, user_id):
    user = es_conn.get_user(ES_INDEX, str(user_id))
    dict_user = schema.dump(user)
    return dict_user


@cache.get("flask_users_search")
def search_users_cached(es_conn, name, limit, offset):
    return search_users(es_conn, name, limit, offset)


def search_users(es_conn, name, limit, offset):
    results = es_conn.search_user(ES_INDEX, name, offset, limit)
    return [
        schema.dump(res) for res in results
    ]


def give_it_some_sleep_return_dict():
    _sleep()
    return schema.dump(utils.build_random_user())


def give_it_some_sleep_return_list_of_dict(amount: int = 10):
    _sleep()
    return [
        schema.dump(utils.build_random_user()) for _ in range(amount)
    ]
