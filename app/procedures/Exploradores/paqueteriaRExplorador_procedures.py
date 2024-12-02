from app.utils.db_helpers import execute_stored_procedure

def ver_PaqueteriaR(data):
    sp_name = "spVerPaqueteriaRecepcion"
    params = [
        data.get("EmpresaID"),
        data.get("ClienteID"),
        data.get("DestinoID"),
        data.get("Movimiento"),
        data.get("FechaD"),
        data.get("FechaH"),
        data.get("UsuarioID"),
    ]
    return execute_stored_procedure(sp_name, params)