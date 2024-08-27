from app.procedures.Catalogos.Usuarios.usuarios_procedures import VerUsuarios, VerUsuariosResumen

def verUsuarios(EmpresaID, EstatusID):
    return VerUsuarios(EmpresaID, EstatusID)

def verUsuariosResumen(ID):
    return VerUsuariosResumen(ID)