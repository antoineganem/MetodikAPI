from flask import Flask
from app.routes.login.login import login_bp  # Asegúrate de que estás importando el blueprint

def register_routes(app: Flask):
    app.register_blueprint(login_bp)  # Asegúrate de registrar el blueprint correcto
