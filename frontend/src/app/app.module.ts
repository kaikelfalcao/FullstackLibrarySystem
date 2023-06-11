import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UsuariosComponent } from './components/usuarios/usuarios.component';
import { LivrosComponent } from './components/livros/livros.component';
import { EmprestimosComponent } from './components/emprestimos/emprestimos.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { PaginaPrincipalComponent } from './components/pagina-principal/pagina-principal.component';


@NgModule({
  declarations: [
    
    AppComponent,
    UsuariosComponent,
    LivrosComponent,
    EmprestimosComponent,
    PaginaPrincipalComponent
  ],
  imports: [
    FormsModule,
    HttpClientModule,
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
