import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection

def VerEmpresas():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerEmpresas")
        
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
            
def VerEmpresasResumen(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerEmpresaResumen ?", ID)
        
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



def actEmpresa(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "EXEC spActEmpresa ?,?,?,?,? ,?,?,?,?,? ,?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("EstatusID"), data.get("Empresa"), data.get("Nombre"), data.get("Direccion"),
                       data.get("DireccionNumero"), data.get("DireccionNumeroINT"), data.get("Colonia"), data.get("Poblacion"), data.get("Estado"),
                       data.get("Pais"), data.get("CodigoPostal"), data.get("Telefonos"), data.get("RFC"))
        
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

def verEmpresaID(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "EXEC spVerUsuarioID ?"
        cursor.execute(query, ID)
        
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
