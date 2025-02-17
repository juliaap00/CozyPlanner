#!/bin/bash

# Nombre del proyecto
PROJECT_NAME="VueTest"

# Crear el backend con Flask
echo "🛠️ Creando backend con Flask..."
mkdir backend && cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install flask flask-cors

# Crear estructura básica del backend
mkdir app && cd app
cat <<EOL > __init__.py
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    from .routes import main
    app.register_blueprint(main)
    return app
EOL

cat <<EOL > routes.py
from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/api', methods=['GET'])
def home():
    return jsonify({'message': 'Hola desde Flask!'})
EOL

cd ..
cat <<EOL > run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
EOL

deactivate
cd ..

# Crear el frontend con Vue
echo "🚀 Creando frontend con Vue.js + Vite..."
mkdir frontend && cd frontend
npx create-vite@latest . --template vue
npm install
cd ..

echo "✅ Proyecto inicializado exitosamente"
echo "🔹 Para correr el backend: cd backend && source venv/bin/activate && python run.py"
echo "🔹 Para correr el frontend: cd frontend && npm run dev"
