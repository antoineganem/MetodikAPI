from app.procedures.Catalogos.Rutas.rutas_procedures import verRutas, verRutasResumen, actRutas, verHorarios, actHorarioRuta, verRutasHorarios, eliminarRutaHorario

def VerRutas():
    return verRutas()

def VerRutasResumen(ID):
    return verRutasResumen(ID)

def ActRuta(data):
    return actRutas(data)

def VerHorarios():
    return verHorarios()

def ActHorarioRuta(data):
    return actHorarioRuta(data)

def VerRutasHorarios(ID):
    return verRutasHorarios(ID)

def EliminarRutaHorario(ID):
    return eliminarRutaHorario(ID)

