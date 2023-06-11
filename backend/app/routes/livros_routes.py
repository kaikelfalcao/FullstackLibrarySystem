from flask import Blueprint,request

from app.controllers.livro_controller import LivroController

livros_bp = Blueprint('livros', __name__)

livro_controller = LivroController()

@livros_bp.route('/livros', methods=['GET'])
def listar_livros():
    try:

        livros = livro_controller.listar_livros()

        livros_dict = [livro.to_dict() for livro in livros]

        return livros_dict
    except Exception as e:
        return {'error': str(e)}
    
@livros_bp.route('/livros/autor/<string:autor>', methods=['GET'])
def listar_livros_por_autor(autor):
    try:
        return livro_controller.listar_livros_por_autor(autor)
    except Exception as e:
        return {'error': str(e)}

@livros_bp.route('/livros/titulo/<string:titulo>', methods=['GET'])
def buscar_livro_por_titulo(titulo):
    try:
        return livro_controller.buscar_livro_por_titulo(titulo)
    except Exception as e:
        return {'error': str(e)}

@livros_bp.route('/livros/<int:livro_id>', methods=['GET'])
def obter_livro(livro_id):
    try:
        livro = livro_controller.obter_livro(livro_id)
        
        return livro
    except Exception as e:
        return {'error': str(e)}

@livros_bp.route('/livros', methods=['POST'])
def adicionar_livro():
    try:
        return livro_controller.adicionar_livro(request.json)
    except Exception as e:
        return {'error': str(e)}

@livros_bp.route('/livros/<int:livro_id>', methods=['PUT'])
def atualizar_livro(livro_id):
    try:
        return livro_controller.atualizar_livro(livro_id, request.json)
    except Exception as e:
        return {'error': str(e)}

@livros_bp.route('/livros/<int:livro_id>', methods=['DELETE'])
def remover_livro(livro_id):
    try:
        return livro_controller.remover_livro(livro_id)
    except Exception as e:
        return {'error': str(e)}