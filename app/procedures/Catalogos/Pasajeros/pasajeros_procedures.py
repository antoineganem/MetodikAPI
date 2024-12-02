from app.utils.db_helpers import execute_stored_procedure

def ver_Pasajeros(data):
    sp_name = "spVerPasajeros"
    params =[
        data.get("PersonaID"),
        data.get("EmpresaID"),
        data.get("EstatusID"),
        data.get("Movimiento"),
        data.get("FechaD"),
        data.get("FechaH"),
        data.get("Situacion"),
        data.get("Usuario")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Pasajeros(data):
    sp_name = "spActPasajero"
    params =[
        data.get("pasajeroid"),
        data.get("nombre"),
        data.get("curp"),
        data.get("email"),
        data.get("telefono"),
        data.get("fechanacimiento"),
        data.get("estatus"),
        data.get("empresaid"),
        data.get("personaid"),
    ]
    return execute_stored_procedure(sp_name, params)

def ver_PasajerosID(ID):
    sp_name = "spVerPasajeroID"
    params = [ID]
    return execute_stored_procedure(sp_name, params)