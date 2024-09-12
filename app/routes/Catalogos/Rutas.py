from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Rutas.rutas_service import VerRutas, VerRutasResumen, ActRuta

rutas_bp = Blueprint('verRutas', __name__)
rutasResumen_bp = Blueprint('verRutasResumen', __name__)
actRuta_bp = Blueprint('actRuta', __name__)


@rutas_bp.route('/Catalogos/Rutas/rutas', methods=['GET'])
@jwt_required()
def rutas_route():
    response = VerRutas()
    return response

@rutasResumen_bp.route('/Catalogos/Rutas/verRutasResumen', methods=['GET'])
@jwt_required()
def rutasResumen_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerRutasResumen(ID)
    return response

@actRuta_bp.route('/Catalogos/Rutas/actRuta', methods=['POST'])
@jwt_required()
def actRuta_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    response, status_code = ActRuta(data)

    return jsonify(response), status_code

