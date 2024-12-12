from app.utils.db_helpers import execute_stored_procedure


def ver_Choferes(data):
    sp_name = "spVerChoferes"
    params = [
        data.get("EstatusID"),
        data.get("EmpresaID"),
        data.get("VehiculoID"),
        data.get("SucursalID")
    ]
    return execute_stored_procedure(sp_name, params)


def ver_ChoferID(ID):
    sp_name = "spVerChoferID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)


def act_ChoferD(data):
    sp_name = "spActChofer"
    params = [
        data.get('ID'),
        data.get('EmpresaID'),
        data.get('SucursalID'),
        data.get('EstatusID'),
        data.get('Nombre'),
        data.get('ProveedorID'),
        data.get('Observaciones'),
        data.get('VehiculoID')
    ]
    return execute_stored_procedure(sp_name, params)

def eliminar_Chofer(ID):
    sp_name = "spEliminarChofer"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)