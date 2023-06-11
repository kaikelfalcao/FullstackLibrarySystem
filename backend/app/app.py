from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from dotenv import load_dotenv


load_dotenv()

db = SQLAlchemy()

usuario =  os.getenv('USUARIO_BANCO')
senha = os.getenv('SENHA_BANCO')
endereco = os.getenv('ENDERECO_BANCO')
nome_do_banco = os.getenv('NOME_DO_BANCO')

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + usuario+ ':' + senha + '@' + endereco +':5432/' + nome_do_banco
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
    
    db.init_app(app)

    # Importe e registre os blueprints abaixo
    from app.routes.usuarios_routes import usuarios_bp
    app.register_blueprint(usuarios_bp)
    
    from app.routes.livros_routes import livros_bp
    app.register_blueprint(livros_bp)
    
    from app.routes.emprestimos_routes import emprestimos_bp
    app.register_blueprint(emprestimos_bp)
    
    
    return app
