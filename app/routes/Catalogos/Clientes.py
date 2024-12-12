from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Clientes.clientes_service import verClienteID, verClientes, actCliente

verClientes_bp = Blueprint('verClientes', __name__)
verClienteID_bp = Blueprint('verClienteID', __name__)
actCliente_bp = Blueprint('actCliente', __name__)

@verClientes_bp.route('/Catalogos/Clientes', methods=['POST'])
@jwt_required()
def verClientes_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verClientes(data)
    return response


@verClienteID_bp.route('/Catalogos/Clientes/verClienteID', methods=['GET'])
@jwt_required()
def verClienteID_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verClienteID(ID)
    return response


@actCliente_bp.route('/Catalogos/Clientes/actCliente', methods=['POST'])
@jwt_required()
def actCliente_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = actCliente(data)
    return response