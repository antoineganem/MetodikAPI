from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Exploradores.rutasExplorador_service import *

verExploradorRutas_bp = Blueprint('verExploradorRutas', __name__)
verExploradorRutasID_bp = Blueprint('verExploradorRutasID', __name__)
VerParadasRutasExp_bp = Blueprint('VerParadasRutasExp', __name__)
verPasajerosRuta_bp = Blueprint('verPasajerosRuta', __name__)




@verExploradorRutas_bp.route('/Exploradores/Rutas/VerRutasExplorador', methods=['POST'])
@jwt_required()
def verExploradorRutas_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verExploradorRutas(data)
    return response

@verExploradorRutasID_bp.route('/Exploradores/Rutas/RutasDetalle', methods=['GET'])
@jwt_required()
def erExploradorRutasID_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verExploradorRutasID(ID)
    return response

@VerParadasRutasExp_bp.route('/Exploradores/Rutas/VerParadasRutasExp', methods=['GET'])
@jwt_required()
def VerParadasRutasExp_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = VerParadasRutasExp(ID)
    return response

@verPasajerosRuta_bp.route('/Exploradores/Rutas/verPasajerosRuta', methods=['GET'])
@jwt_required()
def verPasajerosRuta_route():
    RutaID = request.args.get('RutaID')
    ParadaID = request.args.get('ParadaID')

    if RutaID is None or ParadaID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    response = verPasajerosRuta(RutaID, ParadaID)
    return response

