from app.procedures.Comercial.Reservas.reservasD_procedures import *

def verReservaID(ID):
    return ver_ReservaID(ID)

def avanzaReserva(data):
    return avanza_reserva(data)

def verViajesDisponibles(ID):
    return ver_ViajesDispIda(ID)

def verViajesDisponiblesVuelta(ID):
    return ver_ViajesDispVuelta(ID)

def ActReservaD(data):
    return act_ReservaD(data)

def VerReservaDetalle(ID):
    return ver_ReservaDetalle(ID)

def VerReservaDetalle(ID):
    return ver_ReservaDetalle(ID)

def EliminarRenglonReserva(ID, RenglonID):
    return eliminar_RenglonReserva(ID, RenglonID)

def afectarReserva(data):
    return afectar_reserva(data)

def cancelarReserva(data):
    return cancelar_reserva(data)

def verAsientosDispoblesRuta(data):
    return ver_AsientosDispoblesRuta(data)


def agregarAsientosReserva(data):
    return agregar_AsientosReserva(data)

def guardarDatosPersonasReserva(data):
    return guardar_DatosPersonaReserva(data)

def verPersonasReserva(ID, HorarioRutaID, RenglonID):
    return ver_PersonasReserva(ID, HorarioRutaID, RenglonID)

def agregarFormaPagoReserva(data):
    return agregar_FormaPagoReserva(data)

def cambiarSituacion(data):
    return cambiar_situacion(data)