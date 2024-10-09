import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection
import logging
from app.messagingServices.whatsappAPI import send_message
import json
from app.utils.config import get_db_session, close_db_session


def ver_ReservaID(ID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spVerReservaID ?"
        cursor.execute(query, ID)
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        session.commit()
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            

def avanza_reserva(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spAvanzarReserva ?,?,?,?,? ,?,?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("Movimiento"),  data.get("OrigenID"),  data.get("DestinoID"),  data.get("FechaSalida"),
                        data.get("FechaRegreso"), data.get("Referencia"), data.get("Observaciones"), data.get("Ruta"), data.get("ReservaID"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        session.commit()

        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)


def ver_ViajesDispIda(ID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
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
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            

def ver_ViajesDispVuelta(ID):
    session = get_db_session() 
    try:
        conn = session.connection().connection 
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
        session.rollback()  
        return {"error": str(e)}, 500

    finally:
        close_db_session(session)

            

def act_ReservaD(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spActReservaD ?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("HorarioRutaID"),  data.get("Cantidad"), data.get("TipoViaje"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        session.commit()

        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def ver_ReservaDetalle(ID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
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
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def eliminar_RenglonReserva(ID, RenglonID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spEliminarRenglonReservaDetalle ?,?"
        cursor.execute(query, ID, RenglonID)
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        session.commit()

        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def afectar_reserva(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spAfectarReserva ?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        session.commit()

        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def cancelar_reserva(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spCancelarReserva ?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        session.commit()

        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def ver_AsientosDispoblesRuta(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
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
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def agregar_AsientosReserva(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spAgregarAsientosReserva ?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("HorarioRutaID"), data.get("RenglonID"), data.get("Asientos"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        session.commit()

        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def guardar_DatosPersonaReserva(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spGuardarDatosPersonaReserva ?,?,?,?,? ,?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("RenglonID"), data.get("HorarioRutaID"), data.get("Asiento"), data.get("Nombre"),
                    data.get("Email"), data.get("FechaNacimiento"), data.get("Telefono"), data.get("Curp"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        session.commit()

        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def ver_PersonasReserva(ID, HorarioRutaID, RenglonID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
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
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def agregar_FormaPagoReserva(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spAgregarFormaPagoReserva ?,?,?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"), data.get("FormaPagoID"), data.get("Referencia"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        session.commit()

        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            


def cambiar_situacion(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spCambiarsituacionReserva ?,?"
        cursor.execute(query, data.get("ID"), data.get("Situacion"))

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        session.commit()

        if data.get("Situacion") == "Pagado":
            try:
                query_select = "EXEC spVerBoletosPagadosReserva ?"
                cursor.execute(query_select, data.get("ID"))

                while cursor.description is None:
                    cursor.nextset()

                if cursor.description is None:
                    return {"error": "No data returned from spVerBoletosPagadosReserva."}, 500
                
                columns_select = [column[0] for column in cursor.description]
                select_results = [dict(zip(columns_select, row)) for row in cursor.fetchall()]

                for result in select_results:
                    message_data = {
                        "Telefono": result["Telefono"],
                        "Movimiento": result["Movimiento"],
                        "Fecha": result["Fecha"],
                        "Pasajeros": result["Pasajeros"],
                        "NumeroAsiento": result["NumeroAsiento"],
                        "PrecioTotal": result["PrecioTotal"], 
                        "FechaSalida": result["FechaSalida"],
                        "Ruta": result["Ruta"],
                        "Nombre": result["Nombre"]
                    }
                    send_message(message_data)

            except pyodbc.Error as e:
                session.rollback() 
                return {"error": str(e)}, 500
            
        return results, 200  

    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)


            
def eliminar_reserva(ID, UsuarioID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spEliminarReserva ?,?"
        cursor.execute(query, ID, UsuarioID)
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        session.commit()

        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
            
def ver_pdfReserva(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
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
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
            
def agregar_equipajeDetalle(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spAgregarEquipajeDetalle ?,?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"), data.get("Articulo"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        session.commit()
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def verEquipaje_detalle(ID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True 

        query = "EXEC spVerEquipajeDetalle ?"
        cursor.execute(query, ID)

        # Asegurar que se obtengan los resultados correctos
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        # Obtener las columnas y los resultados
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results, 200
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)


def act_EquipajeDetalle(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spActDetalleEquipaje ?,?,?,?,? ,?"
        cursor.execute(query, data.get("ID"), data.get("RenglonID"), data.get("UsuarioID"), data.get("Cantidad"), data.get("Peso")
                       , data.get("Precio"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        session.commit()
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def eliminar_renglonEquipaje(ID, RenglonID, PersonaID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  

        query = "EXEC spEliminarDetalleEquipaje ?,?,?"
        cursor.execute(query, ID, RenglonID, PersonaID)
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        session.commit()
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)