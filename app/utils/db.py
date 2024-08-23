import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=' + os.getenv('SQL_SERVER') + ';'
        'DATABASE=' + 'Metodik30' + ';'
        'UID=' + os.getenv('SQL_USER') + ';'
        'PWD=' + os.getenv('SQL_PASSWORD') + ';'
    )
    return conn

def close_db_connection(conn):
    try:
        conn.close()
    except pyodbc.Error as e:
        print(f"Error al cerrar la conexión: {e}")
