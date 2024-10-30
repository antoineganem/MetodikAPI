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
eliminarParadaRuta_bp = Blueprint('eliminarParadaRuta', __name__)
verParadaRutasDisponible_bp = Blueprint('verParadaRutasDisponible', __name__)
copiarRuta_bp = Blueprint('copiarRuta', __name__)
eliminarRuta_bp = Blueprint('eliminarRuta', __name__)
cancelarRuta_bp = Blueprint('cancelarRuta', __name__)
afectarRuta_bp = Blueprint('afectarRuta', __name__)
cambiarsituacionRuta_bp = Blueprint('cambiarsituacionRuta', __name__)

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

@verParadaRutasDisponible_bp.route('/Logistica/Rutas/verParadaRutasDisponible', methods=['GET'])
@jwt_required()
def verParadaRutasDisponible_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verParadaRutasDisponible(ID)
    return response

@ActParadaRuta_bp.route('/Logistica/Rutas/ActParadaRuta', methods=['POST'])
@jwt_required()
def ActParadaRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = ActParadaRuta(data)
    return response


@agregarParadaRuta_bp.route('/Logistica/Rutas/agregarParadaRuta', methods=['POST'])
@jwt_required()
def agregarParadaRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = agregarParadaRuta(data)
    return response


@eliminarParadaRuta_bp.route('/Logistica/Rutas/eliminarParadaRuta', methods=['DELETE'])
@jwt_required()
def eliminarParadaRuta_route():
    ID = request.args.get('ID')
    RenglonID = request.args.get('RenglonID')
    UsuarioID = request.args.get('UsuarioID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = eliminarParadaRuta(ID, RenglonID, UsuarioID)
    return response

@copiarRuta_bp.route('/Logistica/Rutas/copiarRuta', methods=['POST'])
@jwt_required()
def copiarRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = copiarRuta(data)
    return response

@eliminarRuta_bp.route('/Logistica/Rutas/eliminarRuta', methods=['DELETE'])
@jwt_required()
def eliminarRuta_route():
    ID = request.args.get('ID')
    UsuarioID = request.args.get('UsuarioID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = eliminarRuta(ID, UsuarioID)
    return response


@cancelarRuta_bp.route('/Logistica/Rutas/cancelarRuta', methods=['POST'])
@jwt_required()
def cancelarRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = cancelarRuta(data)
    return response

@afectarRuta_bp.route('/Logistica/Rutas/afectarRuta', methods=['POST'])
@jwt_required()
def afectarRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = afectarRuta(data)
    return response

@cambiarsituacionRuta_bp.route('/Logistica/Rutas/cambiarsituacionRuta', methods=['POST'])
@jwt_required()
def cambiarsituacionRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = cambiarsituacionRuta(data)
    return response