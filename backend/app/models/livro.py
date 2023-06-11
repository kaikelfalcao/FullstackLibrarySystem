from app.app import db

class Livro(db.Model):
    __tablename__ = 'livros'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    ano_publicacao = db.Column(db.String(100))
    editora = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
    localizacao = db.Column(db.String(100), default=lambda: "Sistema" if Livro.tipo != "Fisico" else None)
    
    def __repr__(self):
        return f'<Livro {self.titulo}>'

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'ano_publicacao': self.ano_publicacao,
            'editora': self.editora,
            'tipo': self.tipo,
            'localizacao': self.localizacao
        }