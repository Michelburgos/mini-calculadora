from app import app, historial


def test_flujo_completo_sumar():
    cliente = app.test_client()
    historial.clear()

    respuesta = cliente.post("/calcular", data={
        "a": "2",
        "b": "3",
        "operacion": "sumar",
        "nota": "prueba"
    })

    # /calcular redirige a "/"
    assert respuesta.status_code == 302
    assert len(historial) == 1
    assert historial[0]["resultado"] == 5.0

    pagina = cliente.get("/")
    assert b"5.0" in pagina.data


def test_flujo_completo_dividir_por_cero():
    cliente = app.test_client()
    historial.clear()

    cliente.post("/calcular", data={
        "a": "8",
        "b": "0",
        "operacion": "dividir",
        "nota": ""
    })

    pagina = cliente.get("/")
    assert b"Error (divisi" in pagina.data
