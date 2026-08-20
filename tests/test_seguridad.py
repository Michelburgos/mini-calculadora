from calculadora import dividir, es_numero_valido, validar_nota
from app import app, historial


def test_division_por_cero_no_rompe_el_programa():
    resultado = dividir(5, 0)
    assert resultado is None


def test_rechaza_texto_como_numero():
    assert es_numero_valido("'; DROP TABLE usuarios; --") is False


def test_rechaza_nota_demasiado_larga():
    nota_larga = "A" * 51
    assert validar_nota(nota_larga) is False


def test_nota_con_html_no_se_ejecuta():
    # Probamos que Flask/Jinja2 escapa el HTML automáticamente (protección XSS)
    cliente = app.test_client()
    historial.clear()

    cliente.post("/calcular", data={
        "a": "1",
        "b": "1",
        "operacion": "sumar",
        "nota": "<script>alert('hackeado')</script>"
    })

    pagina = cliente.get("/")

    # El script NO debe aparecer "vivo", debe verse escapado como texto
    assert b"<script>alert" not in pagina.data
