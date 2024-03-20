# Learning App - Registro de Entradas por Assuntos

Este é um aplicativo Django para registrar entradas por assuntos, semelhante a um diário de aprendizado.

## Configuração do Ambiente Local

Para configurar o ambiente local e executar o aplicativo em sua máquina, siga estas etapas:

### 1. Clonar o Repositório

```https://github.com/gsbad/learning-log.git```

### 2. Configurar o Ambiente Virtual

Certifique-se de ter o Python e o ambiente virtual instalados em sua máquina. Depois, navegue até o diretório clonado e crie um ambiente virtual:

```sh
cd learning-app
python -m venv ll_env
```

Em seguida, ative o ambiente virtual:

#### No Windows:
```sh
ll_env\Scripts\activate
```

#### No macOS/Linux:
```sh
source ll_env/bin/activate
```

### 3. Instalar Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:
```sh
python manage.py migrate
```

### 5. Executar o Servidor de Desenvolvimento

Com tudo configurado, você pode iniciar o servidor de desenvolvimento:
```sh
python manage.py runserver
```


## Contribuindo

Se você quiser contribuir para este projeto, por favor, abra uma issue ou envie um pull request. Estamos abertos a sugestões e melhorias!

