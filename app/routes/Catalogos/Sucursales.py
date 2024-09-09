from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Sucursales.sucursales_service import (
        VerSucursales, VerSucursalResumen, ActSucursal, VerSucursalID)

sucursales_bp = Blueprint('VerSucursales', __name__)
sucursalResumen_bp = Blueprint('VerSucursalResumen', __name__)
actSucursal_bp = Blueprint('ActSucursal', __name__)
verSucursalID_bp = Blueprint('VerSucursalID', __name__)


@sucursales_bp.route('/Catalogos/Sucursales/sucursales', methods=['GET'])
@jwt_required()
def sucursales_route():
    response = VerSucursales()
    return response


@sucursalResumen_bp.route('/Catalogos/Sucursal/verSucursalResumen', methods=['GET'])
@jwt_required()
def sucursalResumen_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerSucursalResumen(ID)
    return response


@actSucursal_bp.route('/Catalogos/Sucursales/actSucursal', methods=['POST'])
@jwt_required()
def actUSucursal_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response, status_code = ActSucursal(data)

    return jsonify(response), status_code


@verSucursalID_bp.route('/Catalogos/Usuarios/verSucursalID', methods=['GET'])
@jwt_required()
def verSucursalID_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerSucursalID(ID)

    return response
