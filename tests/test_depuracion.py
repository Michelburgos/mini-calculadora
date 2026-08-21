from depuracion_ejemplo import es_par


def test_es_par_con_numero_par():
    assert es_par(4) is True


def test_es_par_con_numero_impar():
    assert es_par(7) is False
