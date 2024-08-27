from flask import Flask
from app.routes.login.login import login_bp  
from app.routes.Catalogos.Usuarios import usuarios_bp

def register_routes(app: Flask):
    app.register_blueprint(login_bp)  # Asegúrate de registrar el blueprint correcto
    app.register_blueprint(usuarios_bp)  # Asegúrate de registrar el blueprint correcto
