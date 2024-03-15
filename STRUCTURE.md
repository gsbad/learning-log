# Estrutura do Projeto Learning App

A aplicação Learning App é estruturada em diversos diretórios e arquivos que compõem a base do projeto. Abaixo está detalhado o propósito de cada diretório e arquivo.

## Diretórios Raiz

### `learning-app/`
Raiz do projeto que contém todos os diretórios e arquivos relacionados à aplicação.

#### `learningLog/`
Diretório que contém a configuração principal do projeto Django, incluindo as configurações, URLs, e WSGI/ASGI para deploy.

##### `db.sqlite3`
Banco de dados SQLite usado pela aplicação para armazenar os dados.

##### `learningLog/`
Diretório com arquivos de configuração do Django.

###### `settings.py`
Define as configurações do Django, como banco de dados, aplicativos instalados, middlewares, etc.

###### `urls.py`
Define as URLs da aplicação para roteamento.

###### `wsgi.py` / `asgi.py`
Pontos de entrada WSGI e ASGI para compatibilidade com servidores web.

##### `learningLogApp/`
Diretório da aplicação específica do Django que contém modelos, visualizações, formulários, e templates.

###### `models.py`
Define os modelos do banco de dados.

###### `views.py`
Contém as funções de visualização que retornam respostas para as requisições.

###### `forms.py`
Define os formulários usados na aplicação.

###### `admin.py`
Configuração da interface administrativa.

###### `urls.py`
Define as URLs específicas da aplicação para roteamento.

###### `migrations/`
Diretório que contém as migrações do banco de dados.

###### `templates/learningLogApp/`
Templates HTML usados pela aplicação.

##### `manage.py`
Script de linha de comando do Django para tarefas administrativas.

### `ll_env/`
Ambiente virtual Python que contém as dependências do projeto.

#### `bin/`
Contém os executáveis do ambiente virtual, incluindo o interpretador Python e scripts para ativar o ambiente em diferentes shells.

#### `lib/python3.10/site-packages/`
Diretório que contém os pacotes Python instalados no ambiente virtual.