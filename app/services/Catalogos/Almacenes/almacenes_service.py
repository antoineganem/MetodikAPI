from app.procedures.Catalogos.Almacenes.almacenes_procedures import (
    verAlmacenes, verAlmacenResumen, actAlmacen, verAlmacenID)


def VerAlmacenes():
    return verAlmacenes()


def VerAlmacenResumen(ID):
    return verAlmacenResumen(ID)


def ActAlmacen(data):
    return actAlmacen(data)


def VerAlmacenID(ID):
    return verAlmacenID(ID)
