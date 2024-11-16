from app.procedures.Catalogos.Choferes.choferes_procedures import ver_Choferes, ver_ChoferID, act_ChoferD, eliminar_Chofer


def verChoferes(data):
    return ver_Choferes(data)


def verChoferID(ID):
    return ver_ChoferID(ID)


def actChoferD(data):
    return act_ChoferD(data)


def eliminarChofer(ID):
    return eliminar_Chofer(ID)