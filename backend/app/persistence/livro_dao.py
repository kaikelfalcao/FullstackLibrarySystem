from app.models.livro import Livro
from app.app import db
from app.models.emprestimo import Emprestimo

class LivroDAO:
    def listar_livros(self):
        return Livro.query.all()
    
    def listar_livros_por_autor(self, autor):
        return Livro.query.filter(Livro.autor.ilike(f'%{autor}%')).order_by(Livro.titulo).limit(10).all()

    def buscar_livro_por_titulo(self, titulo):
        return Livro.query.filter(Livro.titulo.ilike(f'%{titulo}%')).limit(5).all()

    def obter_livro_por_id(self, livro_id):
        return Livro.query.get(livro_id)
    
    def salvar_livro(self, livro):
        db.session.add(livro)
        db.session.commit()
    
    def remover_livro(self, livro):
        emprestimos_pendentes = Emprestimo.query.filter_by(livro_id=livro.id, data_devolucao=None).all()
        
        print(emprestimos_pendentes)
        if emprestimos_pendentes:
            return False
        
        emprestimos_existentes = Emprestimo.query.filter(Emprestimo.livro_id == livro.id, Emprestimo.data_devolucao.isnot(None)).all()

        
        if emprestimos_existentes:
            for emprestimo in emprestimos_existentes:
                db.session.delete(emprestimo)
        
        db.session.delete(livro)
        db.session.commit()

    
