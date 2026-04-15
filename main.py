import os
from flask import Flask, jsonify

app = Flask(__name__)

# Tu catálogo de autos (base de datos simulada)
catalogo_autos = [
    {
        "id": 1,
        "marca": "Toyota",
        "modelo": "Corolla",
        "año": 2022,
        "precio": 350000,
        "color": "Gris"
    },
    {
        "id": 2,
        "marca": "Ford",
        "modelo": "Mustang",
        "año": 2023,
        "precio": 850000,
        "color": "Rojo"
    },
    {
        "id": 3,
        "marca": "Honda",
        "modelo": "Civic",
        "año": 2021,
        "precio": 320000,
        "color": "Blanco"
    }
]

# Ruta 1: Pantalla de inicio
@app.route('/', methods=['GET'])
def inicio():
    return "Bienvenido al Microservicio del Catalogo de Autos."

# Ruta 2: El JSON que te pide tu rúbrica
@app.route('/api/autos', methods=['GET'])
def obtener_autos():
    return jsonify(catalogo_autos)

# Configuracion de arranque seguro para Replit
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
