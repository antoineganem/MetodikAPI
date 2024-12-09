from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Filtros.filtros_service import verFiltrosCatalogos, verFiltrosModulo

verFiltrosCatalogos_bp = Blueprint('verFiltrosCatalogos', __name__)

verFiltrosModulo_bp = Blueprint('verFiltrosModulo', __name__)


@verFiltrosCatalogos_bp.route('/Filtros/Catalogos', methods=['POST'])
@jwt_required()
def filtrosCatalogos_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verFiltrosCatalogos(data)
    
    return user_response

@verFiltrosModulo_bp.route('/Filtros/Modulos', methods=['POST'])
@jwt_required()
def filtrosModulos_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verFiltrosModulo(data)
    
    return user_response

