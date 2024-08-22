# Ejemplo básico de un validador
def validar_correo(correo):
    if "@" not in correo:
        return False
    return True
