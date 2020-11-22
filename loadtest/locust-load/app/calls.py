from locust import constant, task
from locust.contrib.fasthttp import FastHttpUser


class Base(FastHttpUser):
    wait_time = constant(0)

    def make_a_call_to(self, url, call_name):
        self.client.get(url, name=call_name)

class DBCall(Base):

    @task
    def db_call(self):
        self.make_a_call_to("/api/db-call", "db-call")

class CalculationCall(Base):

    @task
    def db_call(self):
        self.make_a_call_to("/api/calculation", "calculation")

class CompleteCall(Base):

    @task
    def db_call(self):
        self.make_a_call_to("/api/complete", "complete")


class LiveCall(Base):

    @task
    def db_call(self):
        self.make_a_call_to("/api/live", "live")
