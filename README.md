# Authentication API

This api was created for auth users, allowing acessing, login creation, and information managment by the users. Also with different level permissions, like common user or ADM.


# Functionalities

## Authentication and Security
    - Creat new user login
    - Login with JWT
    - Rollback password by email
    - Acess allows based in lawers


## User Managment
    - Data upgrade from user profile (name, email and password)
    - Users list only for showed for ADM users
    - Delete accounts (ADM)

## Project Stack
    - Framework used FastAPI
    - SQLALchemy (DB managent)
    - SQLite or PostgreSQL (DB)
    - JWT (PyJWT)
    - Passlib for hash
    - Emails with SMTP or any third part service

## Project Folders Schema
**fastapi-auth/**
    **main.py**           # Arquivo principal da API
    **database.py**       # Conexão com o banco de dados
    **models.py**         # Definição das tabelas do banco
    **schemas.py**        # Definição dos modelos de dados (Pydantic)
    **crud.py**           # Funções para operações no banco de dados
    **auth.py**           # Lógica de autenticação (JWT)
    **dependencies.py**   # Dependências reutilizáveis
    **config.py**         # Configurações gerais
    **requirements.txt**  # Dependências do projeto
