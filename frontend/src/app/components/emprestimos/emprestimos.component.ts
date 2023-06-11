import { Component, OnInit } from '@angular/core';
import { EmprestimoService } from '../../services/emprestimo/emprestimo.service';
import { UserService } from '../../services/usuario/usuario.service';
import { LivroService } from '../../services/livro/livro.service';
import { Emprestimo } from '../../models/emprestimo';
import { Usuario } from '../../models/usuario';
import { Livro } from '../../models/livro';


@Component({
  selector: 'app-emprestimos',
  templateUrl: './emprestimos.component.html',
  styleUrls: ['./emprestimos.component.css']
})
export class EmprestimosComponent implements OnInit {
  emprestimos: Emprestimo[] = [];
  usuarios: Usuario[] = [];
  livros: Livro[] = [];

  exibirFormulario: boolean = false;
  emprestimo: Emprestimo = {
    id: 0,
    usuarioId: 0,
    livroId: 0,
    nomeUsuario: '',
    emailUsuario: '',
    nomeLivro: '',
    autorLivro: '',
    dataEmprestimo: '',
    dataDevolucao: ''
  };
  modoEdicao: boolean = false;

  constructor(
    private emprestimoService: EmprestimoService,
    private usuarioService: UserService,
    private livroService: LivroService
  ) {}

  ngOnInit() {
    this.carregarEmprestimos();
    this.carregarLivros();
    this.carregarUsuarios();
  }

  carregarUsuarios() {
    this.usuarioService.getUsuarios().subscribe((usuarios) => {
      this.usuarios = usuarios;
      
    });
  }

  carregarLivros() {
    this.livroService.getLivros().subscribe((livros) => {
      this.livros = livros;
      
    });
  }

  alternarFormulario() {
    this.exibirFormulario = !this.exibirFormulario;
    this.modoEdicao = false;

    if (!this.exibirFormulario) {
      this.limparFormulario();
    }
  }

  salvarEmprestimo() {
    if (this.modoEdicao) {
      this.devolverEmprestimo(this.emprestimo);
    } else {
      this.adicionarEmprestimo();
    }
  }

  adicionarEmprestimo() {
    const usuario = this.usuarios.find((u: any) => u.id == this.emprestimo.usuarioId);
    const livro = this.livros.find((l: any) => l.id == this.emprestimo.livroId);
  
    if (usuario && livro && livro.tipo === 'Físico' && !this.isLivroEmprestado(livro.id)){
      this.emprestimo.nomeUsuario = usuario.nome;
      this.emprestimo.emailUsuario = usuario.email;
      this.emprestimo.nomeLivro = livro.titulo;
      this.emprestimo.autorLivro = livro.autor;
  
      this.emprestimoService.adicionarEmprestimo(this.emprestimo).subscribe(() => {
        this.carregarEmprestimos();
        this.limparFormulario();
      });
    }
    else{
      alert("O Livro ja está emprestado ou não é um livro Físico para ser emprestado")
    }
  }
  
  
  
  carregarEmprestimos() {
    this.emprestimoService.getEmprestimos().subscribe((emprestimos) => {
      this.emprestimos = emprestimos;
      this.carregarDetalhesUsuariosLivros();
    });
  }

  isLivroEmprestado(livroId: number): boolean {
    return this.emprestimos.some((emprestimo) => emprestimo.livroId === livroId);
  }


  carregarDetalhesUsuariosLivros() {
    
    this.emprestimos.forEach((emprestimo) => {
      
      const emp = Object.assign(emprestimo)
      emprestimo.usuarioId = emp.usuario_id;
      emprestimo.livroId = emp.livro_id;
      emprestimo.dataEmprestimo = emp.data_emprestimo;
      emprestimo.dataDevolucao = emp.data_devolucao;
      this.usuarioService.obterUsuarioPorId(emprestimo.usuarioId).subscribe((usuario) => {
        emprestimo.nomeUsuario = usuario.nome;
        emprestimo.emailUsuario = usuario.email;
      });

      this.livroService.obterLivroPorId(emprestimo.livroId).subscribe((livro) => {
        emprestimo.nomeLivro = livro.titulo;
        emprestimo.autorLivro = livro.autor;
      });
    });
  }

    
  

  excluirEmprestimo(id: number) {
    this.emprestimoService.excluirEmprestimo(id).subscribe(
      () => {
        this.carregarEmprestimos();
      },
      (error) => {
        alert('Erro ao excluir empréstimo: ' + error.message);
      }
    );
  }
  
  devolverEmprestimo(emprestimo: Emprestimo) {
    this.emprestimoService.devolverEmprestimo(emprestimo).subscribe(
      () => {
        this.carregarEmprestimos();
        this.limparFormulario();
      },
      (error) => {
        alert('Erro ao devolver empréstimo: ' + error.message);
      }
    );
  }
  
  editarFormulario(emprestimo: Emprestimo) {
    this.exibirFormulario = true;
    this.modoEdicao = true;
    this.emprestimo = { ...emprestimo };
  }
  

  limparFormulario() {
    this.emprestimo = {
      id: 0,
      usuarioId: 0,
      livroId: 0,
      nomeUsuario: '',
      emailUsuario: '',
      nomeLivro: '',
      autorLivro: '',
      dataEmprestimo: '',
      dataDevolucao: ''
    };
  }
}
