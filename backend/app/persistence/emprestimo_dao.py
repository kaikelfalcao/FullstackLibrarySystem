from datetime import date
from app.models.emprestimo import Emprestimo
from app.app import db

class EmprestimoDAO:
    
    def salvar_emprestimo(self, emprestimo):
        try:
            db.session.add(emprestimo)
            db.session.commit()
            return {'message': 'Empréstimo salvo com sucesso'}
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    def obter_emprestimo_por_id(self, emprestimo_id):
        return Emprestimo.query.get(emprestimo_id)
    
    def listar_emprestimos(self):
        return Emprestimo.query.all()
    
    def atualizar_data_devolucao(self, emprestimo):
        emprestimo.data_devolucao = date.today()
        db.session.commit()

    def remover_emprestimo(self, emprestimo):
        try:
            db.session.delete(emprestimo)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False