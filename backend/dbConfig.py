# flask-react-login/backend/config.py

from app import app

class Config:
    # Chave secreta para proteger sessões e outros dados
    SECRET_KEY = 'secret-key-goes-here'

    # URL do banco de dados MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql://rpz:aves123456@localhost/Login_Flask_DB'

    # Desativa o rastreamento de modificações do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
