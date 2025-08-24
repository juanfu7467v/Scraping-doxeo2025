from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from scraper import login_knowlers, search_by_dni, search_by_name

app = Flask(__name__)
CORS(app)

# Interfaz web simple para probar
@app.route("/")
def home():
    return render_template("index.html")

# Endpoint: login
@app.route("/api/scraper/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    result = login_knowlers(username, password)
    return jsonify(result)

# Endpoint: búsqueda por DNI
@app.route("/api/scraper/dni/<dni>", methods=["GET"])
def buscar_dni(dni):
    result = search_by_dni(dni)
    return jsonify(result)

# Endpoint: búsqueda por nombre
@app.route("/api/scraper/nombre", methods=["POST"])
def buscar_nombre():
    data = request.get_json()
    nombres = data.get("nombres")
    apellidos = data.get("apellidos")
    result = search_by_name(nombres, apellidos)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
