from common.config import Config

from locust import HttpUser, between, task


cfg = Config()


class GetUser(HttpUser):
    # wait time between tasks' execution
    wait_time = between(0.1, .5)

    @task
    def get_user(self):
        user_id = cfg.get_user()
        endpoint = f"/v1/users/{user_id}"
        self.client.get(endpoint, name="get_user_by_id")


class SearchUser(HttpUser):
    wait_time = between(0.1, .5)

    @task
    def search_user(self):
        name = cfg.get_name()
        endpoint = f"/v1/users?name={name}"
        self.client.get(endpoint, name="search_user_by_name")
