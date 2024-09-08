from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Vehiculos.vehiculos_service import (
        VerVehiculos, VerVehiculoResumen, ActVehiculo, VerVehiculoID)

vehiculos_bp = Blueprint('VerVehiuclos', __name__)
vehiculoResumen_bp = Blueprint('VerVehiculoResumen', __name__)
actVehiculo_bp = Blueprint('ActVehiculo', __name__)
verVehiculoID_bp = Blueprint('VerVehiculoID', __name__)


@vehiculos_bp.route('/Catalogos/Vehiculos/vehiculos', methods=['GET'])
@jwt_required()
def vehiculos_route():
    response = VerVehiculos()
    return response


@vehiculoResumen_bp.route('/Catalogos/Vehiculos/verVehiculoResumen', methods=['GET'])
@jwt_required()
def vehiculoResumen_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerVehiculoResumen(ID)
    return response


@actVehiculo_bp.route('/Catalogos/Vehiculos/actVehiculo', methods=['POST'])
@jwt_required()
def actUVehiculo_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response, status_code = ActVehiculo(data)

    return jsonify(response), status_code


@verVehiculoID_bp.route('/Catalogos/Usuarios/verVehiculoID', methods=['GET'])
@jwt_required()
def verVehiculoID_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerVehiculoID(ID)

    return response
