from flask import jsonify, request
from app.models.usuario import Usuario
from app.persistence.usuario_dao import UsuarioDAO

usuario_dao = UsuarioDAO()

class UsuarioController:
    def listar_usuarios(self):
        usuarios = usuario_dao.listar_usuarios()
        usuarios_dict = [usuario.to_dict() for usuario in usuarios]
        return usuarios_dict
    
    def obter_usuario(self, usuario_id):
        usuario = usuario_dao.obter_usuario_por_id(usuario_id)
        if usuario:
            return usuario.to_dict()
        else:
            return {'message': 'Usuário não encontrado'}, 404

    
    def criar_usuario(self, request):
        data = request
        nome = data.get('nome')
        cpf = data.get('cpf')
        email = data.get('email')
        telefone = data.get('telefone')
        
        if not nome or not email:
            return {'message': 'Nome e email são campos obrigatórios'}, 400
        
        usuario = Usuario(nome=nome, cpf=cpf, email=email, telefone=telefone)
        result = usuario_dao.salvar_usuario(usuario)
        if isinstance(result, tuple):
            return {'error': result[0]}, result[1]
        
        return {'message': 'Usuário criado com sucesso'}, 201
    
    def atualizar_usuario(self, usuario_id, request):
        usuario = usuario_dao.obter_usuario_por_id(usuario_id)
        if not usuario:
            return {'message': 'Usuário não encontrado'}, 404
        
        data = request
        nome = data.get('nome')
        cpf = data.get('cpf')
        email = data.get('email')
        telefone = data.get('telefone')
        
        if not nome or not email:
            return {'message': 'Nome e email são campos obrigatórios'}, 400
        
        if cpf and cpf != usuario.cpf and usuario_dao.obter_usuario_por_cpf(cpf):
            return {'error': 'CPF já cadastrado'}, 400

        if email and email != usuario.email and usuario_dao.obter_usuario_por_email(email):
            return {'error': 'Email já cadastrado'}, 400

        usuario.nome = nome
        usuario.cpf = cpf
        usuario.email = email
        usuario.telefone = telefone
        usuario_dao.salvar_usuario(usuario)
        
        return {'message': 'Usuário atualizado com sucesso'}, 200
    
    def remover_usuario(self, usuario_id):
        usuario = usuario_dao.obter_usuario_por_id(usuario_id)
        if not usuario:
            return jsonify({'message': 'Usuário não encontrado'}), 404
        
        usuario_dao.remover_usuario(usuario)
        
        return jsonify({'message': 'Usuário removido com sucesso'}), 200
