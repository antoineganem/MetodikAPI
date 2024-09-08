import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection


def verVehiculos():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spVerVehiculos"
        cursor.execute(query)

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify(
                {"error": "No data returned from the procedure."}
            ), 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(results)
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)


def verVehiculoResumen(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spVerVehiculoResumen ?"
        cursor.execute(query, ID)

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify(
                {"error": "No data returned from the procedure."}
            ), 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(results)
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)


def actVehiculo(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True
        query = "EXEC spActVehiculo ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?"
        cursor.execute(query,
                       data.get("ID"), data.get("Vehiculo"),
                       data.get("Descripcion"), data.get("Placas"),
                       data.get("Volumen"), data.get("Peso"),
                       data.get("Agente"), data.get("RutaID"),
                       data.get("EstatusID"), data.get("Proveedor"),
                       data.get("Condicion"), data.get("Concepto"),
                       data.get("serie"), data.get("Marca"),
                       data.get("NoEco"), data.get("Ano"),
                       data.get("CapacidadPeso"), data.get("CapacidadVol"),
                       data.get("EmpresaID"), data.get("TipoVehiculo")
                       )

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify(
                {"error": "No data returned from the procedure."}
            ), 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200
    except pyodbc.Error as e:
        return {"error": str(e)}, 500
    finally:
        if conn:
            close_db_connection(conn)


def verVehiculoID(ID):
    conn = get_db_connection()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spVerVehiculoID ?"
        cursor.execute(query, ID)

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify(
                {"error": "No data returned from the procedure."}
            ), 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(results)
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)
