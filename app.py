from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def obtener_clientes():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, plan FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

@app.route("/", methods=["GET"])
def listar_clientes():
    buscar = request.args.get("buscar", "")

    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()

    if buscar:
        cursor.execute(
            "SELECT nombre, plan FROM clientes WHERE nombre LIKE ?",
            (f"%{buscar}%",)
        )
    else:
        cursor.execute("SELECT nombre, plan FROM clientes")

    clientes = cursor.fetchall()
    conn.close()

    return render_template("clientes.html", clientes=clientes, buscar=buscar)


# 👉 NUEVA RUTA PARA AGREGAR CLIENTES
@app.route("/agregar", methods=["GET", "POST"])
def agregar_cliente():
    if request.method == "POST":
        nombre = request.form["nombre"]
        plan = request.form["plan"]

        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nombre, plan) VALUES (?, ?)",
            (nombre, plan)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("listar_clientes"))

    return render_template("agregar.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
