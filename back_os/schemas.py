from pydantic import BaseModel, ConfigDict

from back_os.models import TipoDeUsuario, StatusDaOs


class Token(BaseModel):
    access_token: str
    token_type: str

class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    password: str
    tipo: TipoDeUsuario


class UserPublic(BaseModel):
    id: int
    username: str
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]

class OsSchema(BaseModel):
    cliente: str
    titulo: str
    descricao: str

class OsPublic(OsSchema):
    id: int
    status: StatusDaOs
    model_config = ConfigDict(from_attributes=True)

class OsList(BaseModel):
    ordens: list[OsPublic]
