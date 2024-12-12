import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection
import logging
from app.utils.db_helpers import execute_stored_procedure

#get all personas from the database
def verPersonas(data):

    sp = 'spLeerPersonas'
    params = [
         data.get('SucursalID'),
         data.get('EstatusID'),
         data.get('EmpresaID'),
    ]

    return execute_stored_procedure(sp, params)

def verPersonasPorID(id):
    
        sp = 'spLeerPersonasDetalle'
        params = [id]
    
        return execute_stored_procedure(sp, params)

#store procedure to insert or update a user
def actPersonas(data):

    print(data)
    sp ='spActPersonas'

    """
    @PersonaID = 10,
    @EstatusID = 1,
    @Usuario = 'prueba',
    @Correo = 'prueba@example.com',
    @Contra = 'password123',
    @Contra2 = 'password123',
    @MultiEmpresa = 1,
    @EmpresaID = 1,
    @SucursalID = 1,
    @AlmacenID = NULL,
    @PerfilID = 2,
    @Nombre = 'John',
    @ApellidoPaterno = 'doe',
    @ApellidoMaterno = 'smith',
    @Imagen = 'path/to/image.jpg',
    @ImagenFondo = 'path/to/background.jpg',
    @Notas = 'New user',
    @Empresas = '101,102,103';

    """
    params = [
        data.get('PersonaID'),
        data.get('EstatusID'),
        data.get('Usuario'),
        data.get('Correo'),
        data.get('Contra'),
        data.get('Contra2'),
        data.get('MultiEmpresa'),
        data.get('EmpresaID'),
        data.get('SucursalID'),
        data.get('AlmacenID'),
        data.get('PerfilID'),
        data.get('Nombre'),
        data.get('ApellidoPaterno'),
        data.get('ApellidoMaterno'),
        data.get('Imagen'),
        data.get('ImagenFondo'),
        data.get('Notas'),
        data.get('Empresas')
    ]

    return execute_stored_procedure(sp, params)

