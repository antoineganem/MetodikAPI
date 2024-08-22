from flask import Blueprint, request, jsonify
from app.services.login.login_service import login

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login_route():
    data = request.json
    print("Datos recibidos:", data)  # Esto mostrará los datos recibidos en la consola
    
    param1 = data.get('param1')
    param2 = data.get('param2')
    param3 = data.get('param3')

    print("Datos recibidos:", param1, param2, param3)  

    # Cambia la condición para verificar si alguno es None en lugar de usar all()
    if param1 is None or param2 is None or param3 is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    return login(param1, param2, param3)