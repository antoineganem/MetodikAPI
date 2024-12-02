import pyodbc
from flask import jsonify
from app.messagingServices.whatsappAPI import send_message
from app.utils.config import get_db_session, close_db_session
from app.utils.db_helpers import execute_stored_procedure

def ver_EquipoID(ID):
    sp_name = "spVerEquipoID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def ver_Equipos(data):
    sp_name = "spVerEquipos"
    params = [
        data.get("EmpresaID"),
        data.get("EstatusID"),
        data.get("FechaD"),
        data.get("FechaH")
    ]
    return execute_stored_procedure(sp_name, params)

def act_EquipoD(data):
    sp_name = "spActEquipo"
    params = [
        data.get("ID"),
        data.get("EmpresaID"),
        data.get("EstatusID"),
        data.get("Nombre"),
        data.get("Descripcion"),
        data.get("Integrantes")
    ]
    return execute_stored_procedure(sp_name, params)

def eliminar_Equipo(ID):
    sp_name = "spEliminarEquipo"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)