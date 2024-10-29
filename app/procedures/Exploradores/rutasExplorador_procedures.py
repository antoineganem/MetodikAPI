from app.utils.db_helpers import execute_stored_procedure

def ver_ExploradorRutas(RutaID, Fecha, Hora):
    sp_name = "spVerExploradorRutas"
    params = [ RutaID, Fecha, Hora ]
    return execute_stored_procedure(sp_name, params)
            
def ver_ExploradorRutasID(ID):
    sp_name = "spVerExploradorRutasID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)