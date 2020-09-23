import random

from locust import HttpUser, between, task


class GetUser(HttpUser):
    # wait time between tasks' execution
    wait_time = between(0.1, .5)

    @task
    def get_user(self):
        user_id = 1
        endpoint = f"/v1/sleep/users/{user_id}"
        self.client.get(endpoint, name="get_user_by_id")


class SearchUser(HttpUser):
    wait_time = between(0.1, .5)

    @task
    def search_user(self):
        limit = random.randint(10, 30)
        endpoint = f"/v1/sleep/users?limit={limit}"
        self.client.get(endpoint, name="get_n_users")
