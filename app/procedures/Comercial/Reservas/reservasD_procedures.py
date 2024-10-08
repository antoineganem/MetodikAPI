import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection
import logging
from app.messagingServices.whatsappAPI import send_message
import json

def ver_ReservaID(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spVerReservaID ?"
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
            

def avanza_reserva(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spAvanzarReserva ?,?,?,?,? ,?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("Movimiento"),  data.get("OrigenID"),  data.get("DestinoID"),  data.get("FechaSalida"),
                        data.get("FechaRegreso"), data.get("Referencia"), data.get("Observaciones"), data.get("Ruta"))
        

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


def ver_ViajesDispIda(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spVerViajesdisponibles ?"
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
            

def ver_ViajesDispVuelta(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spVerViajesdisponiblesVuelta ?"
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
            

def act_ReservaD(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spActReservaD ?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("HorarioRutaID"),  data.get("Cantidad"), data.get("TipoViaje"))
        

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
            
def ver_ReservaDetalle(ID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spVerReservaDetalle ?"
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
            
def eliminar_RenglonReserva(ID, RenglonID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spEliminarRenglonReservaDetalle ?,?"
        cursor.execute(query, ID, RenglonID)
        

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
            
def afectar_reserva(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spAfectarReserva ?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"))
        

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
            
def cancelar_reserva(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spCancelarReserva ?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"))
        

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
            
def ver_AsientosDispoblesRuta(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spVerAsientosDisponiblesRuta ?,?,?"
        cursor.execute(query, data.get("ID"), data.get("HorarioRutaID"), data.get("RenglonID"))
        

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
            
def agregar_AsientosReserva(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spAgregarAsientosReserva ?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("HorarioRutaID"), data.get("RenglonID"), data.get("Asientos"))
        

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
            
def guardar_DatosPersonaReserva(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spGuardarDatosPersonaReserva ?,?,?,?,? ,?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("RenglonID"), data.get("HorarioRutaID"), data.get("Asiento"), data.get("Nombre"),
                    data.get("Email"), data.get("FechaNacimiento"), data.get("Telefono"), data.get("Curp"))
        

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
            
def ver_PersonasReserva(ID, HorarioRutaID, RenglonID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spVerPersonasReserva ?,?,?"
        cursor.execute(query, ID, HorarioRutaID, RenglonID)
        

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
            
def agregar_FormaPagoReserva(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spAgregarFormaPagoReserva ?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"), data.get("FormaPagoID"), data.get("Referencia"))
        

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
            


def cambiar_situacion(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True

        # Ejecutar el procedimiento almacenado principal
        query = "EXEC spCambiarsituacionReserva ?,?"
        cursor.execute(query, data.get("ID"), data.get("Situacion"))

        # Procesar los resultados del primer procedimiento
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        # Obtener los resultados del primer procedimiento
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # Verificar si la situación es "Pagado"
        if data.get("Situacion") == "Pagado":
            try:
                # Ejecutar el procedimiento almacenado para "Pagado"
                query_select = "EXEC spVerBoletosPagadosReserva ?"
                cursor.execute(query_select, data.get("ID"))

                # Verificar si el SELECT devuelve resultados
                while cursor.description is None:
                    cursor.nextset()

                if cursor.description is None:
                    return {"error": "No data returned from spVerBoletosPagadosReserva."}, 500
                
                # Obtener los resultados del SELECT
                columns_select = [column[0] for column in cursor.description]
                select_results = [dict(zip(columns_select, row)) for row in cursor.fetchall()]

                # Iterar sobre los resultados del SELECT y enviar un mensaje por cada uno
                for result in select_results:
                    # Crear el JSON que será enviado, no necesitas json.dumps aquí
                    message_data = {
                        "Telefono": result["Telefono"],
                        "Movimiento": result["Movimiento"],
                        "Fecha": result["Fecha"],
                        "Pasajeros": result["Pasajeros"],
                        "NumeroAsiento": result["NumeroAsiento"],
                        "PrecioTotal": result["PrecioTotal"],  # Asumiendo que ahora es varchar
                        "FechaSalida": result["FechaSalida"],
                        "Ruta": result["Ruta"],
                        "Nombre": result["Nombre"]
                    }

                    # Enviar el mensaje usando send_message directamente con el diccionario
                    send_message(message_data)

            except pyodbc.Error as e:
                # Registrar el error pero no afectar el flujo de retorno
                print(f"Error al ejecutar el procedimiento 'Pagado': {str(e)}")

        # Retornar el resultado del primer procedimiento almacenado
        return results, 200  

    except pyodbc.Error as e:
        if conn:
            conn.rollback()  # Revertir la transacción en caso de error
        return {"error": str(e)}, 500

    finally:
        if conn:
            close_db_connection(conn)


            
def eliminar_reserva(ID, UsuarioID):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spEliminarReserva ?,?"
        cursor.execute(query, ID, UsuarioID)
        

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
            
            
def ver_pdfReserva(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  

        query = "EXEC spPDFReserva ?"
        cursor.execute(query, data.get("ID"))
        

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