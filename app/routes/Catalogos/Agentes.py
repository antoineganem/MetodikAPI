from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Agentes.agentes_service import verAgentes, verAgentesResumen, ActualizarAgentes, VerAgenteID  


agentes_bp = Blueprint('verAgentes', __name__)
agentesResumen_bp = Blueprint('verAgentesResumen', __name__)
actAgente_bp = Blueprint('ActualizarAgentes', __name__)
verAgenteID_bp = Blueprint('VerAgenteID', __name__)




@agentes_bp.route('/Catalogos/Agentes/agentes', methods=['GET'])
@jwt_required()
def agentes_route():
    EmpresaID = request.args.get('EmpresaID')
    EstatusID = request.args.get('EstatusID')

    print("Datos recibidos:", EmpresaID, EstatusID)  

    if EmpresaID is None or EstatusID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    agente_response = verAgentes(EmpresaID, EstatusID)
    
    return agente_response

@agentesResumen_bp.route('/Catalogos/Agentes/verAgentesResumen', methods=['GET'])
@jwt_required()
def agentesResumen_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)  

    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    agenteResumen_response = verAgentesResumen(ID)
    
    return agenteResumen_response



@actAgente_bp.route('/Catalogos/Agentes/actAgentes', methods=['POST'])
@jwt_required()
def actAgentes_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    actAgentes_response, status_code = ActualizarAgentes(data)
    
    return jsonify(actAgentes_response), status_code

@verAgenteID_bp.route('/Catalogos/Agentes/verAgenteID', methods=['GET'])
@jwt_required()
def agentes_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)  

    if ID is None: 
        return jsonify({"error": "Faltan datos requeridos"}), 400

    agente_response = VerAgenteID(ID)
    
    return jsonify(agente_response)
