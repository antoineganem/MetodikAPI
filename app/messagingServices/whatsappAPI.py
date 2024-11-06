import requests 
import json
from app.messagingServices.whatsappSP import leerMensajesPorWAID, actMensajeWAPP # store procedures 
from flask import jsonify,request,current_app
import os 
from dotenv import load_dotenv
import logging
#Load environment variables
load_dotenv()

TOKEN = os.getenv('TOKEN') # Access token for the Facebook Graph API
PHONE_NUMBER_ID = os.getenv('PHONE_NUMBER_ID')  # Your WhatsApp phone number ID


def process_whatsapp_message(body,remitente):

    wa_id = body["entry"][0]["changes"][0]["value"]["contacts"][0]["wa_id"]
    nombre = body["entry"][0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]

    message = body["entry"][0]["changes"][0]["value"]["messages"][0]
    mensaje = message["text"]["body"]

    tipoMensaje = message["type"]

    #save this into the database 

    data = {
        'wa_id': wa_id,
        'nombre': nombre,
        'mensaje': mensaje,
        'remitente': remitente,
        'tipoMensaje': tipoMensaje,

    }
    
    return actMensajeWAPP(data)

def is_valid_whatsapp_message(body):
    """
    Check if the incoming webhook event has a valid WhatsApp message structure.
    """

    return (
        body.get("object")
        and body.get("entry")
        and body["entry"][0].get("changes")
        and body["entry"][0]["changes"][0].get("value")
        and body["entry"][0]["changes"][0]["value"].get("messages")
        and body["entry"][0]["changes"][0]["value"]["messages"][0]
    )

#Send message template to the user
def send_message_template(data):

    if TOKEN is None:
        return jsonify({"error": "No token found in the environment variables."}), 500
   
    URL = f"https://graph.facebook.com/v20.0/452579597933631/messages"
    
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }

    message_data = {
        "messaging_product": "whatsapp",
        "to": f'{data.get("Telefono")}',
        "type": "template",
        "template": {
            "name": "rtn_boletos",
            "language": {
                "code": "es_MX" 
            },
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image":{
                                "id": f"{data.get('IDCodigoQR')}"
                            }
                        }
                    ]
                },
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": f" {data.get('Movimiento')}"
                        },
                        {
                            "type": "text",
                            "text": f"{data.get('Fecha')}"
                        },
                        {
                            "type": "text",
                            "text": f"{data.get('Pasajeros')}"
                        },
                        {
                            "type": "text",
                            "text": f"{data.get('NumeroAsiento')}"
                        },
                        {
                            "type": "text",
                            "text": f"{data.get('PrecioTotal')}"
                        },
                        {
                            "type": "text",
                            "text": f"{data.get('FechaSalida')}"
                        },
                        {
                            "type": "text",
                            "text": f"{data.get('Ruta')}"
                        },
                        {
                            "type": "text",
                            "text": f"{data.get('Nombre')}"
                        }

                    ]
                },
            ]
        }
    }

    try:
        response = requests.post(URL, headers=headers, json=message_data)

        return jsonify((response.json()), response.status_code)
    
    except requests.exceptions.RequestException as e:
        print()
        ##return jsonify({"error": str(e)}), 500
    

#Function to respond to user onces the user has sent a message
def send_message(receipient_WAID, text):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

    url = f"https://graph.facebook.com/v20.0/452579597933631/messages"

    # The JSON to send to the API
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": receipient_WAID,
        "type": "text",
        "text": {"preview_url": False, "body": text},
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        db_data = {
            "wa_id": receipient_WAID,
            "nombre": "Agente",
            "mensaje": text,
            "type": "text",
            "remitente": "agente",
        }
        status = actMensajeWAPP(db_data)
        print("Status db", status)
        print("Status:", response.status_code)
        print("Content-type:", response.headers["content-type"])
        print("Body:", response.text)
        return jsonify(response.text, 200)
    else:
        print(response.status_code)
        print(response.text)
        return response, 500

#Function to handle incoming messages from the WhatsApp API
def handle_message():
    """
    Handle incoming webhook events from the WhatsApp API.

    This function processes incoming WhatsApp messages and other events,
    such as delivery statuses. If the event is a valid message, it gets
    processed. If the incoming payload is not a recognized WhatsApp event,
    an error is returned.

    Every message send will trigger 4 HTTP requests to your webhook: message, sent, delivered, read.

    Returns:
        response: A tuple containing a JSON response and an HTTP status code.
    """
    body = request.get_json()

    # logging.info(f"request body: {body}")

    # Check if it's a WhatsApp status update
    if (
        body.get("entry", [{}])[0]
        .get("changes", [{}])[0]
        .get("value", {})
        .get("statuses")
    ):
        logging.info("Received a WhatsApp status update.")
        return jsonify({"status": "ok"}), 200

    try:
        if is_valid_whatsapp_message(body):
            print("body", body)
            status = process_whatsapp_message(body,'cliente')
            print("status", status) 
            return jsonify({"status": "ok"}), 200
        else:
            # if the request is not a WhatsApp API event, return an error
            return (
                jsonify({"status": "error", "message": "Not a WhatsApp API event"}),
                404,
            )
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON")
        return jsonify({"status": "error", "message": "Invalid JSON provided"}), 400


# Required webhook verifictaion for WhatsApp
def verify():
    # Parse params from the webhook verification request
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    # Check if a token and mode were sent
    if mode and token:
        # Check the mode and token sent are correct
        if mode == "subscribe" and token == os.getenv("VERIFY_TOKEN"):
            # Respond with 200 OK and challenge token from the request
            logging.info("WEBHOOK_VERIFIED")
            return challenge, 200
        else:
            # Responds with '403 Forbidden' if verify tokens do not match
            logging.info("VERIFICATION_FAILED")
            return jsonify({"status": "error", "message": "Verification failed"}), 403
    else:
        # Responds with '400 Bad Request' if verify tokens do not match
        logging.info("MISSING_PARAMETER")
        return jsonify({"status": "error", "message": "Missing parameters"}), 400

def upload_media(data): 

    try:    

        # Get the route of the media file 
        media = data.get("media")


        url = f"https://graph.facebook.com/v21.0/452579597933631/media"

        headers = {
            'Authorization': f'Bearer {TOKEN}'
        }

        form_data = {
            'messaging_product': 'whatsapp',
            'type': 'image/png',
        }

        files = {
            'file': ('default.png', open(media,'rb'), 'image/png',  {'Expires': '0'}),  # Open the file in binary mode
            'type': 'image/png'  # Ensure the type is correct for the file you're sending
        }


        response = requests.post(url, headers= headers, files=files, data=form_data)

        if response.status_code == 200:
            return response.json() 
        else:
            return {"error": response.json()} 

    except FileNotFoundError:
        return {"error": "File not found"}  
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"} 
    
    except Exception as e:
        return {"error": str(e)} 
    
def start_conversation(data):
    """
    Start a conversation with a user on WhatsApp using the Facebook Graph API.
    """
    try: 

        URL = f"https://graph.facebook.com/v20.0/452579597933631/messages"
            
        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {TOKEN}",
        }

        data = {
            "messaging_product": "whatsapp",
            "to": f"{data.get('Telefono')}",
            "type": "template",
            "template": {
                "name": "hello_world", # plantilla temporal
                "language": {
                    "code": "en_US"
                },
            }
        }
        
        response = requests.post(URL, headers=headers, json=data)

        if response.status_code == 200:
            return jsonify(response.json())
        
        else: 
            return response.json()
        
    except requests.exceptions.RequestException as e:
            
        return jsonify({"error": f"Request failed: {str(e)}"})
        
