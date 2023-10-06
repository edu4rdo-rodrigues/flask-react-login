# flask-react-login/backend/models/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.debug = True

# Configuração do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://seu_usuario:sua_senha@localhost/seu_banco_de_dados'
db = SQLAlchemy(app)

# Configuração do CORS para permitir acesso de qualquer origem
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})