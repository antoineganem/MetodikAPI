from app.procedures.Catalogos.Pasajeros.pasajeros_procedures import ver_Pasajeros, act_Pasajeros, ver_PasajerosID

def verPasajeros(data):
    return ver_Pasajeros(data)

def actPasajeros(data):
    return act_Pasajeros(data)

def verPasajerosID(ID):
    return ver_PasajerosID(ID)

