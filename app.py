from flask import Flask, render_template, request, redirect
from calculadora import sumar, restar, multiplicar, dividir, validar_nota

app = Flask(__name__)


historial = []


@app.route("/")
def inicio():
    return render_template("index.html", historial=historial)


@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        a = float(request.form.get("a", ""))
        b = float(request.form.get("b", ""))
    except ValueError:
        return redirect("/")

    operacion = request.form.get("operacion", "sumar")
    nota = request.form.get("nota", "").strip()

    if not validar_nota(nota):
        nota = ""

    if operacion == "sumar":
        resultado = sumar(a, b)
    elif operacion == "restar":
        resultado = restar(a, b)
    elif operacion == "multiplicar":
        resultado = multiplicar(a, b)
    elif operacion == "dividir":
        resultado = dividir(a, b)
    else:
        resultado = None

    historial.append({
        "a": a,
        "b": b,
        "operacion": operacion,
        "resultado": resultado,
        "nota": nota,
    })

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
