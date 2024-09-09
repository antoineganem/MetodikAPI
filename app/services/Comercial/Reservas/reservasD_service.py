from app.procedures.Comercial.Reservas.reservasD_procedures import ver_ReservaID, avanza_reserva, ver_ViajesDispIda, ver_ViajesDispVuelta, act_ReservaD, ver_ReservaDetalle

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
