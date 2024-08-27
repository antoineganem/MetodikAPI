from app.procedures.Catalogos.Empresas.empresas_procedures import VerEmpresas, VerEmpresasResumen, actEmpresa, verEmpresaID

def verEmpresas():
    return VerEmpresas()


def verEmpresasResumen(ID):
    return VerEmpresasResumen(ID)

def ActEmpresa(data):
    return actEmpresa(data)


def VerEmpresaID(ID):
    return verEmpresaID(ID)
    