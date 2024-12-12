# Librerias a instalar

## Requerimientos

1. Install poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Añade poetry al PATH:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

3. Asegurate que funcione:
```bash
poetry --version
```

---

## Entorno de desarrollo

1. Clona el repositorio y entra a la raiz del proyecto.

2. En la raiz del proyecto ejecuta:
```bash
poetry install
```

3. Activa el entorno virtual:
```bash
source .venv/bin/activate
```

4. Run:
```bash
python3 run.py
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
