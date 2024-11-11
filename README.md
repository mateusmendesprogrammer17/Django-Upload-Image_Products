Upload de Imagens com Django
Este guia irá te ensinar como configurar um projeto Django para realizar upload de imagens e configurar o banco de dados (MySQL). Vamos passar pelas etapas desde a criação do ambiente virtual até a execução do servidor.

1. Criar o Ambiente Virtual
Para garantir que as dependências do seu projeto sejam isoladas, é recomendado criar um ambiente virtual. Para criar o ambiente, execute o seguinte comando no terminal:

bash
Copiar código
python -m venv .venv
Este comando cria um diretório .venv no seu projeto, onde as dependências serão instaladas.

2. Ativar o Ambiente Virtual
Após a criação do ambiente virtual, ative-o para garantir que você está utilizando o Python e as dependências corretas para o projeto.

No Windows:

bash
Copiar código
.venv\Scripts\activate
No Linux/Mac:

bash
Copiar código
source .venv/bin/activate
Após ativar o ambiente, você verá o nome do ambiente virtual no início da linha de comando, indicando que ele está ativo.

3. Instalar Dependências
Agora, instale as bibliotecas necessárias para o projeto:

bash
Copiar código
pip install django
pip install mysqlclient
pip install pillow
pip install crispy-bootstrap5
pip install django-crispy-forms
Esses pacotes incluem:

Django: O framework para desenvolver o site.
mysqlclient: O adaptador para conectar o Django ao MySQL.
Pillow: Biblioteca para manipulação de imagens.
crispy-bootstrap5: Estilos para o Django com Bootstrap 5.
django-crispy-forms: Facilita a renderização de formulários Django com o Bootstrap.
4. Criar o Projeto Django
Crie o projeto Django com o comando:

bash
Copiar código
django-admin startproject nome_do_projeto .
Isso irá gerar a estrutura básica de um projeto Django no diretório atual.

5. Configurar o settings.py
Abra o arquivo settings.py do seu projeto e configure as seguintes opções:

Banco de Dados: Configure sua base de dados no Django (MySQL, PostgreSQL, etc.) com as credenciais necessárias.

Exemplo de configuração para MySQL:

python
Copiar código
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # para mariadb ou mysql
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Configuração de Upload de Imagens:

No mesmo arquivo settings.py, configure as variáveis de UPLOAD:

python
Copiar código
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL define a URL pública para acessar as imagens, enquanto MEDIA_ROOT define o caminho físico onde as imagens serão armazenadas.

6. Realizar Migrações
Execute o comando abaixo para aplicar as migrações iniciais do Django:

bash
Copiar código
python manage.py migrate
Isso cria as tabelas padrão do Django, como as relacionadas a sessões e autenticação de usuários.

7. Criar o App Django
Crie um aplicativo dentro do seu projeto Django. No exemplo, vamos chamar de store:

bash
Copiar código
python manage.py startapp store
Agora, você pode começar a adicionar suas funcionalidades dentro da pasta store.

8. Criar Migrações do Modelo
Se você criar ou modificar modelos no seu aplicativo, use o comando a seguir para gerar as migrações:

bash
Copiar código
python manage.py makemigrations
Isso criará as migrações necessárias para o banco de dados.

9. Aplicar as Migrações no Banco de Dados
Após gerar as migrações, execute o comando abaixo para aplicar as mudanças no banco de dados:

bash
Copiar código
python manage.py migrate
Esse comando aplica as alterações das migrações no banco de dados.

10. Rodar o Servidor
Agora, você pode iniciar o servidor de desenvolvimento Django:

bash
Copiar código
python manage.py runserver
O servidor estará disponível em http://127.0.0.1:8000, e você poderá acessar suas páginas da web localmente.

Lista de Bibliotecas Instaladas
Após a instalação das dependências, você pode verificar as versões das bibliotecas com o comando:

bash
Copiar código
pip list
Isso exibirá uma lista como a seguinte:

yaml
Copiar código
asgiref             3.8.1
crispy-bootstrap5   2024.10
Django              5.1.2
django-crispy-forms 2.3
mysqlclient         2.2.5
pillow              11.0.0
pip                 23.1.2
setuptools          65.5.0
sqlparse            0.5.1
tzdata              2024.2
