from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Comercial.Reservas.reservas_service import verReservas, nvaReserva

verReservas_bp = Blueprint('verReservas', __name__)
nvaReserva_bp = Blueprint('nvaReserva', __name__)






@verReservas_bp.route('/Comercial/verReservas', methods=['POST'])
@jwt_required()
def verReservas_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verReservas(data)
    
    return user_response

@nvaReserva_bp.route('/Comercial/NuevaReserva', methods=['POST'])
@jwt_required()
def nvaReserva_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = nvaReserva(data)
    
    return user_response


