from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Choferes.choferes_services import VerChoferes_SR, VerChoferesResumen_SR, ActChoferes_SR, VerChoferID_SR

choferes_bp = Blueprint('VerChoferes_SR', __name__)
choferesResumen_bp = Blueprint('VerChoferesResumen_SR', __name__)
actChoferes_bp = Blueprint('ActChoferes_SR', __name__)
verChoferID_bp = Blueprint('VerChoferID_SR', __name__)


@choferes_bp.route('/Catalogos/Choferes/choferes', methods=['GET'])
@jwt_required()
def choferes_route():
    response = VerChoferes_SR()
    return response



@choferesResumen_bp.route('/Catalogos/Choferes/verChoferesResumen', methods=['GET'])
@jwt_required()
def choferesResumen_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerChoferesResumen_SR(ID)
    return response



@actChoferes_bp.route('/Catalogos/Choferes/actChoferes', methods=['POST'])
@jwt_required()
def actChoferes_route():
    data = request.json
    
    if data is None or data == {}:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    response, status_code = ActChoferes_SR(data)
  
    return jsonify(response), status_code

@verChoferID_bp.route('/Catalogos/Choferes/verChoferID', methods=['GET'])
@jwt_required()
def choferes_route():
    ID = request.args.get('ID')

    print("Datos recibidos:", ID)  

    if ID is None: 
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerChoferID_SR(ID)
    
    return response
