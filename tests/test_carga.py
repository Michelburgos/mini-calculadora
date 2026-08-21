from calculadora import sumar


def test_muchas_sumas_seguidas():
    resultado = 0

    for i in range(1000):
        resultado = sumar(resultado, 1)

    assert resultado == 1000

# Nota: esto NO es una prueba de carga real con usuarios HTTP concurrentes.
