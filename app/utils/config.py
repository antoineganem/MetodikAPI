import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cargar las variables de entorno
load_dotenv()

# Crear el motor (engine) con el pool de conexiones
engine = create_engine(
    f"mssql+pyodbc://{os.getenv('SQL_USER')}:{os.getenv('SQL_PASSWORD')}@{os.getenv('SQL_SERVER')}/Metodik30?driver=ODBC+Driver+17+for+SQL+Server",
    pool_size=50,  # Aumentar el tamaño del pool si esperas más concurrencia
    max_overflow=50,  # Permitir más conexiones adicionales
    pool_pre_ping=True,  # Verificar si una conexión es válida antes de usarla
    pool_recycle=1800  # Reciclar conexiones más frecuentemente
)


# Crear la sesión
Session = sessionmaker(bind=engine)

def get_db_session():
    """
    Retorna una nueva sesión de la base de datos utilizando el pool de conexiones.
    """
    return Session()

def close_db_session(session):
    """
    Cierra la sesión de la base de datos.
    """
    try:
        session.close()
    except Exception as e:
        print(f"Error al cerrar la sesión de la base de datos: {e}")
