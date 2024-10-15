import pyodbc
from app.utils.config import get_db_session, close_db_session

def execute_stored_procedure(sp_name, params):
    session = get_db_session()  
    try:
        conn = session.connection().connection 
        cursor = conn.cursor()  
        conn.autocommit = True    

        query = f"EXEC {sp_name} " + ','.join(['?' for _ in params])
        cursor.execute(query, *params)

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
