from flask import Blueprint, request, jsonify, Response
from app.services.whatsappAPI.whatsapp_services import send_message_service, get_message_data
from flask_jwt_extended import  jwt_required

whatsapp_bp = Blueprint('whatsapp', __name__)
get_message_data_bp = Blueprint('getMessageData', __name__)

@whatsapp_bp.route('/send_message', methods=['POST'])
@jwt_required()
def send_message_route():
    data = request.json
    send_message_response = send_message_service(data)
    return send_message_response, 200

@get_message_data_bp.route('/get_message_data', methods=['POST'])
@jwt_required()
def get_message_data_route():
    data = request.json
    get_message_data_response = get_message_data(data)
    return get_message_data_response, 200