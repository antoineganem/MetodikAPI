from app.procedures.Catalogos.Equipos.equipos_procedures import ver_EquipoID, ver_Equipos, act_EquipoD, eliminar_Equipo

def verEquipos(data):
    return ver_Equipos(data)

def verEquipoID(ID):
    return ver_EquipoID(ID)

def actEquipoD(data):
    return act_EquipoD(data)

def eliminarEquipo(ID):
    return eliminar_Equipo(ID)