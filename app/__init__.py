from flask import Flask
from app.config import Config
from app.routes.__init_ import register_routes
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager
from flask_cors import CORS  # Importa CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Habilitar CORS para toda la aplicación
    CORS(app)  # Esto habilita CORS para toda la API

    # Inicializar JWTManager
    jwt = JWTManager(app)

    register_routes(app)

    # Configuración de Swagger UI
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "MetodikApi"
        }
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Documentación de la seguridad en Swagger
    swagger_template = {
        "components": {
            "securitySchemes": {
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }
        },
        "security": [{"BearerAuth": []}],
    }

    return app
