import os
from dotenv import load_dotenv

load_dotenv()


if os.getenv('PYTHONDONTWRITEBYTECODE') == '1':
    import sys
    sys.dont_write_bytecode = True

class Config:
    SQL_SERVER = os.getenv('SQL_SERVER')
    SQL_DATABASE = os.getenv('SQL_DATABASE')
    SQL_USER = os.getenv('SQL_USER')
    SQL_PASSWORD = os.getenv('SQL_PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = False
