import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection

def VerUsuarios(EmpresaID, EstatusID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerUsuarios ?, ?", EmpresaID, EstatusID)
        
        # Si hay múltiples resultados, avanzar al siguiente conjunto
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify({"error": "No data returned from the procedure."}), 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(results)
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)
            
def VerUsuariosResumen(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerUsuarioResumen ?", ID)
        
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify({"error": "No data returned from the procedure."}), 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(results)
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)

