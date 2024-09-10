from app.procedures.Configuracion.modulos_procedures import ver_Modulos, ver_ModuloID, eliminar_Modulo, act_modulo

def verModulos():
    return ver_Modulos()

def actModulo(data):
    return act_modulo(data)

def eliminarModulo(ID):
    return eliminar_Modulo(ID)

def verModuloID(ID):
    return ver_ModuloID(ID)

