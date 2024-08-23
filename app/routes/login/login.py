from flask import Blueprint, request, jsonify, Response
from app.services.login.login_service import login
from flask_jwt_extended import create_access_token, jwt_required

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

    # Llama al servicio de login para validar las credenciales
    user_response = login(param1, param2, param3)
    if not user_response:
        return jsonify({"error": "Credenciales inválidas"}), 401

    # Si la respuesta del servicio login es un objeto Response, extrae los datos
    if isinstance(user_response, Response):
        user_response = user_response.get_json()

    # Genera un token JWT
    access_token = create_access_token(identity={'param1': param1})

    # Combina la respuesta del servicio `login` con el token JWT
    response = {
        "user_data": user_response,
        "access_token": access_token
    }

    return jsonify(response), 200

# Ejemplo de una ruta protegida con JWT
@login_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    return jsonify(message="Esta es una ruta protegida"), 200
