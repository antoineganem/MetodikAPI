from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Logistica.Rutas.rutas_service import *

verRutasModulo_bp = Blueprint('verRutasModulo', __name__)
nuevaRuta_bp = Blueprint('nuevaRuta', __name__)
verRutaID_bp = Blueprint('verRutaID', __name__)
avanzarRuta_bp = Blueprint('avanzarRuta', __name__)
verRutaDetalle_bp = Blueprint('verRutaDetalle', __name__)
agregarParadaRuta_bp = Blueprint('agregarParadaRuta', __name__)
ActParadaRuta_bp = Blueprint('ActParadaRuta', __name__)


@verRutasModulo_bp.route('/Logistica/Rutas/verRutas', methods=['GET'])
@jwt_required()
def verRutas_route():
    response = verRutasModulo()
    return response

@nuevaRuta_bp.route('/Logistica/Rutas/nuevaRuta', methods=['POST'])
@jwt_required()
def nuevaRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = nuevaRuta(data)
    return response

@verRutaID_bp.route('/Logistica/Rutas/verRutaID', methods=['GET'])
@jwt_required()
def verRutaID_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verRutaID(ID)
    return response

@avanzarRuta_bp.route('/Logistica/Rutas/AvanzarRuta', methods=['POST'])
@jwt_required()
def avanzarRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = avanzarRuta(data)
    return response

@verRutaDetalle_bp.route('/Logistica/Rutas/verRutaDetalle', methods=['GET'])
@jwt_required()
def verRutaDetalle_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verRutaDetalle(ID)
    return response

@ActParadaRuta_bp.route('/Logistica/Rutas/ActParadaRuta', methods=['POST'])
@jwt_required()
def ActParadaRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = ActParadaRuta(data)
    return response