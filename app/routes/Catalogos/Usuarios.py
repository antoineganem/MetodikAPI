from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Usuarios.usuarios_service import *


usuarios_bp = Blueprint('usuarios_bp', __name__)

@usuarios_bp.route('/Catalogos/Usuarios/verUsuarios', methods=['POST'])
@jwt_required()
def verPersonas():
    data = request.json
    print(data)
    response = verPersonas_service(data)
    return response

@usuarios_bp.route('/Catalogos/Usuarios/verUsuariosPorID', methods=['GET'])
@jwt_required()
def verPersonasPorID():
    id = request.args.get('id')
    print(id)
    if id is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    response = verPersonasPorID_service(id)
    return response

@usuarios_bp.route('/Catalogos/Usuarios/actUsuarios', methods=['POST'])
@jwt_required()
def actUsuarios():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    response = actPersonas_service(data)
    return response
