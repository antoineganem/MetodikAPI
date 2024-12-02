import pyodbc
from flask import jsonify
import os 
from dotenv import load_dotenv
from app.utils.db import get_db_connection, close_db_connection
from app.utils.db_helpers import execute_stored_procedure


#Store procedure to obtain the data to send the message 
def message_data(data):

    sp_name = "spMandarWhatsapp"
    params = [
        data.get("ID"),
        data.get("RenglonID"),
        data.get("HorarioRutaID")]
        
    return execute_stored_procedure(sp_name, params)

def leerMensajesPorWAID(data): 
    
    sp_name = "spLeerMensajesPorWAID"
    params = [
        data.get("wa_id")]

    return execute_stored_procedure(sp_name, params)

def actMensajeWAPP(data):
    
    sp_name = "spActMensajesWAPP"
    params = [
        data.get("wa_id"),
        data.get("nombre"),
        data.get("mensaje"),
        data.get("remitente"),
        data.get("tipoMensaje")]

    return execute_stored_procedure(sp_name, params) 
       
def verUsuariosWAPP():

    sp_name = "spVerUsuariosWAPP"
    params = []

    return execute_stored_procedure(sp_name, params)

def marcarComoLeido(data):

    sp_name = "spMarcarComoLeido"
    print(data)
    params = [ 
        data.get("MensajeID")
    ]

    return execute_stored_procedure(sp_name, params)

def enviarEstadoCuenta1SP():

    sp_name = 'spEnviarEstadoCuenta1'
    params = []

    return execute_stored_procedure(sp_name, params)
        

def enviarEstadoCuenta2SP():

    sp_name = 'spEnviarEstadoCuenta2'
    params = []

    return execute_stored_procedure(sp_name, params)

def enviarEstadoCuenta3SP():

    sp_name = 'spEnviarEstadoCuenta3'
    params = []

    return execute_stored_procedure(sp_name, params)
