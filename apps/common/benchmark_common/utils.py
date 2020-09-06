import random
import string
import uuid

from . import models as m


def build_random_user() -> m.User:
    """
    Returns a randomly generated user
    """
    name = ''.join([random.choice(string.ascii_letters) for _ in range(0, 10)])
    return m.User(
        user_id=str(uuid.uuid4()),
        name=name,
        age=random.randint(18, 99),
    )
