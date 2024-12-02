import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection
from app.utils.db_helpers import execute_stored_procedure


def ver_Rutas(data):
    sp_name = "spVerRutas"
    params = [
        data.get("SucursalID"),
        data.get("EstatusID")
    ]
    return execute_stored_procedure(sp_name, params)


def ver_CatRutaID(ID):
    sp_name = "spVerRutaID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)


def act_CatRuta(data):
    sp_name = "spActRuta"
    params = [
        data.get("ID"),
        data.get("Ruta"),
        data.get("Zona"),
        data.get("Kms"),
        data.get("Costo"),
        data.get("SucursalID"),
        data.get("DestinoDID"),
        data.get("DestinoAID"),
        data.get("Observaciones"),
        data.get("EstatusID"),
        data.get("Tiempo")
    ]
    return execute_stored_procedure(sp_name, params)


def act_DescensoRuta(data):
    sp_name = "spActDescensoRuta"
    params = [
        data.get("RutaID"),
        data.get("DestinoID"),
        data.get("Tiempo"),
        data.get("Kilometros"),
        data.get("PrecioNino"),
        data.get("PrecioAdulto"),
        data.get("PrecioInapam"),
    ]
    return execute_stored_procedure(sp_name, params)


def del_DescensoRuta(data):
    sp_name = "spDeleteDescensoRuta"
    params = [
        data.get("RenglonID"),
        data.get("RutaID")
    ]
    return execute_stored_procedure(sp_name, params)