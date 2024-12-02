from app.procedures.Catalogos.Sucursales.sucursales_procedures import (
    ver_Sucursales,act_Sucursales,ver_SucursalID)


def verSucursales(data):
    return ver_Sucursales(data)

def actSucursal(data):
    return act_Sucursales(data)


def verSucursalID(ID):
    return ver_SucursalID(ID)
