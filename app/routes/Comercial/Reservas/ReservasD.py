from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Comercial.Reservas.reservasD_service import verReservaID, avanzaReserva, verViajesDisponibles, verViajesDisponiblesVuelta, ActReservaD, VerReservaDetalle

verReservaID_bp = Blueprint('verReservaID', __name__)
avanzaReserva_bp = Blueprint('avanzaReserva', __name__)
verViajesDisponibles_bp = Blueprint('verViajesDisponibles', __name__)
verViajesDisponiblesVuelta_bp = Blueprint('verViajesDisponiblesVuelta', __name__)
actReservaD_bp = Blueprint('ActReservaD', __name__)
verReservaDetalle_bp = Blueprint('VerReservaDetalle', __name__)



@verReservaID_bp.route('/Comercial/Reservas/verReservaID', methods=['GET'])
@jwt_required()
def usuarios_route():
    ID = request.args.get('ID')
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

@verViajesDisponibles_bp.route('/Comercial/Reservas/verViajesDisponiblesIda', methods=['GET'])
@jwt_required()
def verViajesDisponibles_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verViajesDisponibles(ID)
    return response


@verViajesDisponiblesVuelta_bp.route('/Comercial/Reservas/verViajesDisponiblesVuelta', methods=['GET'])
@jwt_required()
def verViajesDisponiblesVuelta_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verViajesDisponiblesVuelta(ID)
    return response

@actReservaD_bp.route('/Comercial/Reservas/ActReservaD', methods=['POST'])
@jwt_required()
def actReservaD_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = ActReservaD(data)
    return response

@verReservaDetalle_bp.route('/Comercial/Reservas/verReservaDetalle', methods=['GET'])
@jwt_required()
def verReservaDetalle_route():
    ID = request.args.get('ID')
    print(ID)
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = VerReservaDetalle(ID)
    return response