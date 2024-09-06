from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Comercial.Reservas.reservasD_service import verReservaID, avanzaReserva

verReservaID_bp = Blueprint('verReservaID', __name__)
avanzaReserva_bp = Blueprint('avanzaReserva', __name__)







@verReservaID_bp.route('/Comercial/Reservas/verReservaID', methods=['GET'])
@jwt_required()
def usuarios_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)  

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = verReservaID(ID)
    
    return response

@avanzaReserva_bp.route('/Comercial/Reservas/avanzarReserva', methods=['POST'])
@jwt_required()
def nvaReserva_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = avanzaReserva(data)
    
    return response




