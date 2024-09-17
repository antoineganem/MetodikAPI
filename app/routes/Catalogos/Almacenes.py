from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Almacenes.almacenes_service import (
        VerAlmacenes, VerAlmacenResumen, ActAlmacen, VerAlmacenID)

almacenes_bp = Blueprint('VerAlmacenes', __name__)
almacenResumen_bp = Blueprint('VerAlmacenResumen', __name__)
actAlmacen_bp = Blueprint('ActAlmacen', __name__)
verAlmacenID_bp = Blueprint('VerAlmacenID', __name__)


@almacenes_bp.route('/Catalogos/Almacenes/almacenes', methods=['GET'])
@jwt_required()
def almacenes_route():
    response = VerAlmacenes()
    return response


@almacenResumen_bp.route('/Catalogos/Almacenes/verAlmacenResumen', methods=['GET'])
@jwt_required()
def almacenResumen_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerAlmacenResumen(ID)
    return response


@actAlmacen_bp.route('/Catalogos/Almacenes/actAlmacen', methods=['POST'])
@jwt_required()
def actUAlmacen_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response, status_code = ActAlmacen(data)

    return jsonify(response), status_code


@verAlmacenID_bp.route('/Catalogos/Usuarios/verAlmacenID', methods=['GET'])
@jwt_required()
def verAlmacenID_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerAlmacenID(ID)

    return response
