from locust import HttpUser, task, between


class Usuario(HttpUser):

    wait_time = between(1, 2)

    @task(3)
    def visitar_inicio(self):
        self.client.get("/")

    @task(1)
    def calcular_algo(self):
        self.client.post("/calcular", data={
            "a": "2",
            "b": "2",
            "operacion": "sumar",
            "nota": "carga"
        })

# Para correrlo:
#   1) python app.py   (en una terminal)
#   2) locust           (en otra terminal)
#   3) abrir http://localhost:8089 y simular usuarios
