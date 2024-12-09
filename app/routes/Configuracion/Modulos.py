from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Configuracion.modulos_service import verModulos, verModuloID, actModulo

verModulos_bp = Blueprint('verModulos', __name__)
verModuloID_bp = Blueprint('verModuloID', __name__)
actModulo_bp = Blueprint('actModulo', __name__)



@verModulos_bp.route('/Configuracion/verModulos', methods=['POST'])
@jwt_required()
def modulos_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verModulos(data)
    
    return user_response


@actModulo_bp.route('/Configuracion/actModulo', methods=['POST'])
@jwt_required()
def actModulo_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    user_response = actModulo(data)
    return user_response

@verModuloID_bp.route('/Configuracion/verModuloID', methods=['GET'])
@jwt_required()
def verModuloID_route():
    ID = request.args.get('ID')

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = verModuloID(ID)
    return response 



