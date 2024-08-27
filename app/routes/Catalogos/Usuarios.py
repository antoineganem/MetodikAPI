from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Usuarios.usuarios_service import verUsuarios, verUsuariosResumen  


usuarios_bp = Blueprint('verUsuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['GET'])
@jwt_required()
def usuarios_route():
    EmpresaID = request.args.get('EmpresaID')
    EstatusID = request.args.get('EstatusID')

    print("Datos recibidos:", EmpresaID, EstatusID)  

    if EmpresaID is None or EstatusID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verUsuarios(EmpresaID, EstatusID)
    
    return user_response
