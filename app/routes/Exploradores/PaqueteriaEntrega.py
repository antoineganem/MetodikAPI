from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Exploradores.paqueteriaEntrega_service import (verPaqueteriaEntrega)

verPaqueteriaEntrega_bp = Blueprint('verPaqueteriaEntrega', __name__)


@verPaqueteriaEntrega_bp.route('/Exploradores/verPaqueteriaEntrega', methods=['POST'])
@jwt_required()
def verPaqueteriaEntrega_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = verPaqueteriaEntrega(data)
    
    return user_response