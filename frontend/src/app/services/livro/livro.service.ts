import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Livro } from '../../models/livro';

@Injectable({
  providedIn: 'root'
})
export class LivroService {
  private apiUrl = 'http://localhost:5000/livros'; // URL da API backend

  constructor(private http: HttpClient) { }

  getLivros(): Observable<Livro[]> {
    return this.http.get<Livro[]>(this.apiUrl);
  }

  adicionarLivro(livro: Livro): Observable<any> {
    return this.http.post(this.apiUrl, livro);
  }

  editarLivro(livro: Livro): Observable<any> {
    const url = `${this.apiUrl}/${livro.id}`;
    return this.http.put(url, livro);
  }

  excluirLivro(id: number): Observable<any> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.delete(url);
  }

  obterLivroPorId(livroId: number): Observable<any> {
    const url = `${this.apiUrl}/${livroId}`;
    return this.http.get<any>(url);
  }

  buscarLivrosPorTitulo(titulo: string): Observable<Livro[]> {
    const url = `${this.apiUrl}/titulo/${titulo}`;
    return this.http.get<Livro[]>(url);
  }

  buscarLivrosPorAutor(autor: string): Observable<Livro[]> {
    const url = `${this.apiUrl}/autor/${autor}`;
    return this.http.get<Livro[]>(url);
  }

}

