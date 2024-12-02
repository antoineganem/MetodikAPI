from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Logistica.PreciosRuta.preciosruta_service import *

verPreciosRutas_bp = Blueprint('verPreciosRutas', __name__)
actPreciosRuta_bp = Blueprint('actPreciosRuta', __name__)
afectarCambioPreciosRuta_bp = Blueprint('afectarCambioPreciosRuta', __name__)


@verPreciosRutas_bp.route('/Logistica/PreciosRutas/verPreciosRutas', methods=['GET'])
@jwt_required()
def verPreciosRutas_route():
    EmpresaID = request.args.get('EmpresaID')
    OrigenID = request.args.get('OrigenID')
    DestinoID = request.args.get('DestinoID')

    if EmpresaID is None or OrigenID is None or DestinoID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verPreciosRutas(EmpresaID, OrigenID, DestinoID)
    return response

@actPreciosRuta_bp.route('/Logistica/PreciosRutas/actPreciosRuta', methods=['POST'])
@jwt_required()
def actPreciosRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = actPreciosRuta(data)
    return response

@afectarCambioPreciosRuta_bp.route('/Logistica/PreciosRutas/afectarCambioPreciosRuta', methods=['POST'])
@jwt_required()
def afectarCambioPreciosRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = afectarCambioPreciosRuta(data)
    return response