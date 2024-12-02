from app.procedures.Logistica.PreciosRuta.preciosruta_procedure import *

def verPreciosRutas(EmpresaID, OrigenID, DestinoID):
    return ver_preciosRutas(EmpresaID, OrigenID, DestinoID)

def actPreciosRuta( data ):
    return act_preciosRuta( data )

def afectarCambioPreciosRuta( data ):
    return afectar_CambioPreciosRuta( data )