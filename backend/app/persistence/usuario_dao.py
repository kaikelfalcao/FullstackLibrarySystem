from sqlalchemy.exc import IntegrityError
from app.models.usuario import Usuario
from app.app import db

class UsuarioDAO:
    def listar_usuarios(self):
        return Usuario.query.all()
    
    def obter_usuario_por_id(self, usuario_id):
        try:
            return Usuario.query.get(usuario_id)
        except AttributeError:
            return None

    def salvar_usuario(self, usuario):
        try:
            db.session.add(usuario)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            return str(e), 400
    
    def remover_usuario(self, usuario):
        db.session.delete(usuario)
        db.session.commit()

    def obter_usuario_por_cpf(self, cpf):
        return Usuario.query.filter_by(cpf=cpf).first()
    
    def obter_usuario_por_email(self, email):
        return Usuario.query.filter_by(email=email).first()
