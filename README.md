# Mini Calculadora 


### 1. Pruebas unitarias
Archivos: `calculadora.py`, `tests/test_calculadora.py`

```bash
pytest tests/test_calculadora.py -v
```
Expliquen `assert`, casos positivos y negativos, y cómo pytest detecta
automáticamente cualquier archivo `test_*.py`.

### 2. Pruebas de integración
Archivos: `app.py`, `templates/index.html`, `tests/test_integracion.py`

```bash
pytest tests/test_integracion.py -v
```
Aquí ya no probamos una función sola, sino Flask + calculadora.py juntos
(usamos `app.test_client()`, sin necesidad de levantar el servidor).

### 3. Pruebas de regresión
Archivo: `tests/test_regresion.py`

```bash
pytest tests/test_regresion.py -v
```
Cambien algo en `calculadora.py` (por ejemplo rompan
`restar`) y corran de nuevo. La prueba debe fallar de inmediato.

### 4. Depuración y análisis de código
Archivos: `depuracion_ejemplo.py`, `tests/test_depuracion.py`

```bash
pytest tests/test_depuracion.py -v
```
Este test **falla a propósito**. Pasos para depurar:
1. Ver el mensaje de fallo con `-v`.
2. Agregar `breakpoint()` dentro de `es_par()` y correr con `-s` para entrar
   en modo `pdb` (comandos útiles: `n` siguiente línea, `p numero` para ver
   el valor, `c` continuar).
3. Corregir el bug (`== 1` debería ser `== 0`).


### 5. Pruebas de seguridad
Archivo: `tests/test_seguridad.py`

```bash
pytest tests/test_seguridad.py -v
```
Cubre: protección contra división por cero, rechazo de entradas no
numéricas, límite de longitud, y protección contra XSS (Flask/Jinja2 escapa
el HTML automáticamente).

### 6. Automatización con GitHub Actions
Archivo: `.github/workflows/tests.yml`

Al hacer `git push`, GitHub instala dependencias, corre `flake8` y luego
`pytest` automáticamente. Muestren la pestaña "Actions" del repo con un
push que falla y uno que pasa.

### 7. Pruebas de carga
Archivos: `tests/test_carga.py` (calentamiento), `locustfile.py` (carga real)

```bash
python app.py          # en una terminal
locust                  # en otra terminal
```
Abran `http://localhost:8089`, simulen usuarios y observen tiempos de
respuesta contra `/` y `/calcular`.

### 8. Pruebas con Selenium
Archivo: `selenium/test_web.py`

```bash
python app.py                     # dejar corriendo
pytest selenium/test_web.py -v    # en otra terminal
```
Necesitan Chrome instalado. Selenium abre el navegador, llena el formulario,
hace clic y verifica el resultado — como lo haría una persona.

## Ejecutar todo junto (sin Selenium ni Locust)

```bash
pytest tests/
```
