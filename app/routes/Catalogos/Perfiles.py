from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Perfiles.perfiles_service import verPerfiles

verPerfiles_bp = Blueprint('verPerfiles', __name__)


@verPerfiles_bp.route('/Catalogos/Perfiles/verPerfiles', methods=['GET'])
@jwt_required()
def perfiles_route():
    EstatusID = request.args.get('EstatusID')
    EmpresaID = request.args.get('EmpresaID')
    if EstatusID is None or EmpresaID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    response = verPerfiles(EstatusID, EmpresaID)
    return response


