from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Perfiles.perfiles_service import *

verPerfiles_bp = Blueprint('verPerfiles', __name__)
verPerfilID_bp = Blueprint('verPerfilID', __name__)
actPerfil_bp = Blueprint('actPerfil', __name__)
verModulosAcceso_bp = Blueprint('verModulosAcceso', __name__)
actAccesosPerfil_bp = Blueprint('actAccesosPerfil', __name__)
crearMenus_bp = Blueprint('crearMenus', __name__)


@verPerfiles_bp.route('/Catalogos/Perfiles/verPerfiles', methods=['GET'])
@jwt_required()
def perfiles_route():
    EstatusID = request.args.get('EstatusID')
    EmpresaID = request.args.get('EmpresaID')
    Buscar = request.args.get('SearchText')

    if EstatusID is None or EmpresaID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verPerfiles(EstatusID, EmpresaID, Buscar)
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

@verModulosAcceso_bp.route('/Catalogos/Perfiles/verModulosAcceso', methods=['GET'])
@jwt_required()
def verModulosAcceso_route():
    PerfilID = request.args.get('PerfilID')
    PersonaID = request.args.get('PersonaID')

    if PerfilID is None or PersonaID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verModulosAcceso(PerfilID, PersonaID)
    return response

@actAccesosPerfil_bp.route('/Catalogos/Perfiles/actAccesosPerfil', methods=['POST'])
@jwt_required()
def actAccesosPerfil_route():
    data = request.json
    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = actAccesosPerfil(data)
    return response

@crearMenus_bp.route('/Catalogos/Perfiles/crearMenus', methods=['GET'])
@jwt_required()
def verModulosAcceso_route():
    PersonaID = request.args.get('PersonaID')

    if PersonaID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = crearMenus(PersonaID)
    return response