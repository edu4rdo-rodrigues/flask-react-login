# flask-react-login/backend/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.debug = True

# Configuração do CORS para permitir acesso de qualquer origem
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
