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
    ]
    return execute_stored_procedure(sp_name, params)

def ver_RutaDetalle(ID):
    sp_name = "spVerRutaDetalle"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def agregar_paradaRuta(data):
    sp_name = "spAgregarParadaRuta"
    params = [
        data.get("ID"), 
        data.get("UsuarioID")
    ]
    return execute_stored_procedure(sp_name, params)

def act_ParadaRuta(data):
    sp_name = "spActParadaRuta"
    params = [
        data.get("ID"), 
        data.get("RenglonID"), 
        data.get("UsuarioID"), 
        data.get("HoraAbordaje"), 
        data.get("DestinoID"), 
        data.get("Descripcion"), 
        data.get("HoraDescenso")
    ]
    return execute_stored_procedure(sp_name, params)