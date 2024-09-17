import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection
import logging

def verFiltros_Catalogos(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spVerFiltroCatalogo ?,?,?,?"
        cursor.execute(query, data.get("Tipo"), data.get("PersonaID"), data.get("Modulo"), data.get("ModuloID"))
        
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]

        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results, 200  
    except pyodbc.Error as e:
        if conn:
            conn.rollback()  # En caso de error, revertir la transacción
        return {"error": str(e)}, 500  
    finally:
        if conn:
            close_db_connection(conn)
            

def verFiltros_Modulo(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spVerFiltroModulo ?,?,?,?"
        cursor.execute(query, data.get("Tipo"), data.get("PersonaID"), data.get("Modulo"), data.get("ModuloID"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        if conn:
            conn.rollback()  # En caso de error, revertir la transacción
        return {"error": str(e)}, 500  
    finally:
        if conn:
            close_db_connection(conn)



