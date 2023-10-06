# flask-react-login/backend/main.py

from flask import Flask, jsonify
from flask_cors import CORS
from models.usuario import db
from routes.routes import Routes
from flask_migrate import Migrate
from dbConfig import Config

app = Flask(__name__)
CORS(app)



# Carregue as configurações do objeto Config
app.config.from_object(Config)

# Inicialize o SQLAlchemy diretamente no main.py
db.init_app(app)

migrate = Migrate(app, db)
# Crie uma instância da classe Routes e passe o aplicativo Flask para ela
Routes(app)

with app.app_context():
    db.create_all()

# Manipulador de erro CORS personalizado
@app.errorhandler(500)
def handle_cors_error(e):
    return jsonify({"error": "Erro de CORS"}), 500

if __name__ == '__main__':
    app.run(debug=True)
