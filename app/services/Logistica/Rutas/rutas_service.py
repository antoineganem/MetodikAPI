from app.procedures.Logistica.Rutas.rutas_procedures import *

def verRutasModulo():
    return ver_rutas()

def nuevaRuta(data):
    return nueva_Ruta(data)

def verRutaID(ID):
    return ver_RutaID(ID)

def avanzarRuta(data):
    return avanzar_ruta(data)

def verRutaDetalle(ID):
    return ver_RutaDetalle(ID)

def verParadaRutasDisponible(ID):
    return ver_ParadaRutasDisponible(ID)

def agregarParadaRuta(data):
    return agregar_paradaRuta(data)

def ActParadaRuta(data):
    return act_ParadaRuta(data)

def eliminarParadaRuta(ID, RenglonID, UsuarioID):
    return eliminar_paradaRuta(ID, RenglonID, UsuarioID)

def copiarRuta(data):
    return copiar_Ruta(data)

def eliminarRuta(ID, UsuarioID):
    return eliminar_ruta(ID, UsuarioID)

def cancelarRuta(data):
    return cancelar_Ruta(data)

def afectarRuta(data):
    return afectar_Ruta(data)

def cambiarsituacionRuta(data):
    return cambiar_situacionRuta(data)