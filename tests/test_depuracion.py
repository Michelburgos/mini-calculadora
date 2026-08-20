from depuracion_ejemplo import es_par


def test_es_par_con_numero_par():
    assert es_par(4) is True


def test_es_par_con_numero_impar():
    assert es_par(7) is False


# Este archivo falla a propósito la primera vez que se ejecuta.
# Es el punto de partida perfecto para enseñar depuración:
#
# 1) Correr "pytest tests/test_depuracion.py -v" y ver cuál falla.
# 2) Abrir depuracion_ejemplo.py y agregar un print(numero) dentro de es_par.
# 3) O mejor: agregar la palabra "breakpoint()" dentro de es_par y correr
#    "pytest tests/test_depuracion.py -s" para entrar en modo pdb.
# 4) Dentro de pdb, escribir "numero", luego "n" para avanzar línea a línea.
# 5) Corregir el "== 1" por "== 0" y volver a correr las pruebas.
