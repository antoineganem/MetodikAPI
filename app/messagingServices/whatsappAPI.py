import requests 
import json
from app.socketio_config import socketio  
from app.messagingServices.whatsappSP import leerMensajesPorWAID, actMensajeWAPP,enviarEstadoCuenta1SP, enviarEstadoCuenta2SP, enviarEstadoCuenta3SP # store procedures 
from flask import jsonify,request
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


    status = actMensajeWAPP(data)

    print(status)
    socketio.emit('new_message', status)

    return status

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
            "name": "rtn_boletos_2",
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
    print(text)
    print(receipient_WAID)
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

#Function to handle incoming messages from the WhatsApp API webhook
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
    print(body)
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
            'type': 'image/jgp',
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
        

def send_templates(to_number, template_name, *parameters):
    # Construct the parameters for the template message
    if isinstance(to_number, tuple):
        to_number = to_number[0]

    if isinstance(template_name, tuple):
        template_name = template_name[0]

    message_parameters = [
        {"type": "text", "text": param} for param in parameters
    ]
    
    # Create the payload with dynamic parameters
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {
                "code": "es_MX"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": 
                    message_parameters
                    
                }
            ]
        }
    }

    # Define headers and send request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"  # Replace with your token
    }
    
    URL = f"https://graph.facebook.com/v20.0/452579597933631/messages"
    
    try: 

        response = requests.post(URL, json=payload, headers=headers)
        print(response.json())
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(e)
        return ({"error": str(e),"status": 500}) 


def enviarEstadosCuenta1():

    client_data, status_code =  enviarEstadoCuenta1SP()
 
    acc = []

    if isinstance(client_data, list):
        for client in client_data: 

            cliente_name = client['Cliente']
            factura = client['Factura']
            importe = str(client['Importe'])
            telefono = f"+52{client['Telefono']}"

            template_name = 'contacto_1'
                
            # Send the message to each client
            response = send_templates(
                telefono,
                template_name,
                cliente_name,
                factura,
                importe
            )
            
            acc.append(response)

        return jsonify(acc),200

def enviarEstadoCuenta2():

    client_data, status_code = enviarEstadoCuenta2SP()

    acc = []

    if isinstance(client_data, list):
        for client in client_data: 

            cliente_name = client['Cliente']
        
            telefono = f"+52{client['Telefono']}"

            template_name = 'contacto_2'
                
            # Send the message to each client
            response = send_templates(
                telefono,
                template_name,
                cliente_name
            )
            
            acc.append(response)

        return jsonify(acc),200

def enviarEstadoCuenta3():

    client_data, status_code = enviarEstadoCuenta3SP()

    acc = []

    if isinstance(client_data, list):
        for client in client_data: 
        
            telefono = f"52{client['Telefono']}"

            diasVencido = client['Diasvencido']

            factura = client['Factura']

            importe = str(client['Importe'])

            template_name = 'contacto_3'
                
            # Send the message to each client
            response = send_templates(
                telefono,
                template_name,
                diasVencido, 
                importe, 
                factura
            )
            
            acc.append(response)

        return jsonify(acc),200