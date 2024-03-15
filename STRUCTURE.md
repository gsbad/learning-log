# Estrutura do Projeto Learning-App

Este documento descreve a organização geral do projeto Learning-App.

## Diretórios

- `/learning_app/`: Raiz do projeto Django, contendo o arquivo de configuração do projeto.
- `/app/`: Contém a lógica principal do aplicativo, incluindo modelos, visualizações e templates.
- `/migrations/`: Armazena as migrações do banco de dados para evoluir o esquema do banco de dados.

## Arquivos Principais

- `settings.py`: Configurações do projeto Django, incluindo configuração de banco de dados, aplicativos instalados, middleware, etc.
- `urls.py`: Define as rotas URL do projeto e suas respectivas views.
- `models.py`: Define os modelos de dados do aplicativo.
- `views.py`: Contém a lógica de apresentação, conectando modelos e templates.