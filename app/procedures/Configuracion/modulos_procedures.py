from app.utils.db_helpers import execute_stored_procedure

def ver_Modulos(data):
    sp_name = "spVerModulos"
    params = [
        data.get("EstatusID"),
        data.get("Tipo"),
        data.get("FechaD"),
        data.get("FechaH")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Modulo(data):
    sp_name = "spActModulo"
    params = [
        data.get("ID"),
        data.get("PersonaID"),
        data.get("Nombre"),
        data.get("Tipo"),
        data.get("Descripcion"),
        data.get("MenuID"),
        data.get("NombreMenu"),
        data.get("Icono"),
        data.get("NombreArchivo")
    ]
    return execute_stored_procedure(sp_name, params)

def ver_ModuloID(ID):
    sp_name = "spVerModuloID"
    params = [ID]
    return execute_stored_procedure(sp_name, params)