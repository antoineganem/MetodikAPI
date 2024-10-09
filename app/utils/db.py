import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()

def get_db_connection():
    # Asegúrate de que la conexión se abre sólo cuando es necesario
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=' + os.getenv('SQL_SERVER') + ';'
        'DATABASE=' + 'Metodik30' + ';'
        'UID=' + os.getenv('SQL_USER') + ';'
        'PWD=' + os.getenv('SQL_PASSWORD') + ';'
    )
    return conn

def close_db_connection(conn):
    # Cerrar la conexión correctamente
    try:
        if conn:
            conn.close()
    except pyodbc.Error as e:
        print(f"Error al cerrar la conexión: {e}")

# Uso de la conexión en funciones individuales
def execute_query(query, params=()):
    conn = get_db_connection()  # Abrir nueva conexión para cada consulta
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        
        # Procesar los resultados aquí...
        
        return cursor.fetchall()
    except pyodbc.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None
    finally:
        close_db_connection(conn)  # Cerrar la conexión al final
