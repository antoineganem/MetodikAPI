from flask import Blueprint, request
from app.services.whatsappAPI.whatsapp_services import send_template_service, get_message_data, send_message_service, verify_service, handle_message_service, upload_media_service, start_conversation, leerMensajesPorWAID_service, verUsuariosWAPP_service
from app.services.whatsappAPI.whatsapp_services import leerMensajesPorWAID_service, verUsuariosWAPP_service, enviarEstadoCuenta1_service, enviarEstadoCuenta2_service, enviarEstadoCuenta3_service, marcarComoLeido_service
from flask_jwt_extended import  jwt_required

whatsapp_bp = Blueprint('whatsapp', __name__)
get_message_data_bp = Blueprint('getMessageData', __name__)
send_message_bp = Blueprint('sendMessageData', __name__)
webhook_verify_bp = Blueprint('webhook', __name__)
webhook_bp = Blueprint('webhookRoute', __name__)
upload_media_bp = Blueprint('uploadMedia', __name__)
start_conversation_bp = Blueprint('startConversation', __name__)
leerMensajesPorWAID_bp = Blueprint('leerMensajesPorWAID', __name__)
verUsuariosWAPP_bp = Blueprint('verUsuariosWAPP', __name__)
enviarEstadoCuenta1_bp = Blueprint('enviarEstadoCuenta1',__name__)
enviarEstadoCuenta2_bp = Blueprint('enviarEstadoCuenta2',__name__)
enviarEstadoCuenta3_bp = Blueprint('enviarEstadoCuenta3',__name__)
marcarComoLeido_bp = Blueprint('marcarComoLeido',__name__)

@whatsapp_bp.route('/send_message', methods=['POST'])
def send_message_route():
    data = request.json
    print(data)
    send_message_response = send_template_service(data)
    return send_message_response, 200

@get_message_data_bp.route('/get_message_data', methods=['POST'])
@jwt_required()
def get_message_data_route():
    data = request.json
    print(data)
    get_message_data_response = get_message_data(data)
    return get_message_data_response 

@send_message_bp.route('/answer_message', methods=['POST'])
@jwt_required()
def answer_message_route():
    data = request.json
    recipient_WAID = data.get('recipient_WAID')
    text = data.get('text')
    send_message_response = send_message_service(recipient_WAID, text)
    return send_message_response 

# Webhook verification route
@webhook_verify_bp.route('/webhook', methods=['GET'])
def webhook_route():
    return verify_service()

# Webhook route
@webhook_bp.route('/webhook', methods=['POST'])
def webhook_route():
    return handle_message_service()

@upload_media_bp.route('/upload_media', methods=['POST'])
@jwt_required()
def upload_media_route():
    data = request.json
    upload_media_response = upload_media_service(data)
    return upload_media_response 


@start_conversation_bp.route('/start_conversation', methods=['POST'])
@jwt_required()
def start_conversation_route():
    data = request.json
    start_conversation_response = start_conversation(data)
    return start_conversation_response 

@leerMensajesPorWAID_bp.route('/leerMensajes', methods=['POST'])
@jwt_required()
def leerMensajesPorWAID_route():
    data = request.json
    leerMensajesPorWAID_response = leerMensajesPorWAID_service(data)
    return leerMensajesPorWAID_response

@marcarComoLeido_bp.route('/marcarComoLeido', methods=['POST'])
@jwt_required()
def marcarComoLeido_route():
    data = request.json
    marcarComoLeido_response = marcarComoLeido_service(data)
    return marcarComoLeido_response

@verUsuariosWAPP_bp.route('/verUsuarios', methods=['GET'])
@jwt_required()
def verUsuariosWAPP_route():
    verUsuariosWAPP_response = verUsuariosWAPP_service()
    return verUsuariosWAPP_response


@enviarEstadoCuenta1_bp.route('/enviarEstadoCuenta1',methods=['GET'])
def enviarEstadoCuenta1():
    #data = request.json

    #to_number = data.get('Telefono'),
    #template_name = data.get('Plantilla'),
    #parameters = data.get('Parametros',[])

    #send_template_response = send_templates_service(to_number,template_name, *parameters)

    #return send_template_response
    
    data =  enviarEstadoCuenta1_service()
    
    return data

@enviarEstadoCuenta2_bp.route('/enviarEstadoCuenta2', methods=['GET'])
def enviarEstadoCuenta2():

    data = enviarEstadoCuenta2_service()

    return data

@enviarEstadoCuenta3_bp.route('/enviarEstadoCuenta3',methods=['GET'])
def enviarEstadosCuenta3():

    data = enviarEstadoCuenta3_service()

    return data