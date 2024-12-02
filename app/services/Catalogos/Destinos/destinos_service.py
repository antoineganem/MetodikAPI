from app.procedures.Catalogos.Destinos.destinos_procedures import (
    ver_Destinos,act_Destinos,ver_DestinoID)

def verDestinos(data):
    return ver_Destinos(data)

def actDestinos(data):
    return act_Destinos(data)

def verDestinoID(ID):
    return ver_DestinoID(ID)



