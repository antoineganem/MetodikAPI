from app.procedures.Catalogos.Choferes.choferes_procedures import verChoferes, verChoferesResumen, actChoferes, verChoferID

def VerChoferes_SR():
    return verChoferes()

def VerChoferesResumen_SR(ID):
    return verChoferesResumen(ID)

def ActChoferes_SR(data):
    return actChoferes(data)

def VerChoferID_SR(ID):
    return verChoferID(ID)