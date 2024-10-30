from app.utils.db_helpers import execute_stored_procedure

def ver_Reservas(data):
    sp_name = "spVerReservas"
    params = [
        data.get("PersonaID"), 
        data.get("EmpresaID"),
        data.get("EstatusID"),
        data.get("Movimiento"),
        data.get("FechaD"),
        data.get("FechaH"),
        data.get("Situacion"),
        data.get("Usuario"),

    ]
    return execute_stored_procedure(sp_name, params)

def nva_reserva(data):
    sp_name = "spNvaReserva"
    params = [
        data.get("PersonaID"), 
        data.get("EmpresaID"),
    ]
    return execute_stored_procedure(sp_name, params)





