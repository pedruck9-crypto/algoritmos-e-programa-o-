# CRUD de Filmes e Séries

Projeto simples em FastAPI para administrar um catálogo de filmes e séries (SQLite com SQLModel ORM).

**Arquivos principais**
- `crud_filmes_e_series.py` — aplicação FastAPI (endpoints CRUD).
- `db.py` — modelos SQLModel e operações ORM para o banco SQLite (`midias.db`).
- `seed_midias.py` — script CLI para popular o banco com mídias fictícias.
- `requirements.txt` — dependências do projeto.

Pré-requisitos
- Python 3.8+ instalado

Instalação

Abra um terminal no diretório do projeto (`C:\Users\DELL\Documents`) e crie (opcional) um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install -r requirements.txt
```

Executando a aplicação

**Opção 1: Usando o script de inicialização (recomendado)**

```powershell
.\run.ps1
```

**Opção 2: Comando manual**

```powershell
cd "C:\Users\DELL\Documents"
python -m uvicorn crud_filmes_e_series:app --reload
```

Acesse a API em `http://127.0.0.1:8000` e a documentação automática em `http://127.0.0.1:8000/docs`.

Executando com Docker

Com o Docker Desktop aberto, execute no diretório do projeto:

```powershell
docker compose up --build
```

Acesse `http://127.0.0.1:8000`. O banco SQLite ficará em `data/midias.db` e será preservado mesmo que o container seja recriado.

Para executar em segundo plano:

```powershell
docker compose up --build -d
```

Para parar:

```powershell
docker compose down
```

Popular o banco (seed)

Para popular com mídias de exemplo rode o script CLI (não é mais uma rota no app):

```powershell
python seed_midias.py
```

Endpoints principais

- `GET /midias` — lista mídias. Suporta query params: `limit`, `offset`, `titulo`, `genero`, `tipo`.
  - Ex.: `/midias?limit=10&offset=0`
  - Ex.: `/midias?titulo=Duna`
  - Ex.: `/midias?tipo=filme`
- `GET /midias/{midia_id}` — retorna uma mídia específica.
- `POST /midias` — cria nova mídia. Corpo JSON exemplo:

```json
{
  "titulo": "Duna",
  "tipo": "filme",
  "genero": "ficção científica",
  "ano": 2021,
  "sinopse": "Sinopse do filme"
}
```

- `PUT /midias/{midia_id}` — atualiza campos (envie apenas os campos a alterar).
- `DELETE /midias/{midia_id}` — remove uma mídia.

Credenciais

A aba **Credenciais** gera automaticamente um `username` único e uma senha com letras maiúsculas, minúsculas e números.

- `POST /credenciais/gerar` — gera e salva um novo login e senha.
- `GET /credenciais` — lista os logins gerados, sem exibir senhas ou hashes.

A senha aparece somente na resposta da geração. Copie e guarde a senha nesse momento.

Regra automática

Quando já existir uma credencial e uma mídia no banco, o sistema cria automaticamente o filme **Vingadores: Ultimato**. Essa regra funciona independentemente da ordem dos eventos e não cria duplicatas.

Testes automatizados

Os testes ficam em `tests/test_api.py` e usam um banco SQLite temporário. Execute:

```powershell
python -m pytest tests -q
```

Os testes cobrem o CRUD completo de mídias, a validação do tipo de mídia e a geração segura de credenciais.

Validação
- O campo `tipo` é validado via `Enum` e aceita apenas `filme` ou `série`.

Banco de dados
- O arquivo SQLite criado é `midias.db` no mesmo diretório do projeto.
- O acesso aos dados é feito com SQLModel, usando os modelos `Midia` e `Usuario`.
- A inicialização usa `SQLModel.metadata.create_all` e preserva tabelas e dados existentes.

Próximos passos sugeridos
- Configurar migrações versionadas com Alembic para alterações futuras no esquema.
- Adicionar autenticação real para proteger os endpoints de credenciais.

