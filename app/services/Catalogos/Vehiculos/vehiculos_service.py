from app.procedures.Catalogos.Vehiculos.vehiculos_procedures import ver_Vehiculos,act_Vehiculos,ver_VehiculosID

def verVehiculos(data):
    return ver_Vehiculos(data)

def actVehiculo(data):
    return act_Vehiculos(data)

def verVehiculoID(ID):
    return ver_VehiculosID(ID)