from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Destinos.destinos_service import (
       verDestinos,actDestinos,verDestinoID)

verDestinos_bp = Blueprint('verDestinos', __name__)
actDestino_bp = Blueprint('actDestino', __name__)
verDestinoID_bp = Blueprint('verDestinoID', __name__)


@verDestinos_bp.route('/Catalogos/verDestinos',methods=['POST'])
@jwt_required()
def verDestinos_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = verDestinos(data)

    return user_response

@actDestino_bp.route('/Catalogos/actDestino', methods=['POST'])
@jwt_required()
def actDestino_route():
    data= request.json 

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    user_response = actDestinos(data)

    return user_response

@verDestinoID_bp.route('/Catalogos/verDestinoID',methods=['GET'])
@jwt_required()
def verDestinoID_route():
    ID = request.args.get('ID')

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verDestinoID(ID)
    return response