from flask import Blueprint, request
from app.services.whatsappAPI.whatsapp_services import send_template_service, get_message_data, send_message_service, verify_service, handle_message_service
from flask_jwt_extended import  jwt_required

whatsapp_bp = Blueprint('whatsapp', __name__)
get_message_data_bp = Blueprint('getMessageData', __name__)
send_message_bp = Blueprint('sendMessageData', __name__)
webhook_verify_bp = Blueprint('webhook', __name__)
webhook_bp = Blueprint('webhookRoute', __name__)

@whatsapp_bp.route('/send_message', methods=['POST'])
def send_message_route():
    data = request.json
    send_message_response = send_template_service(data)
    return send_message_response, 200

@get_message_data_bp.route('/get_message_data', methods=['POST'])
@jwt_required()
def get_message_data_route():
    data = request.json
    get_message_data_response = get_message_data(data)
    return get_message_data_response, 200

@send_message_bp.route('/answer_message', methods=['POST'])
@jwt_required()
def answer_message_route():
    data = request.json
    recipient_WAID = data.get('recipient_WAID')
    text = data.get('text')
    send_message_response = send_message_service(recipient_WAID, text)
    return send_message_response, 200

# Webhook verification route
@webhook_verify_bp.route('/webhook', methods=['GET'])
def webhook_route():
    return verify_service()

# Webhook route
@webhook_bp.route('/webhook', methods=['POST'])
def webhook_route():
    return handle_message_service()
