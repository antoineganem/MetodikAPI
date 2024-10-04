from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Comercial.Paqueteria.paqueteria_service import *

verPaqueteria_bp = Blueprint('verPaqueteria', __name__)
nuevaPaqueteria_bp = Blueprint('nuevaPaqueteria', __name__)
verPaqueteriaID_bp = Blueprint('verPaqueteriaID', __name__)
verArtDispPaqueteria_bp = Blueprint('verArtDispPaqueteria', __name__)


@verPaqueteria_bp.route('/Comercial/Paqueteria/verPaqueterias', methods=['GET'])
@jwt_required()
def verPaqueteria_route():
    response = verPaqueteria()
    return response


@nuevaPaqueteria_bp.route('/Comercial/Paqueteria/nuevaPaqueteria', methods=['POST'])
@jwt_required()
def nuevaPaqueteria_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = nuevaPaqueteria(data)
    return response


@verPaqueteriaID_bp.route('/Comercial/Paqueteria/verPaqueteriaID', methods=['GET'])
@jwt_required()
def verPaqueteriaID_route():
    ID = request.args.get('ID')
    
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verPaqueteriaID(ID)
    return response

@verArtDispPaqueteria_bp.route('/Comercial/Paqueteria/verArtDispPaqueteria', methods=['GET'])
@jwt_required()
def verArtDispPaqueteria_route():
    EmpresaID = request.args.get('EmpresaID')
    
    if EmpresaID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verArtDispPaqueteria(EmpresaID)
    return response