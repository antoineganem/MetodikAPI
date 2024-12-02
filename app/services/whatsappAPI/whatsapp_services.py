from app.messagingServices.whatsappAPI import send_message_template, send_message,handle_message, verify, upload_media, start_conversation, enviarEstadosCuenta1, enviarEstadoCuenta2, enviarEstadoCuenta3
from app.messagingServices.whatsappSP import message_data, leerMensajesPorWAID, verUsuariosWAPP, marcarComoLeido

def send_template_service(data):
    return send_message_template(data)

def get_message_data(data):
    return message_data(data)

def send_message_service(receipient_WAID, text):
    return send_message(receipient_WAID, text)

def handle_message_service():
    return handle_message()

def verify_service():
    return verify()

def upload_media_service(data):
    return upload_media(data)

def start_conversation(data):
    return start_conversation(data)

def leerMensajesPorWAID_service(data):
    return leerMensajesPorWAID(data)

def verUsuariosWAPP_service():
    return verUsuariosWAPP()

def marcarComoLeido_service(data):
    return marcarComoLeido(data)

def enviarEstadoCuenta1_service():
    return enviarEstadosCuenta1()

def enviarEstadoCuenta2_service():
    return enviarEstadoCuenta2()

def enviarEstadoCuenta3_service():
    return enviarEstadoCuenta3()