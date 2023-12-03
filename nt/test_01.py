from locust import HttpUser, task, TaskSet
import random as rnd



class forecast_test(HttpUser):

    @task
    def forecast_(self):
        forecast_id = rnd.randint(10, 1000)
        h = {'Host': 'weather-api111.sre-cource.example'}
        self.client.get(f"/forecast/{forecast_id}", headers=h)
