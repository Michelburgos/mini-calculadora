from calculadora import sumar, restar, multiplicar, dividir


def test_regresion_sumar():
    assert sumar(1, 1) == 2


def test_regresion_restar():
    assert restar(10, 4) == 6


def test_regresion_multiplicar():
    assert multiplicar(3, 3) == 9


def test_regresion_dividir():
    assert dividir(9, 3) == 3


# Idea para la clase: cambien algo en calculadora.py (por ejemplo,
# rompan "restar" a propósito) y vuelvan a correr "pytest".
# Estas pruebas deben fallar inmediatamente y así ven para qué sirve
# la regresión: detectar que algo que ya funcionaba se rompió.
