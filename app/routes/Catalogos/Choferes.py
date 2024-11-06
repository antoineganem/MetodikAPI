from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Choferes.choferes_service import verChoferes, verChoferID, actChoferD, eliminarChofer


verChoferes_bp = Blueprint('verChoferes', __name__)
verChoferID_bp = Blueprint('verChoferID', __name__)
actChoferD_bp = Blueprint('actChoferD', __name__)
eliminarChofer_bp = Blueprint('eliminarChofer', __name__)


@verChoferes_bp.route('/Catalogos/Choferes', methods=['POST'])
@jwt_required()
def verChoferes_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verChoferes(data)
    return response


@verChoferID_bp.route('/Catalogos/Choferes/verChoferID', methods=['GET'])
@jwt_required()
def verChoferID_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verChoferID(ID)
    return response


@actChoferD_bp.route('/Catalogos/Choferes/actChoferD', methods=['POST'])
@jwt_required()
def actChoferD_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = actChoferD(data)
    return response


@eliminarChofer_bp.route('/Catalogos/Choferes/eliminarChofer', methods=['DELETE'])
# @jwt_required()
def eliminarChofer_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = eliminarChofer(ID)
    return response