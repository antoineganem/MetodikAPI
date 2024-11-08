from app.utils.db_helpers import execute_stored_procedure

def ver_Perfiles(EstatusID, EmpresaID, Buscar):
    sp_name = "spVerPerfiles"
    params = [ EstatusID, EmpresaID, Buscar ]
    return execute_stored_procedure(sp_name, params)
            
def ver_PerfilID(ID):
    sp_name = "spVerPerfilID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def act_Perfil(data):
    sp_name = "spActPerfiles"
    params = [
        data.get("ID"), 
        data.get("Nombre"), 
        data.get("Notas"), 
        data.get("EstatusID"), 
        data.get("EmpresaID"),
    ]
    return execute_stored_procedure(sp_name, params)

def ver_ModulosAcceso(PerfilID, PersonaID):
    sp_name = "spVerModulosAcceso"
    params = [ PerfilID, PersonaID ]
    return execute_stored_procedure(sp_name, params)