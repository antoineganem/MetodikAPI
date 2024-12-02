from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Sucursales.sucursales_service import (
        verSucursales,actSucursal,verSucursalID)

verSucursales_bp = Blueprint('verSucursales', __name__)
actSucursal_bp = Blueprint('actSucursal', __name__)
verSucursalID_bp = Blueprint('verSucursalID', __name__)


@verSucursales_bp.route('/Catalogos/verSucursales', methods=['POST'])
@jwt_required()
def sucursales_route():
    data= request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verSucursales(data)

    return user_response

@actSucursal_bp.route('/Catalogos/actSucursal', methods=['POST'])
@jwt_required()
def actUSucursal_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = actSucursal(data)

    return user_response


@verSucursalID_bp.route('/Catalogos/verSucursalID', methods=['GET'])
@jwt_required()
def verSucursalID_route():
    ID = request.args.get('ID')

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verSucursalID(ID)
    return response
