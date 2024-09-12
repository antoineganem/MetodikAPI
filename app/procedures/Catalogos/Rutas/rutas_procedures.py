import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection

def verRutas():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Execute the stored procedure
        cursor.execute("EXEC spVerRutas")
        
        # Advance through multiple result sets (if necessary)
        while cursor.description is None:
            cursor.nextset()

        # Check if we have valid result set
        if cursor.description is None:
            return jsonify({"error": "No data returned from the procedure."}), 500

        # Fetch column names
        columns = [column[0] for column in cursor.description]

        # Fetch all rows
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # Return results as JSON
        return jsonify(results), 200

    except pyodbc.Error as e:
        # Log the error and return a 500 response
        return jsonify({"error": str(e)}), 500

    finally:
        # Ensure the connection is closed
        if conn:
            close_db_connection(conn)

def verRutasResumen(ID):
    conn = None 
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerRutasResumen ?", ID)
        
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
        
def actRutas(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  # Asegúrate de que las transacciones se confirmen automáticamente
        
        query = "EXEC spActRuta ?,?,?,?,? ,?,?,?,?,? ,?,?,? "
        cursor.execute(query, data.get('ID'),data.get('Ruta'),data.get('Zona'),data.get('Kms'),data.get('Costo'),data.get('SucursalD'),data.get('DestinoDID'),
                data.get('DestinoAID'),data.get('Observaciones'),data.get('EstatusID'),data.get('Tiempo'),data.get('UltimoCambio'), data.get('FechaRegistro'))
        
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify({"error": "No data returned from the procedure."}), 500
        
        columns = [column[0] for column in cursor.description]
        
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()
        
        return results, 200
    
    except pyodbc.Error as e:

        return jsonify({"error": str(e)}), 500
    
    finally:
        if conn:
            close_db_connection(conn)
