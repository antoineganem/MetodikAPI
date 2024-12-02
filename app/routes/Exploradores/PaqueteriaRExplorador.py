from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Exploradores.paqueteriaRExplorador_service import ( verPaqueteriaR )

verPaqueteriaR_bp = Blueprint('verPaqueteriaR', __name__)


@verPaqueteriaR_bp.route('/Exploradores/verPaqueteriaR', methods=['POST'])
@jwt_required()
def verPaqueteriaR_route():
    data = request.json
    
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = verPaqueteriaR(data)

    return user_response