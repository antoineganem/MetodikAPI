import pyodbc
from flask import jsonify
from app.messagingServices.whatsappAPI import send_message_template, upload_media
from app.utils.config import get_db_session, close_db_session
from app.utils.db_helpers import execute_stored_procedure



def ver_ReservaID(ID):
    sp_name = "spVerReservaID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def avanza_reserva(data):
    sp_name = "spAvanzarReserva"
    params = [
        data.get("ID"), 
        data.get("Movimiento"),
        data.get("OrigenID"),
        data.get("DestinoID"),
        data.get("FechaSalida"),
        data.get("FechaRegreso"),
        data.get("Referencia"),
        data.get("Observaciones"),
        data.get("Ruta"),
        data.get("ReservaID"),
    ]
    return execute_stored_procedure(sp_name, params)

def ver_ViajesDispIda(ID):
    sp_name = "spVerViajesdisponibles"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)            

def ver_ViajesDispVuelta(ID):
    sp_name = "spVerViajesdisponiblesVuelta"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)   

def act_ReservaD(data):
    sp_name = "spActReservaD"
    params = [
        data.get("ID"), 
        data.get("RutaID"),
        data.get("ParadaID"),
        data.get("DestinoID"),
        data.get("Cantidad"),
        data.get("TipoViaje"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def ver_ReservaDetalle(ID):
    sp_name = "spVerReservaDetalle"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params) 
            
def eliminar_RenglonReserva(ID, RenglonID):
    sp_name = "spEliminarRenglonReservaDetalle"
    params = [ ID, RenglonID ]
    return execute_stored_procedure(sp_name, params) 
            
def afectar_reserva(data):
    sp_name = "spAfectarReserva"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def cancelar_reserva(data):
    sp_name = "spCancelarReserva"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def ver_AsientosDispoblesRuta(data):
    sp_name = "spVerAsientosDisponiblesRuta"
    params = [
        data.get("ID"), 
        data.get("RenglonID"),

    ]
    return execute_stored_procedure(sp_name, params)
            
def agregar_AsientosReserva(data):
    sp_name = "spAgregarAsientosReserva"
    params = [
        data.get("ID"), 
        data.get("RenglonID"),
        data.get("Asientos"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def guardar_DatosPersonaReserva(data):
    sp_name = "spGuardarDatosPersonaReserva"
    params = [
        data.get("ID"), 
        data.get("RenglonID"),
        data.get("Asiento"),
        data.get("Nombre"),
        data.get("Email"),
        data.get("FechaNacimiento"),
        data.get("Telefono"),
        data.get("Curp"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def ver_PersonasReserva(ID, RenglonID):
    sp_name = "spVerPersonasReserva"
    params = [ ID, RenglonID]
    return execute_stored_procedure(sp_name, params)

            
def agregar_FormaPagoReserva(data):
    sp_name = "spAgregarFormaPagoReserva"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
        data.get("FormaPagoID"),
        data.get("Referencia"),
    ]
    return execute_stored_procedure(sp_name, params)

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
                
                subirQRreserva(data.get("ID"))
                
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
                        "Nombre": result["Nombre"],
                        "IDCodigoQR": result["IDCodigoQR"]

                    }
                send_message_template(message_data)

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
    sp_name = "spEliminarReserva"
    params = [ ID, UsuarioID]
    return execute_stored_procedure(sp_name, params)            
            
def ver_pdfReserva(data):
    sp_name = "spPDFReserva"
    params = [
        data.get("ID"), 
    ]
    return execute_stored_procedure(sp_name, params)
            
def agregar_equipajeDetalle(data):
    sp_name = "spAgregarEquipajeDetalle"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"), 
        data.get("Articulo"), 
    ]
    return execute_stored_procedure(sp_name, params)
            
def verEquipaje_detalle(ID):
    sp_name = "spVerEquipajeDetalle"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def act_EquipajeDetalle(data):
    sp_name = "spActDetalleEquipaje"
    params = [
        data.get("ID"), 
        data.get("RenglonID"), 
        data.get("UsuarioID"), 
        data.get("Cantidad"), 
        data.get("Peso"), 
        data.get("Precio"), 
    ]
    return execute_stored_procedure(sp_name, params)
            
def eliminar_renglonEquipaje(ID, RenglonID, PersonaID):
    sp_name = "spEliminarDetalleEquipaje"
    params = [ ID, RenglonID, PersonaID ]
    return execute_stored_procedure(sp_name, params)

def subirQRreserva(ID):
    sp_name = "spGenerarQRReserva"
    params = [ID]
    Resp, status_code = execute_stored_procedure(sp_name, params)
    
    if status_code == 200:
        ruta_archivos = []
        for item in Resp:
            ruta_archivo = {"media": item.get("RutaArchivo")}
            ruta_archivos.append(ruta_archivo)
        for ruta in ruta_archivos:
            response = upload_media(ruta)
            try:
                subirQRReserva(ID, item.get("RenglonID"), item.get("NoAsiento"), response)
            except ValueError:
                print(f"Error al obtener JSON de la respuesta: {response.text}")
    else:
        print(f"Error al ejecutar el procedimiento: {Resp}")

def subirQRReserva(ID, RenglonID, NoAsiento, response):
    sp_name = "spActIDQrReserva"
    params = [ ID, RenglonID, NoAsiento, response.get("id")]
    execute_stored_procedure(sp_name, params)
