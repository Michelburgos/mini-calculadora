def es_par(numero):
    """
    Esta función tiene un error a propósito.
    El objetivo es que el estudiante lo encuentre usando:
      - pytest -s
      - breakpoint() / pdb para pausar la ejecución
    """
    if numero % 2 == 0:
        return True
    else:
        return False