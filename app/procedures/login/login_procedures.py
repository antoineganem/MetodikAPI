import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection

def login(Correo, Contrasena, Empresa):
    conn = None
    print("entro store")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Pasa los parámetros al procedimiento almacenado
        cursor.execute("EXEC spUsuarioAcceso ?, ?, ?", Correo, Contrasena, Empresa)

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
