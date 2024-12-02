from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Pasajeros.pasajeros_service import verPasajeros, actPasajeros, verPasajerosID

verPasajeros_bp = Blueprint('verPasajeros', __name__)
actPasajeros_bp = Blueprint('actPasajeros', __name__)
verPasajerosID_bp = Blueprint('verPasajerosID', __name__)


@verPasajeros_bp.route('/Catalogos/verPasajeros', methods=['POST'])
@jwt_required()
def verPasajeros_route():
    data = request.json

    if data is None: 
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verPasajeros(data)

    return user_response

@actPasajeros_bp.route('/Catalogos/actPasajeros', methods=['POST'])
@jwt_required()
def actPasajeros_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = actPasajeros(data)
    
    return user_response

@verPasajerosID_bp.route('/Catalogos/verPasajerosID',methods=['GET'])
@jwt_required()
def verPasajerosID_route():
    ID= request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verPasajerosID(ID)
    return response 

