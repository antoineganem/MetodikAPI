from flask import request, Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required
from app.services.Catalogos.Rutas.rutas_service import VerRutas, VerRutasResumen, ActRuta, VerHorarios, ActHorarioRuta, VerRutasHorarios, EliminarRutaHorario

rutas_bp = Blueprint('verRutas', __name__)
rutasResumen_bp = Blueprint('verRutasResumen', __name__)
actRuta_bp = Blueprint('actRuta', __name__)
verHorarios_bp = Blueprint('verHorarios', __name__)
actHorarioRuta_bp = Blueprint('actHorarioRuta', __name__)
verRutasHorarios_bp = Blueprint('verRutasHorarios', __name__)
eliminarRutaHorario_bp = Blueprint('eliminarRutaHorario', __name__)

@rutas_bp.route('/Catalogos/Rutas/rutas', methods=['GET'])
@jwt_required()
def rutas_route():
    response = VerRutas()
    return response

@rutasResumen_bp.route('/Catalogos/Rutas/verRutasResumen', methods=['GET'])
@jwt_required()
def rutasResumen_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = VerRutasResumen(ID)
    return response

@actRuta_bp.route('/Catalogos/Rutas/actRuta', methods=['POST'])
@jwt_required()
def actRuta_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    response, status_code = ActRuta(data)

    return jsonify(response), status_code


@verHorarios_bp.route('/Catalogos/Rutas/verHorarios', methods=['GET'])
@jwt_required()
def verHorarios_route():
    response = VerHorarios()
    return jsonify(response)

@actHorarioRuta_bp.route('/Catalogos/Rutas/actHorarioRuta', methods=['POST'])
@jwt_required()
def actHorarioRuta_route():
    data = request.json

    if data is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    response, status_code = ActHorarioRuta(data)

    return jsonify(response), status_code

@verRutasHorarios_bp.route('/Catalogos/Rutas/verRutasHorarios', methods=['GET'])
@jwt_required()
def verRutasHorarios_route():
    ID = request.args.get('ID')
    print (ID)
    response = VerRutasHorarios(ID)

    return (response)

@eliminarRutaHorario_bp.route('/Catalogos/Rutas/eliminarRutaHorario', methods=['DELETE'])
@jwt_required()
def eliminarRutaHorario_route():
    ID = request.args.get('ID')
    if ID is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    response = EliminarRutaHorario(ID)
    return response
