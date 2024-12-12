from app.utils.db_helpers import execute_stored_procedure

def ver_rutas():
    sp_name = "spVerRutasModulo"
    params = []
    return execute_stored_procedure(sp_name, params)

def nueva_Ruta(data):
    sp_name = "spNvaRuta"
    params = [
        data.get("PersonaID"), 
        data.get("EmpresaID")
    ]
    return execute_stored_procedure(sp_name, params)

def ver_RutaID(ID):
    sp_name = "spVerRutasID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def avanzar_ruta(data):
    sp_name = "spAvanzarRuta"
    params = [
        data.get("ID"), 
        data.get("Movimiento"), 
        data.get("RutaID"), 
        data.get("FechaInicio"), 
        data.get("HoraSalida"), 
        data.get("Referencia"), 
        data.get("VehiculoID"), 
        data.get("EquipoID"), 
        data.get("Observaciones"),
        data.get("GenerarAutomatico"),

    ] 
    return execute_stored_procedure(sp_name, params)

def ver_RutaDetalle(ID):
    sp_name = "spVerRutaDetalle"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def ver_ParadaRutasDisponible(ID):
    sp_name = "spVerParadasRuta"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def agregar_paradaRuta(data):
    sp_name = "spAgregarParadaRuta"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
        data.get("DestinoID"),
    ]
    return execute_stored_procedure(sp_name, params)

def act_ParadaRuta(data):
    sp_name = "spActParadaRuta"
    params = [
        data.get("ID"), 
        data.get("RenglonID"), 
        data.get("UsuarioID"), 
        data.get("HoraAbordaje"), 
        data.get("Descripcion"), 
        data.get("HoraDescenso"), 
    ]
    return execute_stored_procedure(sp_name, params)

def eliminar_paradaRuta(ID, RenglonID, UsuarioID):
    sp_name = "spEliminarParadaRuta"
    params = [ID, RenglonID, UsuarioID]
    return execute_stored_procedure(sp_name, params)

def copiar_Ruta(data):
    sp_name = "spCopiarRuta"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
    ]
    return execute_stored_procedure(sp_name, params)

def eliminar_ruta(ID, UsuarioID):
    sp_name = "spEliminarRuta"
    params = [ID, UsuarioID]
    return execute_stored_procedure(sp_name, params)

def cancelar_Ruta(data):
    sp_name = "spCancelarRuta"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
    ]
    return execute_stored_procedure(sp_name, params)

def afectar_Ruta(data):
    sp_name = "spAfectarRuta"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
    ]
    return execute_stored_procedure(sp_name, params)

def cambiar_situacionRuta(data):
    sp_name = "spCambiarSituacionRuta"
    params = [
        data.get("ID"), 
        data.get("UsuarioID"),
        data.get("Situacion"),
    ]
    return execute_stored_procedure(sp_name, params)