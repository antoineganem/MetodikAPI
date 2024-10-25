from app.messagingServices.whatsappAPI import send_message_template, send_message,handle_message, verify
from app.messagingServices.whatsappSP import message_data

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
