from app.procedures.Catalogos.Usuarios.usuarios_procedures import VerUsuarios, VerUsuariosResumen, actUsuario, verUsuarioID

def verUsuarios(EmpresaID, EstatusID):
    return VerUsuarios(EmpresaID, EstatusID)

def verUsuariosResumen(ID):
    return VerUsuariosResumen(ID)

def ActualizarUsuarios(data):
    return actUsuario(data)

def VerUsuarioID(ID):
    return verUsuarioID(ID)