import sqlite3
import pandas as pd
import random
import base64
import os
from flask import Flask, Blueprint, jsonify, request

app = Flask(__name__)
main = Blueprint('main', __name__)

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("planes_cozy.db", check_same_thread=False)
cursor = conn.cursor()

# Ruta base para los iconos
ICON_BASE_PATH = "./data/icons"

@main.route('/api', methods=['GET'])
def home():
    return jsonify({'message': 'Hola desde Flask!'})

# Función para leer y codificar el icono en base64
def encode_icon(icon_name):
    icon_path = os.path.join(ICON_BASE_PATH, icon_name)
    try:
        with open(icon_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        return None  # Se maneja luego en la respuesta JSON

# Función para obtener un plan aleatorio según el tier
@main.route('/plan_random', methods=['GET'])
def obtener_plan_random():
    tier = request.args.get('tier', '').lower()
    if tier not in ['bronze', 'silver', 'gold']:
        return jsonify({"error": "Tier inválido. Usa 'bronze', 'silver' o 'gold'"}), 400
    
    cursor.execute("SELECT icono, titulo, tier, descripcion, materiales, indoor_outdoor FROM planes WHERE tier = ?", (tier,))
    planes = cursor.fetchall()
    
    if not planes:
        return jsonify({"error": "No hay planes disponibles para este tier"}), 404
    
    plan = random.choice(planes)
    
    # Codificar el icono en base64
    icon_base64 = encode_icon(plan[0])
    if not icon_base64:
        icon_base64 = ""

    plan_dict = {
        "icono": icon_base64,
        "titulo": plan[1],
        "tier": plan[2],
        "descripcion": plan[3],
        "materials": plan[4],
        "indoor_outdoor": plan[5]
    }
    return jsonify(plan_dict)

# Registrar el Blueprint
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)