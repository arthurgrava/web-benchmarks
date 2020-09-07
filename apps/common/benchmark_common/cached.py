import json
from typing import Any, Callable, Dict

import redis


class Cacher:
    def __init__(self, host: str, port: int):
        self.conn = redis.Redis(host=host, port=port)

    def _build_key(self, prefix, *args, **kwargs):
        values = [prefix] + [str(e) for e in args] + [str(e) for e in kwargs.values()]
        return "_".join(values)

    def get(self, prefix: str, expiration: int = 300) -> Callable:
        """
        Looks for a value in the cache using `keys` to format the cache key using `key_format`
        as a simple get.
        """
        def wrapped(func: Callable) -> Callable:
            def inner_with_args(*args, **kwargs) -> Any:
                key = self._build_key(prefix, *args, **kwargs)
                res = self.conn.get(key)
                if res:
                    return json.loads(res)
                else:
                    res = func(*args, **kwargs)
                    self.conn.set(key, json.dumps(res), ex=expiration)
                    return res
            return inner_with_args
        return wrapped
