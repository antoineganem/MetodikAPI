from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Usuarios.usuarios_service import verUsuarios, verUsuariosResumen, ActualizarUsuarios, VerUsuarioID  


usuarios_bp = Blueprint('verUsuarios', __name__)
usuariosResumen_bp = Blueprint('verUsuariosResumen', __name__)
actUsuario_bp = Blueprint('ActualizarUsuarios', __name__)
verUsuarioID_bp = Blueprint('VerUsuarioID', __name__)




@usuarios_bp.route('/Catalogos/Usuarios/usuarios', methods=['GET'])
@jwt_required()
def usuarios_route():
    EmpresaID = request.args.get('EmpresaID')
    EstatusID = request.args.get('EstatusID')

    print("Datos recibidos:", EmpresaID, EstatusID)  

    if EmpresaID is None or EstatusID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = verUsuarios(EmpresaID, EstatusID)
    
    return user_response

@usuariosResumen_bp.route('/Catalogos/Usuarios/verUsuariosResumen', methods=['GET'])
@jwt_required()
def usuariosResumen_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)  

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    userResumen_response = verUsuariosResumen(ID)
    
    return userResumen_response



@actUsuario_bp.route('/Catalogos/Usuarios/actUsuarios', methods=['POST'])
@jwt_required()
def actUsuarios_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    actUsuarios_response, status_code = ActualizarUsuarios(data)
    
    return jsonify(actUsuarios_response), status_code

@verUsuarioID_bp.route('/Catalogos/Usuarios/verUsuarioID', methods=['GET'])
@jwt_required()
def usuarios_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)  

    if ID is None: 
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user_response = VerUsuarioID(ID)
    
    return jsonify(user_response)