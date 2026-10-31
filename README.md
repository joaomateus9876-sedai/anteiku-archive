# 🩸 Tokyo Ghoul: Anteiku Archive (Arquivos Anteiku)

Um sistema de gerenciamento de personagens inspirado no universo de **Tokyo Ghoul**, desenvolvido como projeto de aprendizado e portfólio.

## ☕ Sobre o projeto

O Anteiku Archive é uma aplicação web que permite cadastrar, consultar, editar, pesquisar e excluir registros de personagens.

O projeto possui uma interface com estética sombria, inspirada na atmosfera de Tokyo Ghoul e na identidade do café Anteiku.

## 🚀 Tecnologias utilizadas

- Python
- Flask
- SQLite
- HTML5
- CSS3
- Jinja2

## ✨ Funcionalidades

- Cadastro de personagens.
- Listagem de personagens registrados.
- Edição de registros.
- Exclusão de personagens com confirmação.
- Pesquisa por nome.
- Contagem automática de personagens.
- Interface responsiva.

## 📁 Estrutura do projeto

```text
Anteiku-Archive/
├── static/
│   └── style.css
├── templates/
│   ├── editar.html
│   └── index.html
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Como executar o projeto

### 1. Pré-requisitos

- Python instalado.
- Git (opcional, para clonar o repositório).

### 2. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd Anteiku-Archive
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python app.py
```

### 5. Acessar o sistema

Abra o navegador e acesse:

```text
http://127.0.0.1:5000
```

O banco de dados SQLite será preparado automaticamente na primeira execução.

## 🎯 Objetivo

Este projeto foi desenvolvido com o objetivo de praticar conceitos de desenvolvimento web, operações CRUD, integração com banco de dados e construção de interfaces utilizando Flask e Python.

## 👨‍💻 Status

Primeira versão concluída. O projeto poderá receber novas funcionalidades e melhorias visuais em versões futuras.