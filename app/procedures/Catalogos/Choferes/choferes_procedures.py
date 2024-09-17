import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection


def verChoferes():
    conn = None
    try: 
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerChoferes")

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

def verChoferesResumen(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerChoferResumen ?", ID)
        
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
        
def actChoferes(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  # Ensure auto-commit mode for transactions

        print(data)
        # Execute the stored procedure with the provided data
        query = "EXEC spActChofer ?,?,?,?,? ,?,?,?,?,?"
        cursor.execute(query,
            data.get('ChoferID'),
            data.get('EmpresaID'),
            data.get('SucursalID'),
            data.get('EstatusID'),
            data.get('Nombre'),
            data.get('ProveedorID'),
            data.get('Observaciones'),
            data.get('FechaRegistro'),
            data.get('UltimaModificacion'),
            data.get('VehiculoID')
        )

        # Move to the first result set, checking if there is any data
        while cursor.description is None:
            cursor.nextset()

        # If cursor.description is still None, no data was returned
        if cursor.description is None:
            return jsonify({"message": "No data returned from the procedure."}), 404
        
        # Fetch the column names and the results
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # If no results are found, return an appropriate message
        if not results:
            return jsonify({"message": "No records found."}), 404

        return results, 200

    except pyodbc.Error as e:
        # Log the error (this is just an example, adapt to your logging system)
        print(f"Database error: {str(e)}")
        
        # Return error details in the response
        return jsonify({"error": "A database error occurred.", "details": str(e)}), 500

    except Exception as e:
        # Catch other exceptions and return error response
        print(f"General error: {str(e)}")
        
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

    finally:
        # Ensure the connection is properly closed
        if conn:
            close_db_connection(conn)

        
def verChoferID(ID):
    conn = None
    try: 
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC spVerChoferID ?", ID)

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
        