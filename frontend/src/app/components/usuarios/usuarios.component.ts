import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/usuario/usuario.service';
import { Usuario } from '../../models/usuario';

@Component({
  selector: 'app-usuarios',
  templateUrl: './usuarios.component.html',
  styleUrls: ['./usuarios.component.css']
})
export class UsuariosComponent implements OnInit {
  usuarios: Usuario[] = [];
  
  exibirFormulario: boolean = false;
  usuario: Usuario = {
    id: 0,
    nome: '',
    cpf: '',
    email: '',
    telefone: ''
  };
  modoEdicao: boolean = false;

  constructor(private userService: UserService) { }

  ngOnInit() {
    this.carregarUsuarios();
  }

  alternarFormulario() {
    this.exibirFormulario = !this.exibirFormulario;
    this.modoEdicao = false;

    if (!this.exibirFormulario) {
      this.limparFormulario();
    }
  }

  salvarUsuario() {
    if (this.modoEdicao) {
      this.userService.editarUsuario(this.usuario).subscribe(() => {
        console.log('Livro atualizado com sucesso');
        this.carregarUsuarios();
        this.limparFormulario();
        this.alternarFormulario(); 
      }, error => {
        console.log('Erro ao atualizar livro:', error);
      });
    } else {
      this.userService.adicionarUsuario(this.usuario).subscribe(() => {
        this.carregarUsuarios();
        this.limparFormulario();
        this.alternarFormulario(); 
      });
    }
  }

  

  adicionarUsuario() {
    this.userService.adicionarUsuario(this.usuario).subscribe(() => {
      this.carregarUsuarios();
      this.limparFormulario();
      this.exibirFormulario = false; // Fechar o formulário
    });
  }

  carregarUsuarios() {
    this.userService.getUsuarios().subscribe(usuarios => {
      this.usuarios = usuarios;
    });
  }

  excluirUsuario(id: number) {
    console.log('Excluir usuário ID:', id);
    this.userService.excluirUsuario(id).subscribe(() => {
      console.log('Usuário excluído com sucesso');
      this.carregarUsuarios();
    }, error => {
      console.log('Erro ao excluir usuário:', error);
      alert('Erro ao excluir Usuário: ' + error.error.message);
    });
  }

  editarUsuario(usuario: Usuario) {
    this.usuario = { ...usuario }; // Copia as propriedades do usuário para o formulário
    this.modoEdicao = true;
    this.exibirFormulario = true;
  }

  private limparFormulario() {
    this.usuario = {
      id: 0,
      nome: '',
      cpf: '',
      email: '',
      telefone: ''
    };
  }
}
