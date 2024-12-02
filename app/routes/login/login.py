from flask import Blueprint, request, jsonify, Response
from app.services.login.login_service import login
from flask_jwt_extended import create_access_token, jwt_required

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login_route():
    data = request.json
    print("Datos recibidos:", data) 

    Correo = data.get('Correo')
    Contrasena = data.get('Contrasena')
    Empresa = data.get('Empresa')

    print("Datos recibidos:", Correo, Contrasena, Empresa)  

    if Correo is None or Contrasena is None or Empresa is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
      
    user_response = login(Correo, Contrasena, Empresa)   
    
     
    if not user_response:
        return jsonify({"error": "Credenciales inválidas"}), 401

    if isinstance(user_response, Response):
        user_response = user_response.get_json()

    if isinstance(user_response, list) and len(user_response) > 0:
        user_data = user_response[0]
    else:
        return jsonify({"error": "Respuesta inválida del servicio de login"}), 500
    if user_data.get('Ok') == 0:
        access_token = create_access_token(identity={'Correo': Correo})
        response = {
            "user_data": user_data,
            "access_token": access_token
        }
        return jsonify(response), 200
    else:
        return jsonify(user_data), 400

@login_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    return jsonify(message="Esta es una ruta protegida"), 200
