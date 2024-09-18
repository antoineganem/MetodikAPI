import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection


def verAlmacenes():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spVerAlmacenes"
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


def verAlmacenResumen(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spVerAlmacenResumen ?"
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


def actAlmacen(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True
        query = "EXEC spActAlmacen ?,?,?,?,?,?,?"
        cursor.execute(query,
                       data.get("ID"), 
                       data.get("Nombre"), data.get("GrupoID"),
                       data.get("TipoID"), data.get("SucursalID"),
                       data.get("EstatusID"), data.get("EmpresaID"),
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


def verAlmacenID(ID):
    conn = get_db_connection()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "EXEC spVerAlmacenID ?"
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
