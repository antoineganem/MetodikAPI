import requests 
import pyodbc
from flask import jsonify
import os 
from dotenv import load_dotenv
from app.utils.db import get_db_connection, close_db_connection

def message_data(data):
    conn = None
    try: 
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spMandarWhatsapp ?,?,?"
        cursor.execute(query,
                       data.get("ID"),
                       data.get("RenglonID"),
                       data.get("HorarioRutaID"))
        
        while cursor.description is None:
            cursor.nextset()
        if cursor.description is None:
            return jsonify({"error": "No data returned from the procedure."}), 500
        
        columns = [column[0] for column in cursor.description]

        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return jsonify(results, 200)
    except pyodbc.Error as e:
        return ({"error": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)

def send_message(data):
    load_dotenv()
    TOKEN  = os.getenv('TOKEN')

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
                                "id": "1471435016875389"
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

        ##return jsonify((response.json()), response.status_code)
    
    except requests.exceptions.RequestException as e:
        print()
        ##return jsonify({"error": str(e)}), 500
    