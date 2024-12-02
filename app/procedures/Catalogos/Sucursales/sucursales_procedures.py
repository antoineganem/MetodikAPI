from app.utils.db_helpers import execute_stored_procedure

def ver_Sucursales(data):
    sp_name = "spVerSucursales"
    params = [
        data.get("PersonaID"),
        data.get("EmpresaID"),
        data.get("EstatusID"),
        data.get("FechaD"),
        data.get("FechaH")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Sucursales(data):
    sp_name = "spActSucursal"
    params = [
        data.get("ID"),
        data.get("Nombre"), data.get("Prefijo"),
        data.get("Direccion"), data.get("DireccionNumero"),
        data.get("DireccionNumeroInt"), data.get("Delegacion"),
        data.get("Colonia"), data.get("Poblacion"),
        data.get("Estado"), data.get("Pais"),
        data.get("CodigoPostal"), data.get("Telefonos"),
        data.get("EstatusID"), data.get("RFC"),
        data.get("EmpresaID"), data.get("ZonaImpuestoID")
    ]
    return execute_stored_procedure(sp_name, params)

def ver_SucursalID(ID):
    sp_name = "spVerSucursalID"
    params = [ID]
    return execute_stored_procedure(sp_name, params)