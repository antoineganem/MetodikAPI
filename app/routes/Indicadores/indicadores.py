from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Indicadores.indicadores_service import verIndicadores

verIndicadores_bp = Blueprint('verIndicadores', __name__)






@verIndicadores_bp.route('/Indicadores', methods=['POST'])
@jwt_required()
def verIndicadores_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verIndicadores(data)
    
    return user_response



