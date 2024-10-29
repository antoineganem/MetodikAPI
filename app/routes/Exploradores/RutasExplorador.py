from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Exploradores.rutasExplorador_service import verExploradorRutas, verExploradorRutasID

verExploradorRutas_bp = Blueprint('verExploradorRutas', __name__)
verExploradorRutasID_bp = Blueprint('verExploradorRutasID', __name__)




@verExploradorRutas_bp.route('/Exploradores/Rutas/VerRutasExplorador', methods=['GET'])
@jwt_required()
def verExploradorRutas_route():
    RutaID = request.args.get('RutaID')
    Fecha = request.args.get('Fecha')
    Hora = request.args.get('Hora')

    response = verExploradorRutas(RutaID, Fecha, Hora)
    return response

@verExploradorRutasID_bp.route('/Exploradores/Rutas/RutasDetalle', methods=['GET'])
@jwt_required()
def erExploradorRutasID_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verExploradorRutasID(ID)
    return response
