from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Destinos.destinos_service import (
        VerDestinos, VerDestinoResumen, ActDestino, VerDestinoID)

destinos_bp = Blueprint('VerDestinos', __name__)
destinoResumen_bp = Blueprint('VerDestinoResumen', __name__)
actDestino_bp = Blueprint('ActDestino', __name__)
verDestinoID_bp = Blueprint('VerDestinoID', __name__)


@destinos_bp.route('/Catalogos/Destinos/destinos', methods=['GET'])
@jwt_required()
def destinos_route():
    response = VerDestinos()
    return response


@destinoResumen_bp.route('/Catalogos/Destinos/verDestinoResumen', methods=['GET'])
@jwt_required()
def destinoResumen_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerDestinoResumen(ID)
    return response


@actDestino_bp.route('/Catalogos/Destinos/actDestino', methods=['POST'])
@jwt_required()
def actUDestino_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response, status_code = ActDestino(data)

    return jsonify(response), status_code


@verDestinoID_bp.route('/Catalogos/Usuarios/verDestinoID', methods=['GET'])
@jwt_required()
def verDestinoID_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerDestinoID(ID)

    return response
