from flask import Flask, render_template, request
import pymysql
import os

app = Flask(__name__)

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "Chunchunmaru_07"
DB_NAME = "practicas_web"

def conectar_bd():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)

@app.route("/")
def inicio():

    return render_template("index.html")

@app.route("/saludar", methods=["POST"])
def f_saludar():

    nombre = request.form["nombre"]
    pasatiempos = request.form.getlist("pasatiempos")
    me_gusta = request.form["me_gusta"]
    pasatiempos_texto = ", ".join(pasatiempos)
    
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO alumnos (nombre, pasatiempos, me_gusta)
        VALUES (%s, %s, %s)
    """, (nombre, pasatiempos_texto, me_gusta))
    conexion.commit()
    conexion.close()
    
    return render_template("saludar.html", nombre=nombre, pasatiempos=pasatiempos, me_gusta=me_gusta)

@app.route("/alumnos")
def listar_alumnos():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alumnos ORDER BY id")
    alumnos = cursor.fetchall()
    conexion.close()

    return render_template("listar_alumnos.html", alumnos=alumnos)

if __name__ == "__main__":
    app.run(debug=True)