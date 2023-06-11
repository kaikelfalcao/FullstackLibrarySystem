import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Emprestimo } from '../../models/emprestimo';

@Injectable({
  providedIn: 'root'
})
export class EmprestimoService {
  private apiUrl = 'http://localhost:5000/emprestimos'; // URL da API backend

  constructor(private http: HttpClient) { }

  getEmprestimos(): Observable<Emprestimo[]> {
    return this.http.get<Emprestimo[]>(this.apiUrl);
  }

  adicionarEmprestimo(emprestimo: Emprestimo): Observable<any> {
    return this.http.post(this.apiUrl, emprestimo);
  }

  devolverEmprestimo(emprestimo: Emprestimo): Observable<any> {
    const url = `${this.apiUrl}/${emprestimo.id}`;
    return this.http.put(url, emprestimo);
  }

  excluirEmprestimo(id: number): Observable<any> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.delete(url);
  }
}
