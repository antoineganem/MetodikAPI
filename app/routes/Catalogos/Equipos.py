from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Equipos.equipos_service import verEquipoID, verEquipos, actEquipoD, eliminarEquipo


verEquipos_bp = Blueprint('verEquipos', __name__)
verEquipoID_bp = Blueprint('verEquipoID', __name__)
actEquipoD_bp = Blueprint('verEquipoD', __name__)
eliminarEquipo_bp = Blueprint('eliminarEquipo', __name__)


@verEquipos_bp.route('/Catalogos/Equipos', methods=['POST'])
@jwt_required()
def verEquipos_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verEquipos(data)
    return response


@verEquipoID_bp.route('/Catalogos/Equipos/verEquipoID', methods=['GET'])
@jwt_required()
def verEquipoID_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos."}), 400
    response = verEquipoID(ID)
    return response


@actEquipoD_bp.route('/Catalogos/Equipos/actEquipoD', methods=['POST'])
@jwt_required()
def actEquipoD_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos."}), 400
    response = actEquipoD(data)
    return response


@eliminarEquipo_bp.route('/Catalogos/Equipos/eliminarEquipo', methods=['DELETE'])
@jwt_required()
def eliminarEquipo_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos."}), 400
    response = eliminarEquipo(ID)
    return response