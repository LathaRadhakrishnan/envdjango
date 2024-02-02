from locust import HttpUser, between, task

class MyUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def my_task(self):
        self.client.get("/path")
