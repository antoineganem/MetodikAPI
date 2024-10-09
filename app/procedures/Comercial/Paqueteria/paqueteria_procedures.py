import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection
from app.utils.config import get_db_session, close_db_session


def ver_paqueteria():
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True    

        query = "EXEC spVerPaqueteria"
        cursor.execute(query)
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def nueva_paqueteria(data):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        conn.autocommit = True  
        query = "EXEC spNvaPaqueteria ?,?"
        cursor.execute(query, data.get("PersonaID"), data.get("EmpresaID"))
        
        while cursor.description is None:
            cursor.nextset()
        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        if conn:
            conn.rollback()  # En caso de error, revertir la transacción
        return {"error": str(e)}, 500  
    finally:
        if conn:
            close_db_connection(conn)
            
def ver_paqueteriaID(ID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True  

        query = "EXEC spVerPaqueteriaID ?"
        cursor.execute(query, ID)
        
        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def ver_ArtDispPaqueteria(EmpresaID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True   

        query = "EXEC spVerArticulosPaqueteria ?"
        cursor.execute(query, EmpresaID)
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def avanza_paqueteria(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True   

        query = "EXEC spAvanzarPaqueteria ?,?,?,?,? ,?,?,?,?,? ,?"
        cursor.execute(query, data.get("ID"), data.get("Movimiento"), data.get("ClienteID"), data.get("TerminalOrigenID"), data.get("TerminalDestinoID")
                       , data.get("FechaEnvio"), data.get("FormaPagoID"), data.get("ReferenciaPago"), data.get("TelefonoDest"), data.get("NombreDest")
                       , data.get("PersonaID") )
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def agregar_paqueteriaDetalle(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True  

        query = "EXEC spAgregarPaqueteriaDetalle ?,?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"), data.get("Articulo"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def verPaqueteria_detalle(ID):
    session = get_db_session()  # Obtener una sesión del pool de SQLAlchemy
    try:
        conn = session.connection().connection  # Obtener la conexión cruda compatible con pyodbc
        cursor = conn.cursor()  # Crear el cursor para ejecutar la consulta

        query = "EXEC spVerPaqueteriaDetalle ?"
        cursor.execute(query, ID)  # Ejecutar el procedimiento almacenado con el parámetro

        # Iterar hasta obtener la descripción del cursor (si hay varios conjuntos de resultados)
        while cursor.description is None:
            cursor.nextset()

        # Si no hay resultados, retornar un error
        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        # Obtener los nombres de las columnas y los resultados
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results, 200

    except pyodbc.Error as e:
        session.rollback()  # Revertir la transacción en caso de error
        return {"error": str(e)}, 500

    finally:
        close_db_session(session)  # Cerrar la sesión al final para devolver la conexión al pool

            
            
def act_paqueteriaDetalle(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True  

        query = "EXEC spActDetallePaqueteria ?,?,?,?,? ,?"
        cursor.execute(query, data.get("ID"), data.get("RenglonID"), data.get("UsuarioID"), data.get("Cantidad"), data.get("Peso")
                       , data.get("Precio"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
            
def eliminar_renglonPaqueteria(ID, RenglonID, PersonaID):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True    

        query = "EXEC spEliminarDetallePaqueteria ?,?,?"
        cursor.execute(query, ID, RenglonID, PersonaID)
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def cambiar_situacion(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True    

        query = "EXEC spCambiarSituacionPaqueteria ?,?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"), data.get("Situacion"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def afectar_paqueteria(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True  

        query = "EXEC spAfectarPaqueteria ?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
            
def eliminar_paqueteria(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True   

        query = "EXEC spEliminarPaqueteria ?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)
            
def cancelar_paqueteria(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True  

        query = "EXEC spCancelarPaqueteria ?,?"
        cursor.execute(query, data.get("ID"), data.get("UsuarioID"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)