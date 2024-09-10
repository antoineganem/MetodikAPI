import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection
import logging

def ver_Perfiles(EstatusID, EmpresaID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spVerPerfiles ?,?"
        cursor.execute(query, EstatusID, EmpresaID)
        

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
            
def ver_PerfilID(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spVerPerfilID ?"
        cursor.execute(query, ID)
        

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
            

def act_Perfil(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  # Asegúrate de que las transacciones se confirmen automáticamente


        query = "EXEC spActPerfiles ?,?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("Nombre"), data.get("Notas"), data.get("EstatusID"), data.get("EmpresaID"))

        
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        return {"error": str(e)}, 500  
    finally:
        if conn:
            close_db_connection(conn)
