def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        # Protección: no dejamos que el programa explote con ZeroDivisionError
        return None
    return a / b


def es_numero_valido(valor):
    try:
        float(valor)
        return True
    except (TypeError, ValueError):
        return False


def validar_nota(nota):
    # Protección simple: evitamos notas demasiado largas
    if len(nota) > 50:
        return False
    return True
