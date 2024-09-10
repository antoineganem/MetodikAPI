from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Perfiles.perfiles_service import verPerfiles, verPerfilID, actPerfil

verPerfiles_bp = Blueprint('verPerfiles', __name__)
verPerfilID_bp = Blueprint('verPerfilID', __name__)
actPerfil_bp = Blueprint('actPerfil', __name__)


@verPerfiles_bp.route('/Catalogos/Perfiles/verPerfiles', methods=['GET'])
@jwt_required()
def perfiles_route():
    EstatusID = request.args.get('EstatusID')
    EmpresaID = request.args.get('EmpresaID')
    if EstatusID is None or EmpresaID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verPerfiles(EstatusID, EmpresaID)
    return response


@verPerfilID_bp.route('/Catalogos/Perfiles/verPerfilID', methods=['GET'])
@jwt_required()
def perfiles_route():
    ID = request.args.get('ID')
    
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verPerfilID(ID)
    return response

@actPerfil_bp.route('/Catalogos/Perfiles/actPerfil', methods=['POST'])
@jwt_required()
def actPerfiles_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    response = actPerfil(data)
    
    return response

