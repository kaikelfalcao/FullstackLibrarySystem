import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Usuario } from '../../models/usuario';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'http://localhost:5000/usuarios'; // URL da API backend

  constructor(private http: HttpClient) { }

  getUsuarios(): Observable<Usuario[]> {
    return this.http.get<Usuario[]>(this.apiUrl);
  }

  adicionarUsuario(usuario: Usuario): Observable<any> {
    return this.http.post(this.apiUrl, usuario);
  }

  editarUsuario(usuario: Usuario): Observable<any> {
    const url = `${this.apiUrl}/${usuario.id}`;
    return this.http.put(url, usuario);
  }

  excluirUsuario(id: number): Observable<any> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.delete(url);
  }

  obterUsuarioPorId(usuarioId: number): Observable<any> {
    const url = `${this.apiUrl}/${usuarioId}`;
  return this.http.get<any>(url);
  }

  
}
