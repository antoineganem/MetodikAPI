import os
import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=' + os.getenv('SQL_SERVER') + ';'
        'DATABASE=' + os.getenv('SQL_DATABASE') + ';'
        'UID=' + os.getenv('SQL_USER') + ';'
        'PWD=' + os.getenv('SQL_PASSWORD') + ';'
    )
    return conn

def close_db_connection(conn):
    try:
        conn.close()
    except pyodbc.Error as e:
        print(f"Error al cerrar la conexión: {e}")
