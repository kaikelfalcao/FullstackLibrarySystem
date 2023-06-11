export class Emprestimo {
  id: number;
  usuarioId: number;
  livroId: number;
  nomeUsuario: string;
  emailUsuario: string;
  nomeLivro: string;
  autorLivro: string;
  dataEmprestimo: string;
  dataDevolucao: string;

  constructor(id: number, usuarioId: number, livroId: number) {
    this.id = id;
    this.usuarioId = usuarioId;
    this.livroId = livroId;
    this.nomeUsuario = '';
    this.emailUsuario = '';
    this.nomeLivro = '';
    this.autorLivro = '';
    this.dataEmprestimo = '';
    this.dataDevolucao = '';

  }
}
