def es_par(numero):
    """
    Esta función tiene un error a propósito.
    El objetivo es que el estudiante lo encuentre usando:
      - pytest -v
      - print() para inspeccionar valores
      - breakpoint() / pdb para pausar la ejecución
      - flake8 para revisar el estilo del código
    """
    if numero % 2 == 0:
        return True
    else:
        return False
