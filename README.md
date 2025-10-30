# Clone Twitter

Aplicativo desenvolvido como projeto final do curso **Desenvolvedor Full Stack Python** da **EBAC**.

## Descrição

O Clone Twitter é um aplicativo que replica as principais funcionalidades do Twitter. As funcionalidades de interação são: postar, seguir, curtir e comentar. As funcionalidades de configuração são: alterar nome, foto e senha.

## Pré-requisitos

```

python >= 3.10
pip >= 22.0

```

## Instalação local

1. Clone do repositório

   ```shell
   git clone https://github.com/lucaspereira12/clone-twitter.git
   ```


2. Instalação das dependências:

   ```shell
   cd twitter-clone
   pip install -r requirements.txt
   ```


3. Execução do servidor de desenvolvimento local:

   ```shell
   python manage.py migrate
   python manage.py runserver
   ```