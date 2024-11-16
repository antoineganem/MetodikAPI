from app.utils.db_helpers import execute_stored_procedure

def ver_ExploradorRutas(data):
    sp_name = "spVerExploradorRutas"
    params = [
        data.get("EmpresaID"), 
        data.get("PersonaID"),
        data.get("RutaID"),
        data.get("OrigenID"),
        data.get("DestinoID"),
        data.get("HoraSalida"),
        data.get("FechaDesde"),
        data.get("FechaHasta"),
    ]
    return execute_stored_procedure(sp_name, params)
            
def ver_ExploradorRutasID(ID):
    sp_name = "spVerExploradorRutasID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def ver_ParadasRutasExp(ID):
    sp_name = "spVerParadasRutasExp"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def ver_pasajerosRuta(RutaID, ParadaID):
    sp_name = "spVerPasajerosRutaExp"
    params = [ RutaID, ParadaID ]
    return execute_stored_procedure(sp_name, params)