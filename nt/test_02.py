from locust import HttpUser, task, TaskSet
import random as rnd



class forecast_test(HttpUser):

    @task(1)
    def forecast_(self):
        h = {'Host': 'weather-api111.sre-cource.example'}
        self.client.get("/forecast/", headers=h)
