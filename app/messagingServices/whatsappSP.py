import pyodbc
from flask import jsonify
import os 
from dotenv import load_dotenv
from app.utils.db import get_db_connection, close_db_connection

#Store procedure to obtain the data to send the message 
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

def leerMensajesPorWAID(data):
    conn = None
    try: 
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spLeerMensajesPorWAID ?"
        cursor.execute(query,
                       data.get("wa_id"))
        
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

def actMensajeWAPP(data):
    conn = None 
    try: 
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spActMensajesWAPP ?,?,?,?,?"
        print(data.get("wa_id"),data.get("nombre"),data.get("mensaje"),data.get("remitente"),data.get("tipoMensaje"))
        cursor.execute(query,
                       data.get("wa_id"),
                       data.get("nombre"),
                       data.get("mensaje"),
                       data.get("remitente"),
                       data.get("tipoMensaje"))

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify({"error": "No data returned from the procedure."}), 500
        
        columns = [column[0] for column in cursor.description]

        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return (results),200
    
    except pyodbc.Error as e:
        print(e)
        return ({"error": str(e)}), 500
    
    finally:
        if conn:
            close_db_connection(conn)
