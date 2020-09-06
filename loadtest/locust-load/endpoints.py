import os
import random

from locust import HttpUser, constant, task


class Config:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        filepath = os.getenv("USERS_FILE", f"{dirname}/../../user_ids.txt")
        with open(filepath, "r") as fr:
            self.users = [l.strip() for l in fr]

    def get_user(self):
        return random.choice(self.users)


cfg = Config()


class Loadtest(HttpUser):
    # wait time between tasks' execution
    wait_time = constant(1)

    @task
    def get_user(self):
        user_id = cfg.get_user()
        endpoint = f"/v1/users/{user_id}"
        self.client.get(endpoint)
