from app.utils.db_helpers import execute_stored_procedure

def ver_Vehiculos(data):
    sp_name = "spVerVehiculos"
    params = [
        data.get("PersonaID"),
        data.get("EmpresaID"),
        data.get("EstatusID"), 
        data.get("FechaD"),
        data.get("FechaH"),
        data.get("UsuarioID")
    ]
    return execute_stored_procedure(sp_name, params)

def act_Vehiculos(data):
    sp_name = "spActVehiculo"
    params = [ 
        data.get("ID"),
        data.get("Vehiculo"),
        data.get("Descripcion"),
        data.get("Placas"),
        data.get("Peso"),
        data.get("EstatusID"),
        data.get("serie"),
        data.get("Marca"),
        data.get("NoEco"),
        data.get("CapacidadPeso"),
        data.get("EmpresaID"),
        data.get("PersonaID"),
        data.get("TipoVehiculo"),
    ]
    return execute_stored_procedure(sp_name, params)

def ver_VehiculosID(ID):
    sp_name = "spVerVehiculoID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)