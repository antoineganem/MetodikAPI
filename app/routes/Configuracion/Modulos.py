from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Configuracion.modulos_service import verModulos, verModuloID, eliminarModulo, actModulo

verModulos_bp = Blueprint('verModulos', __name__)
verModuloID_bp = Blueprint('verModuloID', __name__)
eliminarModulo_bp = Blueprint('eliminarModulo', __name__)
actModulo_bp = Blueprint('actModulo', __name__)





@verModulos_bp.route('/Configuracion/modulos', methods=['GET'])
@jwt_required()
def modulos_route():
    response = verModulos()
    return response


@actModulo_bp.route('/Configuracion/actModulo', methods=['POST'])
@jwt_required()
def actModulo_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = actModulo(data)
    return response

@verModuloID_bp.route('/Configuracion/verModuloID', methods=['GET'])
@jwt_required()
def verModuloID_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verModuloID(ID)
    return response

@eliminarModulo_bp.route('/Configuracion/eliminarModuloID', methods=['DELETE'])
@jwt_required()
def eliminarModulo_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = eliminarModulo(ID)
    return response

