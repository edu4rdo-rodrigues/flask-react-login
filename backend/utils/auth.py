# flask-react-login/backend/utils/auth.py

from flask import session
from models.usuario import Usuario  # Importe a classe de modelo de usuário, ajuste o caminho conforme necessário

def authenticate_user(email, senha):
    # Consulte o banco de dados para encontrar um usuário com o email fornecido
    usuario = Usuario.query.filter_by(email=email).first()

    # Verifique se o usuário existe e a senha está correta
    if usuario and usuario.verificar_senha(senha):
        return usuario.id  # Retorne o ID do usuário autenticado

    return None  # Retorne None se a autenticação falhar

def login_user(user_id):
    session['user_id'] = user_id

def logout_user():
    session.pop('user_id', None)

def is_logged_in():
    return 'user_id' in session
