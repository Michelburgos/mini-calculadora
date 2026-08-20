from calculadora import sumar, restar, multiplicar, dividir, es_numero_valido


def test_sumar():
    assert sumar(2, 3) == 5


def test_restar():
    assert restar(5, 2) == 3


def test_multiplicar():
    assert multiplicar(4, 3) == 12


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_cero():
    # No debe explotar, debe devolver None
    assert dividir(10, 0) is None


def test_es_numero_valido_con_numero():
    assert es_numero_valido("42") is True


def test_es_numero_valido_con_texto():
    assert es_numero_valido("hola") is False
