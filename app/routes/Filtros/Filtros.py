from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Filtros.filtros_service import verFiltrosCatalogos

verFiltrosCatalogos_bp = Blueprint('verFiltrosCatalogos', __name__)





@verFiltrosCatalogos_bp.route('/Filtros/Catalogos', methods=['POST'])
@jwt_required()
def filtrosCatalogos_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verFiltrosCatalogos(data)
    
    return user_response

