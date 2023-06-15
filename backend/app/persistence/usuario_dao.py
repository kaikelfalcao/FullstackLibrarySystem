from sqlalchemy.exc import IntegrityError
from app.models.usuario import Usuario
from app.app import db
from app.models.emprestimo import Emprestimo

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
        emprestimos_pendentes = Emprestimo.query.filter_by(usuario_id=usuario.id, data_devolucao=None).all()
    
        print(emprestimos_pendentes)
        
        if emprestimos_pendentes:
            return False
        
        emprestimos_existentes = Emprestimo.query.filter(Emprestimo.usuario_id == usuario.id, Emprestimo.data_devolucao.isnot(None)).all()

        if emprestimos_existentes:
            for emprestimo in emprestimos_existentes:
                db.session.delete(emprestimo)

        db.session.delete(usuario)
        db.session.commit()

    def obter_usuario_por_cpf(self, cpf):
        return Usuario.query.filter_by(cpf=cpf).first()
    
    def obter_usuario_por_email(self, email):
        return Usuario.query.filter_by(email=email).first()
