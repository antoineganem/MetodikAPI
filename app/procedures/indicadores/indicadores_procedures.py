import pyodbc
from flask import jsonify
from app.utils.db import get_db_connection, close_db_connection
from app.utils.config import get_db_session, close_db_session

def ver_Indicadores(data):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()    

        query = "EXEC spVerIndicadores ?,?"
        cursor.execute(query, data.get("Tipo"), data.get("EmpresaID"))
        

        while cursor.description is None:
            cursor.nextset()

        if cursor.description is None:
            return {"error": "No data returned from the procedure."}, 500

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        session.commit()
        return results, 200  
    except pyodbc.Error as e:
        session.rollback() 
        return {"error": str(e)}, 500
    finally:
        close_db_session(session)





