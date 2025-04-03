from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True



'''
UserBase → Modelo base com username e email.

UserCreate → Herda UserBase e adiciona password (usado para criação de usuário).

UserOut → Herda UserBase e adiciona id (usado para retorno de dados).

Config.orm_mode = True → Permite que os modelos aceitem objetos do SQLAlchemy.

🔹 Pydantic é usado para validação de dados, não para criar tabelas no banco.
'''