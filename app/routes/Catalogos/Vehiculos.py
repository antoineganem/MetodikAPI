from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Vehiculos.vehiculos_service import verVehiculos, actVehiculo, verVehiculoID

verVehiculos_bp = Blueprint('verVehiculos',__name__)
actVehiculo_bp = Blueprint('actVehiculo',__name__)
verVehiculoID_bp = Blueprint('verVehiculoID',__name__)


@verVehiculos_bp.route('/Catalogos/verVehiculos', methods=['POST'])
@jwt_required()
def verVehiculos_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = verVehiculos(data)

    return user_response

@actVehiculo_bp.route('/Catalogos/actVehiculo', methods=['POST'])
@jwt_required()
def actVehiculo_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = actVehiculo(data)

    return user_response

@verVehiculoID_bp.route('/Catalogos/verVehiculoID', methods=['GET'])
@jwt_required()
def verVehiculoID_route():
    ID = request.args.get('ID')
    
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verVehiculoID(ID)
    return response

