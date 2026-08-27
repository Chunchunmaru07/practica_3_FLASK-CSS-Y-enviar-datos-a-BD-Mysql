from flask import Flask, render_template, request

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Ruta que recibe los datos enviados por el formulario
@app.route("/saludar", methods=["POST"])
def saludar():
    # Recuperar los datos del formulario HTML
    nombre = request.form["nombre"]
    pasatiempos = request.form.getlist("pasatiempos")
    me_gusta = request.form["me_gusta"]
    
    # Enviar las variables hacia saludar.html
    return render_template(
        "saludar.html",
        nombre=nombre,
        pasatiempos=pasatiempos,
        me_gusta=me_gusta
    )

# Iniciar el servidor de desarrollo
if __name__ == "__main__":
    app.run(debug=True)