from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Comercial.Reservas.reservasD_service import verReservaID

verReservaID_bp = Blueprint('verReservaID', __name__)






@verReservaID_bp.route('/Comercial/Reservas/verReservaID', methods=['GET'])
@jwt_required()
def usuarios_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)  

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = verReservaID(ID)
    
    return response



