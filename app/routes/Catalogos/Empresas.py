from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Empresas.empresas_service import verEmpresas, VerEmpresasResumen, ActEmpresa, VerEmpresaID

empresas_bp = Blueprint('verEmpresas', __name__)
empresasResumen_bp = Blueprint('VerEmpresasResumen', __name__)
actEmpresa_bp = Blueprint('ActEmpresa', __name__)
verEmpresaID_bp = Blueprint('VerEmpresaID', __name__)




@empresas_bp.route('/Catalogos/Empresas/empresas', methods=['GET'])
@jwt_required()
def empresas_route():
    response = verEmpresas()
    return response




@empresasResumen_bp.route('/Catalogos/Empresas/verEmpresasResumen', methods=['GET'])
@jwt_required()
def empresasResumen_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerEmpresasResumen(ID)
    return response



@actEmpresa_bp.route('/Catalogos/Empresas/actEmpresa', methods=['POST'])
@jwt_required()
def actUEmpresa_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    response, status_code = ActEmpresa(data)
    
    return jsonify(response), status_code



@verEmpresaID_bp.route('/Catalogos/Usuarios/verEmpresaID', methods=['GET'])
@jwt_required()
def verEmpresaID_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)  

    if ID is None: 
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerEmpresaID(ID)
    
    return response
    

