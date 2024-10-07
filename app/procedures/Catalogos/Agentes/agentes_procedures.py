import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection
import logging

def VerAgentes(EmpresaID, EstatusID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerAgentes ?, ?", EmpresaID, EstatusID)
        
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
 
def VerAgentesResumen(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerAgenteResumen ?", ID)
        
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

def actAgente(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  # Asegúrate de que las transacciones se confirmen automáticamente

        query = "EXEC spActAgenteERP ?,?,?,?,? ,?,?,?,?,? ,?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("EstatusID"), data.get("EmpresaID"),data.get("Nombre"), data.get("TipoID"),
                       data.get("TipoComisionID"), data.get("PorcentajeComision"), data.get("Cuota"), data.get("PorcentajeCuota"), 
                       data.get("SucursalID"), data.get("Telefono"), data.get("Puesto"), data.get("Notas"), data.get("Correo"));

        while cursor.description is None:
            logging.info("Checking for more result sets...")
            cursor.nextset()

        if cursor.description is None:
            logging.error("No data returned from the procedure.")
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        logging.info("Returning results...")
        return results, 200  
    except pyodbc.Error as e:
        logging.error(f"Database error: {str(e)}")
        if conn:
            conn.rollback()  # En caso de error, revertir la transacción
        return {"error": str(e)}, 500  
    finally:
        if conn:
            logging.info("Closing the database connection...")
            close_db_connection(conn)


def verAgenteID(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "EXEC spVerAgenteID ?"
        cursor.execute(query, ID)
        
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify({"error": "No data returned from the procedure."}), 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)
