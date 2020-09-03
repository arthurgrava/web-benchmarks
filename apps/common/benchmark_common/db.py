from typing import Any, Dict, List

from elasticsearch import Elasticsearch

from . import models as m


DOC_TYPE = "_doc"


class DB:
    def __init__(self):
        self.es = Elasticsearch()
        self.user_schema = m.UserSchema()

    def create_index_if_doesnt_exist(self, index: str) -> None:
        if not self.es.indices.exists(index):
            self.es.indices.create(index)

    def put_user(self, index: str, user: Dict[str, Any]) -> None:
        u = self.user_schema.load(user)
        some_operation_on_user = self.user_schema.dump(u)
        self.create_index_if_doesnt_exist(index)
        self.es.index(
            index, some_operation_on_user, doc_type=DOC_TYPE, id=u.user_id
        )

    def get_user(self, index: str, user_id: str) -> m.User:
        document = self.es.get(index, user_id, doc_type=DOC_TYPE)
        return self.user_schema.load(document["_source"])

    def search_user(self, index: str, user_name: str) -> List[m.User]:
        pass # for now
