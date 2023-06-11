from flask import Blueprint,request
from app.controllers.emprestimo_controller import EmprestimoController

emprestimo_controller = EmprestimoController()

emprestimos_bp = Blueprint('emprestimos', __name__)

@emprestimos_bp.route('/emprestimos', methods=['POST'])
def realizar_emprestimo():
    try:
        print(request.json)
        return emprestimo_controller.realizar_emprestimo(request.json)
    except Exception as e:
        return {'error': str(e)}

@emprestimos_bp.route('/emprestimos/<int:emprestimo_id>', methods=['PUT'])
def devolver_emprestimo(emprestimo_id):
    try:
        return emprestimo_controller.devolver_emprestimo(emprestimo_id)
    except Exception as e:
        return {'error': str(e)}

@emprestimos_bp.route('/emprestimos', methods=['GET'])
def listar_emprestimos():
    try:
        emprestimos = emprestimo_controller.listar_emprestimos()

        emprestimos_dict = [emprestimo.to_dict() for emprestimo in emprestimos]

        return emprestimos_dict
    except Exception as e:
        return {'error': str(e)}

@emprestimos_bp.route('/emprestimos/<int:emprestimo_id>', methods=['DELETE'])
def remover_emprestimo(emprestimo_id):
    try:
        return emprestimo_controller.remover_emprestimo(emprestimo_id)
    except Exception as e:
        return {'error': str(e)}
