from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Exploradores.rutasExplorador_service import verExploradorRutas, verExploradorRutasID

verExploradorRutas_bp = Blueprint('verExploradorRutas', __name__)
verExploradorRutasID_bp = Blueprint('verExploradorRutasID', __name__)




@verExploradorRutas_bp.route('/Exploradores/Rutas', methods=['GET'])
@jwt_required()
def verExploradorRutas_route():
    response = verExploradorRutas()
    return response

@verExploradorRutasID_bp.route('/Exploradores/Rutas/RutasDetalle', methods=['GET'])
@jwt_required()
def erExploradorRutasID_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verExploradorRutasID(ID)
    return response
