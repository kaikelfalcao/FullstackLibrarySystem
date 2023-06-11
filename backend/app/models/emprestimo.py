from app.app import db
from datetime import date

class Emprestimo(db.Model):
    __tablename__ = 'emprestimos'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    livro_id = db.Column(db.Integer, db.ForeignKey('livros.id'), nullable=False)
    data_emprestimo = db.Column(db.Date, nullable=False)
    data_devolucao = db.Column(db.Date)

    def __repr__(self):
        return f'<Emprestimo {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'livro_id': self.livro_id,
            'data_emprestimo': self.data_emprestimo.strftime('%Y-%m-%d') if self.data_emprestimo else None,
            'data_devolucao': self.data_devolucao.strftime('%Y-%m-%d') if self.data_devolucao else None
        }