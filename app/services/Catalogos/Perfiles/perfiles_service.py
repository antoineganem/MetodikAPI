from app.procedures.Catalogos.Perfiles.perfiles_procedures import ver_Perfiles, ver_PerfilID, act_Perfil, ver_ModulosAcceso

def verPerfiles(EstatusID, EmpresaID, Buscar):
    return ver_Perfiles(EstatusID, EmpresaID, Buscar)

def verPerfilID(ID):
    return ver_PerfilID(ID)

def actPerfil(data):
    return act_Perfil(data)

def verModulosAcceso(PerfilID, PersonaID):
    return ver_ModulosAcceso(PerfilID, PersonaID)
