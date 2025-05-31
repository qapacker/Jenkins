from locust import HttpUser, task, between
import random

class CalculatorUser(HttpUser):
    wait_time = between(1, 2)  # Espera entre tareas

    def on_start(self):
        print("🚀 Iniciando usuario virtual")

    @task(1)
    def hello(self):
        self.client.get("/")

    @task(2)
    def add(self):
        a, b = random.randint(1, 100), random.randint(1, 100)
        self.client.get(f"/calc/add/{a}/{b}")

    @task(2)
    def substract(self):
        a, b = random.randint(1, 100), random.randint(1, 100)
        self.client.get(f"/calc/substract/{a}/{b}")

    @task(2)
    def multiply(self):
        a, b = random.randint(1, 100), random.randint(1, 100)
        self.client.get(f"/calc/multiply/{a}/{b}")

    @task(2)
    def divide(self):
        a, b = random.randint(1, 100), random.randint(1, 100) or 1  # evita división por cero
        self.client.get(f"/calc/divide/{a}/{b}")