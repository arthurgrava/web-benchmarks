from dataclasses import dataclass

from marshmallow import Schema, fields, post_load


@dataclass
class User:
    user_id: str
    name: str
    age: int


class UserSchema(Schema):
    user_id = fields.String()
    name = fields.String()
    age = fields.Int()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
