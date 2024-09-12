from app.procedures.Catalogos.Rutas.rutas_procedures import verRutas, verRutasResumen, actRutas

def VerRutas():
    return verRutas()

def VerRutasResumen(ID):
    return verRutasResumen(ID)

def ActRuta(data):
    return actRutas(data)
