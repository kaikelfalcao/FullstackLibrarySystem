import { Component, HostListener, OnInit } from '@angular/core';
import { LivroService } from '../../services/livro/livro.service';
import { Livro } from '../../models/livro';

@Component({
  selector: 'app-livros',
  templateUrl: './livros.component.html',
  styleUrls: ['./livros.component.css']
})
export class LivrosComponent implements OnInit {
  livros: Livro[] = [];
  searchByTitle: string = "";
  searchByAuthor: string = "";
  
  exibirFormulario: boolean = false;
  livro: Livro = {
    id: 0,
    titulo: '',
    autor: '',
    ano_publicacao: '',
    editora: '',
    tipo: '',
    localizacao: ''
  };
  modoEdicao: boolean = false;

  constructor(private livroService: LivroService) { }

  ngOnInit() {
    this.carregarLivros();
  }
  
  buscarPorTitulo() {
    const termoBusca = this.searchByTitle;
    if (termoBusca && termoBusca.trim() !== '') {
      // Lógica de busca por título
      this.livroService.buscarLivrosPorTitulo(termoBusca).subscribe(resultado => {
        this.livros = resultado; 
        
      });
    } else {
      
      this.livroService.getLivros().subscribe(resultado => {
        this.livros = resultado; 
        
      });
    }
  }
  
  buscarPorAutor() {
    const termoBusca = this.searchByAuthor;
    if (termoBusca && termoBusca.trim() !== '') {
      // Lógica de busca por autor
      this.livroService.buscarLivrosPorAutor(termoBusca).subscribe(resultado => {
        this.livros = resultado; // Atualiza a variável livros com o resultado da busca
        
      });
    } else {
      
      this.livroService.getLivros().subscribe(resultado => {
        this.livros = resultado; 
        
      });
    }
  }
  

  alternarFormulario() {
    this.exibirFormulario = !this.exibirFormulario;
    this.modoEdicao = false;

    if (!this.exibirFormulario) {
      this.limparFormulario();
    }
  }

  salvarLivro() {
    if (this.livro.tipo !== 'Físico') {
      this.livro.localizacao = 'Sistema';
    }
  
    if (this.modoEdicao) {
      this.livroService.editarLivro(this.livro).subscribe(() => {
        console.log('Livro atualizado com sucesso');
        this.carregarLivros();
        this.limparFormulario();
        this.alternarFormulario();
      }, error => {
        console.log('Erro ao atualizar livro:', error);
      });
    } else {
      this.livroService.adicionarLivro(this.livro).subscribe(() => {
        this.carregarLivros();
        this.limparFormulario();
        this.alternarFormulario();
      });
    }
  }
  
  

  adicionarLivro() {
    this.livroService.adicionarLivro(this.livro).subscribe(() => {
      this.carregarLivros();
      this.limparFormulario();
    });
  }

  

  carregarLivros() {
    this.livroService.getLivros().subscribe(livros => {
      this.livros = livros;
    });
  }

  excluirLivro(id: number) {
    console.log('Excluir livro ID:', id);
    this.livroService.excluirLivro(id).subscribe(() => {
      console.log('Livro excluído com sucesso');
      this.carregarLivros();
    }, error => {
      console.log('Erro ao excluir livro:', error);
      alert('Erro ao excluir livro: ' + error.error.message);
    });
  }
  
  

  editarLivro(livro: Livro) {
    this.livro = { ...livro }; // Preenche o formulário com os dados do livro
    this.modoEdicao = true;
    this.exibirFormulario = true;
  }
  
  

  private limparFormulario() {
    this.livro = {
      id: 0,
      titulo: '',
      autor: '',
      ano_publicacao: '',
      editora: '',
      tipo: '',
      localizacao: ''
    };
  }
}
