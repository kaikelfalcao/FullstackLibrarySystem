from flask import jsonify, request
from app.models.livro import Livro
from app.persistence.livro_dao import LivroDAO

livro_dao = LivroDAO()

class LivroController:
    def listar_livros(self):
        livros = livro_dao.listar_livros()
        return livros
    
    def listar_livros_por_autor(self, autor):
        livros = livro_dao.listar_livros_por_autor(autor)
        livros_dict = [livro.to_dict() for livro in livros]
        return livros_dict

    def buscar_livro_por_titulo(self, titulo):
        livros = livro_dao.buscar_livro_por_titulo(titulo)
        livros_dict = [livro.to_dict() for livro in livros]
        if livros_dict:
            return livros_dict
        else:
            return {'message': 'Livro não encontrado'}, 404
    
    def obter_livro(self, livro_id):
        livro = livro_dao.obter_livro_por_id(livro_id)
        if livro:
            return livro.to_dict()
        else:
            return {'message': 'Livro não encontrado'},404
    
    def adicionar_livro(self,request):
        data = request
        titulo = data.get('titulo')
        autor = data.get('autor')
        ano_publicacao = data.get('ano_publicacao')
        editora = data.get('editora')
        tipo = data.get('tipo')
        localizacao = data.get('localizacao')
        
        if not titulo or not autor:
            return jsonify({'message': 'Título e autor são campos obrigatórios'}), 400
        
        livro = Livro(titulo=titulo, autor=autor, ano_publicacao=ano_publicacao,
                      editora=editora, tipo=tipo, localizacao=localizacao)
        livro_dao.salvar_livro(livro)
        
        return jsonify({'message': 'Livro criado com sucesso'}), 201
    
    def atualizar_livro(self, livro_id, request):
        livro = livro_dao.obter_livro_por_id(livro_id)
        if not livro:
            return {'message': 'Livro não encontrado'}, 404

        data = request
        titulo = data.get('titulo')
        autor = data.get('autor')
        ano_publicacao = data.get('ano_publicacao')
        editora = data.get('editora')
        tipo = data.get('tipo')
        localizacao = data.get('localizacao')

        if not titulo or not autor:
            return {'message': 'Título e autor são campos obrigatórios'}, 400

        livro.titulo = titulo
        livro.autor = autor
        livro.ano_publicacao = ano_publicacao
        livro.editora = editora
        livro.tipo = tipo  # Corrigido aqui
        livro.localizacao = localizacao
        livro_dao.salvar_livro(livro)

        return {'message': 'Livro atualizado com sucesso'}, 200

    
    def remover_livro(self, livro_id):
        livro = livro_dao.obter_livro_por_id(livro_id)
        
        if not livro:
            return {'message': 'Livro não encontrado'}, 404
        
        resultado = livro_dao.remover_livro(livro)
        
        if resultado is False:
            return {'message': 'Não é possível remover o livro. Existem empréstimos pendentes.'}, 400

        return {'message': 'Livro removido com sucesso'}, 200

