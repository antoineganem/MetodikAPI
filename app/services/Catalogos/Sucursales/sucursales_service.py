from app.procedures.Catalogos.Sucursales.sucursales_procedures import (
    verSucursales, verSucursalResumen, actSucursal, verSucursalID)


def VerSucursales():
    return verSucursales()


def VerSucursalResumen(ID):
    return verSucursalResumen(ID)


def ActSucursal(data):
    return actSucursal(data)


def VerSucursalID(ID):
    return verSucursalID(ID)
