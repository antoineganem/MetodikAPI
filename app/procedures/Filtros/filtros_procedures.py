from app.utils.db_helpers import execute_stored_procedure

def verFiltros_Catalogos(data):
    sp_name = "spVerFiltroCatalogo"
    params = [
        data.get("Tipo"), 
        data.get("PersonaID"),
        data.get("Modulo"),
        data.get("ModuloID"),
    ]
    return execute_stored_procedure(sp_name, params)

def verFiltros_Modulo(data):
    sp_name = "spVerFiltroModulo"
    params = [
        data.get("Tipo"), 
        data.get("PersonaID"),
        data.get("Modulo"),
        data.get("ModuloID"),
    ]
    return execute_stored_procedure(sp_name, params)





