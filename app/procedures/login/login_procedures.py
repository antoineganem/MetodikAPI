import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection

def login(param1, param2, param3):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Pasa los parámetros al procedimiento almacenado
        cursor.execute("EXEC spUsuarioAcceso ?, ?, ?", param1, param2, param3)

        # Obtén las columnas de la consulta
        columns = [column[0] for column in cursor.description]
        # Convierta los resultados a una lista de diccionarios
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # Retorna los resultados como JSON
        return jsonify(results)
    
    except pyodbc.Error as e:
        # Retorna el error como JSON
        return jsonify({"error": str(e)}), 500
    
    finally:
        if conn:
            close_db_connection(conn)
