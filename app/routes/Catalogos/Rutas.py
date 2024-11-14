from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Rutas.rutas_service import verRutas, verCatRutaID, actCatRuta, actDescensoRuta, delDescensoRuta

verRutas_bp = Blueprint('verRutas', __name__)
verCatRutaID_bp = Blueprint('verCatRutaID', __name__)
actCatRuta_bp = Blueprint('actCatRuta', __name__)
actDescensoRuta_bp = Blueprint('actDescensoRuta', __name__)
delDescensoRuta_bp = Blueprint('delDescensoRuta', __name__)


@verRutas_bp.route('/Catalogos/Rutas', methods=['POST'])
@jwt_required()
def verRutas_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verRutas(data)
    return response


@verCatRutaID_bp.route('/Catalogos/Rutas/verCatRutaID', methods=['GET'])
@jwt_required()
def verCatRutaID_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verCatRutaID(ID)
    return response


@actCatRuta_bp.route('/Catalogos/Rutas/actCatRuta', methods=['POST'])
@jwt_required()
def actCatRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = actCatRuta(data)
    return response


@actDescensoRuta_bp.route('/Catalogos/Rutas/actDescensoRuta', methods=['POST'])
@jwt_required()
def actDescensoRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = actDescensoRuta(data)
    return response


@delDescensoRuta_bp.route('/Catalogos/Rutas/delDescensoRuta', methods=['DELETE'])
@jwt_required()
def delDescensoRuta_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = delDescensoRuta(data)
    return response