from app.procedures.Catalogos.Destinos.destinos_procedures import (
    verDestinos, verDestinoResumen, actDestino, verDestinoID)


def VerDestinos():
    return verDestinos()


def VerDestinoResumen(ID):
    return verDestinoResumen(ID)


def ActDestino(data):
    return actDestino(data)


def VerDestinoID(ID):
    return verDestinoID(ID)
