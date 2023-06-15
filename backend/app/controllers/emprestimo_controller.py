import datetime
from flask import jsonify, request
from app.models.emprestimo import Emprestimo
from app.persistence.emprestimo_dao import EmprestimoDAO
from app.persistence.usuario_dao import UsuarioDAO
from app.persistence.livro_dao import LivroDAO

usuario_dao = UsuarioDAO()
livro_dao = LivroDAO()
emprestimo_dao = EmprestimoDAO()

class EmprestimoController:
    
    def listar_emprestimos(self):
        emprestimos = emprestimo_dao.listar_emprestimos()
        return emprestimos
    
    def obter_emprestimo(self, emprestimo_id):
        emprestimo = emprestimo_dao.obter_emprestimo_por_id(emprestimo_id)
        if emprestimo:
            return emprestimo, 200
        else:
            return {'message': 'Empréstimo não encontrado'}, 404
    
    def realizar_emprestimo(self, data):
        usuarioId = data.get('usuarioId')
        livroId = data.get('livroId')

        if not usuarioId or not livroId:
            return {'message': 'Usuário e livro são obrigatórios'}, 400

        usuario = usuario_dao.obter_usuario_por_id(usuarioId)
        livro = livro_dao.obter_livro_por_id(livroId)

        if not usuario or not livro:
            return {'message': 'Usuário ou livro não encontrado'}, 404

        emprestimo = Emprestimo(usuario_id=usuarioId, livro_id=livroId, data_emprestimo=datetime.date.today())
        result = emprestimo_dao.salvar_emprestimo(emprestimo)
        return result
    
    def devolver_emprestimo(self, emprestimo_id):
        emprestimo = emprestimo_dao.obter_emprestimo_por_id(emprestimo_id)
        if emprestimo:
            emprestimo_dao.atualizar_data_devolucao(emprestimo)  
            return {'message': 'Empréstimo devolvido com sucesso'}, 200
        else:
            return {'message': 'Empréstimo não encontrado'}, 404


    def remover_emprestimo(self, emprestimo_id):
        emprestimo = emprestimo_dao.obter_emprestimo_por_id(emprestimo_id)
        if emprestimo:
            if emprestimo_dao.remover_emprestimo(emprestimo):
                return {'message': 'Empréstimo removido com sucesso'}, 200
            else:
                return {'message': 'Erro ao remover empréstimo'}, 500
        else:
            return {'message': 'Empréstimo não encontrado'}, 404
