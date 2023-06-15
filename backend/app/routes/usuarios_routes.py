from flask import Blueprint,request
from app.controllers.usuario_controller import UsuarioController

usuario_controller = UsuarioController()


usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        usuarios = usuario_controller.listar_usuarios()
        return usuarios
    except Exception as e:
        return {'error': str(e)}


@usuarios_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
def obter_usuario(usuario_id):
    try:
        return usuario_controller.obter_usuario(usuario_id)
    except Exception as e:
        return {'error': str(e)}


@usuarios_bp.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    try:
        return usuario_controller.criar_usuario(request.json)
    except Exception as e:
        return {'error': str(e)}


@usuarios_bp.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def atualizar_usuario(usuario_id):
    try:
        return usuario_controller.atualizar_usuario(usuario_id, request.json)
    except Exception as e:
        return {'error': str(e)}


@usuarios_bp.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def remover_usuario(usuario_id):
    try:
        return usuario_controller.remover_usuario(usuario_id)
    except Exception as e:
        return {'error': str(e)}