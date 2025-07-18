from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(1, 2)

    @task
    def predict(self):
        self.client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
