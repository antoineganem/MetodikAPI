from app.utils.db_helpers import execute_stored_procedure



def ver_paqueteria(data):
    sp_name = "spVerPaqueteria"
    params = [
        data.get("EmpresaID"), 
        data.get("EstatusID"),
        data.get("Movimiento"),
        data.get("FechaD"),
        data.get("FechaH"),
        data.get("Situacion"),
        data.get("Usuario"),
    ]
    return execute_stored_procedure(sp_name, params)

def nueva_paqueteria(data):
    sp_name = "spNvaPaqueteria"
    params = [
        data.get("PersonaID"), 
        data.get("EmpresaID"),
    ]
    return execute_stored_procedure(sp_name, params)

def ver_paqueteriaID(ID):
    sp_name = "spVerPaqueteriaID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)
            
def ver_ArtDispPaqueteria(EmpresaID):
    sp_name = "spVerArticulosPaqueteria"
    params = [ EmpresaID ]
    return execute_stored_procedure(sp_name, params)
            
def avanza_paqueteria(data):
    sp_name = "spAvanzarPaqueteria"
    params = [
        data.get("ID"), 
        data.get("Movimiento"),
        data.get("ClienteID"),
        data.get("TerminalOrigenID"),
        data.get("TerminalDestinoID"),
        data.get("FechaEnvio"),
        data.get("FormaPagoID"),
        data.get("ReferenciaPago"),
        data.get("TelefonoDest"),
        data.get("NombreDest"),
        data.get("PersonaID"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def agregar_paqueteriaDetalle(data):
    sp_name = "spAgregarPaqueteriaDetalle"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
        data.get("Articulo"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def verPaqueteria_detalle(ID):
    sp_name = "spVerPaqueteriaDetalle"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def act_paqueteriaDetalle(data):
    sp_name = "spActDetallePaqueteria"
    params = [
        data.get("ID"), 
        data.get("RenglonID"),
        data.get("UsuarioID"),
        data.get("Cantidad"),
        data.get("Peso"),
        data.get("Precio"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def eliminar_renglonPaqueteria(ID, RenglonID, PersonaID):
    sp_name = "spEliminarDetallePaqueteria"
    params = [ID, RenglonID, PersonaID]
    return execute_stored_procedure(sp_name, params)
            
def cambiar_situacion(data):
    sp_name = "spCambiarSituacionPaqueteria"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
        data.get("Situacion"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def afectar_paqueteria(data):
    sp_name = "spAfectarPaqueteria"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def eliminar_paqueteria(data):
    sp_name = "spEliminarPaqueteria"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def cancelar_paqueteria(data):
    sp_name = "spCancelarPaqueteria"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
    ]
    return execute_stored_procedure(sp_name, params)
