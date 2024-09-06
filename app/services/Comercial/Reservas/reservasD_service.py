from app.procedures.Comercial.Reservas.reservasD_procedures import ver_ReservaID, avanza_reserva, ver_ViajesDispIda, ver_ViajesDispVuelta

def verReservaID(ID):
    return ver_ReservaID(ID)

def avanzaReserva(data):
    return avanza_reserva(data)

def verViajesDisponibles(ID):
    return ver_ViajesDispIda(ID)

def verViajesDisponiblesVuelta(ID):
    return ver_ViajesDispVuelta(ID)
