from app.procedures.login.login_procedures import login

def login_usuario(Correo, Contrasena, Empresa):
    """
    Llama al procedimiento almacenado de login y devuelve los resultados.
    """
    return login(Correo, Contrasena, Empresa)
