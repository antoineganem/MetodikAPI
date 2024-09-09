from app.procedures.Catalogos.Vehiculos.vehiculos_procedures import (
    verVehiculos, verVehiculoResumen, actVehiculo, verVehiculoID)


def VerVehiculos():
    return verVehiculos()


def VerVehiculoResumen(ID):
    return verVehiculoResumen(ID)


def ActVehiculo(data):
    return actVehiculo(data)


def VerVehiculoID(ID):
    return verVehiculoID(ID)
