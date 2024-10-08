from app.messagingServices.whatsappAPI import message_data, send_message

def send_message_service(data):
    return send_message(data)

def get_message_data(data):
    return message_data(data)