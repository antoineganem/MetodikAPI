from app.utils.db_helpers import execute_stored_procedure

def ver_Destinos(data):
    sp_name = "spVerDestinos"
    params = [
        data.get("PersonaID"),
        data.get("EmpresaID"),
        data.get("EstatusID"), 
        data.get("FechaD"),
        data.get("FechaH")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Destinos(data):
    sp_name = "spActDestino"
    params = [
        data.get("ID"),
        data.get("Nombre"),
        data.get("Ciudad"),
        data.get("Pais"),
        data.get("CodigoPostal"),
        data.get("Descripcion"),
        data.get("EstatusID"),
        data.get("EmpresaID"),
        data.get("PersonaID")
    ]
    return execute_stored_procedure(sp_name, params)

def ver_DestinoID(ID):
    sp_name = "spVerDestinoID"
    params = [ID]
    return execute_stored_procedure(sp_name,params)
