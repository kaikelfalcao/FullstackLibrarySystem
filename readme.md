<h1 align="center" style="font-weight: bold;">Fullstack Library System 💻</h1>

<p align="center">
 <a href="#tech">Tecnologias</a> • 
 <a href="#started">Se preparando</a> •
 <a href="#routes">APP Routes</a> • 
 <a href="#colab">Colaboladores</a> •
 <a href="#contribute">Contribua</a>
</p>

<p align="center">
    <b>Um CRUD de um sistema de Biblioteca com Angular, Flask e Postgres </b>
</p>

<h2 id="technologies">💻 Tecnologias</h2>

- Angular 16
- Flask
- PostGres

<h2 id="started">🚀 Se preparando</h2>

Para iniciar essa aplicação siga esses passos, estou considerando que o servidor PostGres ja esteja aberto e o banco de dados criado

<h3>Prerequisites</h3>


- [PYTHON](https://www.python.org/downloads/)
- [FLASK](https://flask.palletsprojects.com/en/2.3.x/)
- [Node](https://nodejs.org/en)
- [POSTGRES](https://www.postgresql.org/download/)


<h3>Cloning</h3>

Para clonar basta rodar

```bash
git clone https://github.com/LimeHawk/FullstackLibrarySystem
```

<h3>Starting BackEnd </h3>

Para começar siga esses Passos:

```bash
cd FullstackLibrarySystem
cd backend
```
Crie um .env com as seguintes informações e salve na raiz do projeto:

```bash
USUARIO_BANCO = "Usuario no postgres"
SENHA_BANCO = "senha do postgres"
ENDERECO_BANCO = "localhost"
NOME_DO_BANCO = "nome do BD"
```
Instanciando e Iniciando o servidor para Windows ou Linux:

Windows
```bash
python -m venv nome_do_ambiente
python -m venv nome_do_ambiente
nome_do_ambiente\Scripts\activate.bat
pip install -r requirements.txt
python main.py
```

Linux

```bash
python3 -m venv nome_do_ambiente
source nome_do_ambiente/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

<h3>Starting FrontEnd </h3>

Para começar siga esses Passos:

```bash
cd FullstackLibrarySystem
cd frontend
```

Instalando Dependencias
```bash
npm install
```

Após a conclusão da instalação iniciar o servidor Angular
```bash
ng serve
```

Com isso basta acessar pelo seu navegador a seguinte URL: http://localhost:4200


<h1 id="routes">📍 Application Routes</h1>

Como você estará rodando localmente todas as saidas estarão na http://127.0.0.1:5000

<h2> Usuários </h2>

​
| route               | request    | response                                        
|----------------------|-----------------------------------------------------|---------------------------
| <kbd>GET /usuarios</kbd>   | None | A lista de Usuários no banco
| <kbd>GET /usuarios/<int:usuario_id> </kbd>  | None | Pegar Usuário com id 
| <kbd>POST /usuarios</kbd> | `json` with `nome` , `email` , `telefone` , `CPF`| `json` `message`
| <kbd>PUT /usuarios/<int:usuario_id></kbd>  | `json` with `nome` , `email` , `telefone` , `CPF` and `id`| `json` `message`
| <kbd>DELETE /usuarios/<int:usuario_id> </kbd> | None | `json` `message`

<h2> Livros </h2>

| route               | request    | response                                        
|----------------------|-----------------------------------------------------|---------------------------
| <kbd>GET /livros</kbd>   | None | A lista de livros no banco
| <kbd>GET /livros/autor/string:autor </kbd>   | None | A lista de livros no banco com o autor parecido
| <kbd>GET /livros/titulo/string:titulo </kbd>   | None | A lista de livros no banco com o titulo parecido
| <kbd>GET /livros/<int:livro_id> </kbd>  | None | Pegar Livro com id 
| <kbd>POST /livros</kbd> | `json` with `titulo` , `autor` , `ano_publicao` , `editora`, `tipo`,`localizacao`| `json` `message`
| <kbd>PUT /livros/int:id</kbd> | `json` with `titulo` , `autor` , `ano_publicao` , `editora`, `tipo`,`localizacao` and `id`| `json` `message`
| <kbd>DELETE /livros/int:id </kbd> | None | `json` `message`

<h2> Emprestimos </h2>

| route               | request    | response                                        
|----------------------|-----------------------------------------------------|---------------------------
| <kbd>GET /emprestimos</kbd>   | None | A lista de emprestimos no banco
| <kbd>POST /emprestimos</kbd> | `json` with `livro_id` , `usuario_id` , `data_emprestimo`| `json` `message`
| <kbd>PUT /emprestimos/<int:emprestimo_id></kbd>  | `json` with `livro_id` , `usuario_id` , `data_emprestimo` and `id`| `json` `message`
| <kbd>DELETE /emprestimos/<int:emprestimo_id> </kbd> | None | `json` `message`




<h2 id="colab">🤝 Collaborators</h2>

Special thank you for all people that contributed for this project.

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LimeHawk">
        <img src="https://avatars.githubusercontent.com/u/96706378?s=400&u=c9ec291bbbb7ff2f92b39ba6350b6eb6894e7036&v=4" width="100px;" alt="Kaike Profile Picture"/><br>
        <sub>
          <b>Kaíke Falcão</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/BisNeT0">
        <img src="https://avatars.githubusercontent.com/u/111530921?v=4" width="100px;" alt="Henrique Profile Picture"/><br>
        <sub>
          <b>Henrique Bisneto</b>
        </sub>
      </a>
    </td>
    </td>
    <td align="center">
      <a href="https://github.com/imtakezo">
        <img src="https://avatars.githubusercontent.com/u/62066012?v=4" width="100px;" alt="JoaoVictor Profile Picture"/><br>
        <sub>
          <b>João Victor</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/vShipa">
        <img src="https://avatars.githubusercontent.com/u/135391335?v=4" width="100px;" alt="Vitor Profile Picture"/><br>
        <sub>
          <b>Vitor Gabriel</b>
        </sub>
      </a>
    </td>
    
    
  </tr>
</table>



<h2 id="contribute">📫 Contribute</h2>

Apenas seguir os passos abaixo para contribuir, será de enorme ajuda

1. `git clone https://github.com/LimeHawk/FullstackLibrarySystem
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!

<h3>Documentations that might help</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
