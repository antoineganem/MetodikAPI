import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection


def verSucursales():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spVerSucursales"
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


def verSucursalResumen(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spVerSucursalResumen ?"
        cursor.execute(query, ID)

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return jsonify(
                {"error": "No data returned from the procedure."}
            ), 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(results[0])
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            close_db_connection(conn)


def actSucursal(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True
        query = "EXEC spActSucursal ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?"
        cursor.execute(query,
                       data.get("ID"),
                       data.get("Nombre"), data.get("Prefijo"),
                       data.get("Direccion"), data.get("DireccionNumero"),
                       data.get("DireccionNumeroInt"), data.get("Delegacion"),
                       data.get("Colonia"), data.get("Poblacion"),
                       data.get("Estado"), data.get("Pais"),
                       data.get("CodigoPostal"), data.get("Telefonos"),
                       data.get("EstatusID"), data.get("RFC"),
                       data.get("EmpresaID"), data.get("ZonaImpuestoID")
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


def verSucursalID(ID):
    conn = get_db_connection()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spVerSucursalID ?"
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
