from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/saludar", methods=["POST"])
def saludar():
    nombre = request.form["nombre"]
    pasatiempos = request.form.getlist("pasatiempos")
    me_gusta = request.form["me_gusta"]

    return render_template(
        "saludar.html",
        nombre=nombre,
        pasatiempos=pasatiempos,
        me_gusta=me_gusta
    )

if __name__ == "__main__":
    app.run(debug=True)