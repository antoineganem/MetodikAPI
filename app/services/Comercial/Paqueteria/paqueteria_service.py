from app.procedures.Comercial.Paqueteria.paqueteria_procedures import *

def verPaqueteria(data):
    return ver_paqueteria(data)

def nuevaPaqueteria(data):
    return nueva_paqueteria(data)

def verPaqueteriaID(ID):
    return ver_paqueteriaID(ID)

def verArtDispPaqueteria(EmpresaID):
    return ver_ArtDispPaqueteria(EmpresaID)

def avanzarPaqueteria(data):
    return avanza_paqueteria(data)

def agregarPaqueteriaDetalle(data):
    return agregar_paqueteriaDetalle(data)

def verPaqueteriaDetalle(ID):
    return verPaqueteria_detalle(ID)

def actPaqueteriaDetalle(ID):
    return act_paqueteriaDetalle(ID)

def eliminarRenglonPaqueteria(ID, RenglonID, PersonaID):
    return eliminar_renglonPaqueteria(ID, RenglonID, PersonaID)

def cambiarSituacionPaqueteria(data):
    return cambiar_situacion(data)

def afectarPaqueteria(data):
    return afectar_paqueteria(data)

def eliminarPaqueteria(data):
    return eliminar_paqueteria(data)

def cancelarPaqueteria(data):
    return cancelar_paqueteria(data)