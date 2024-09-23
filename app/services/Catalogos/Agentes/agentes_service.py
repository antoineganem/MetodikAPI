from app.procedures.Catalogos.Agentes.agentes_procedures import VerAgentes, VerAgentesResumen, actAgente, verAgenteID

def verAgentes(EmpresaID, EstatusID):
    return VerAgentes(EmpresaID, EstatusID)

def verAgentesResumen(ID):
    return VerAgentesResumen(ID)

def ActualizarAgentes(data):
    return actAgente(data)

def VerAgenteID(ID):
    return verAgenteID(ID)
