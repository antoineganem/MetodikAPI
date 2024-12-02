# Librerias a instalar

## venv

1. Start venv:
```bash
    python3 -m venv venv/
```

2. Initialize:
```bash
    source venv/bin/activate
```

---

### Massive Install:

- Python dependencies:
```bash
    pip install flask pyodbc python-dotenv flask-swagger-ui flask-jwt-extended flask-cors sqlalchemy requests flask-socketio
```

- Others:
```bash
    # servicio sqlserver en mac
    brew install msodbcsql17 mssql-tools
```

---

1. Flask
Flask es el framework web que usaremos el funcionamiento de la API.

pip install flask


2. PyODBC
pyodbc es el paquete que utilizaremos para conectar Python con SQL Server y ejecutar los procedimientos almacenados.

pip install pyodbc

3. Python-Dotenv
Si quieres manejar las configuraciones sensibles (como las credenciales de la base de datos) en un archivo .env, python-dotenv es útil para cargar estas variables de entorno en tu aplicación Flask.

pip install python-dotenv

Swagger UI con Flask
pip install flask-swagger-ui

instalar servicio sqlserver en mac

brew install msodbcsql17 mssql-tools

instalar flask-jwt-extended 
pip install flask-jwt-extended    

CORS
pip install flask-cors

sqlalchemy
pip install sqlalchemy

requests
pip install requests

Flask-SocketIO   
pip install flask-socketio
