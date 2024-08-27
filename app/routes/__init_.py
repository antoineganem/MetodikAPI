from flask import Flask
from app.routes.login.login import login_bp  
from app.routes.Catalogos.Usuarios import usuarios_bp, usuariosResumen_bp, actUsuario_bp, verUsuarioID_bp

def register_routes(app: Flask):
    app.register_blueprint(login_bp) 
    app.register_blueprint(usuarios_bp)  
    app.register_blueprint(usuariosResumen_bp)  
    app.register_blueprint(actUsuario_bp)
    app.register_blueprint(verUsuarioID_bp)  
  

