from app.procedures.Catalogos.Rutas.rutas_procedures import ver_Rutas, ver_CatRutaID, act_CatRuta, act_DescensoRuta, del_DescensoRuta
def verRutas(data):
    return ver_Rutas(data)


def verCatRutaID(ID):
    return ver_CatRutaID(ID)


def actCatRuta(data):
    return act_CatRuta(data)


def actDescensoRuta(data):
    return act_DescensoRuta(data)


def delDescensoRuta(data):
    return del_DescensoRuta(data)