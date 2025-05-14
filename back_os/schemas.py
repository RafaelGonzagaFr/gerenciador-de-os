from pydantic import BaseModel, ConfigDict

from back_os.models import TipoDeUsuario


class Token(BaseModel):
    access_token: str
    token_type: str


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
