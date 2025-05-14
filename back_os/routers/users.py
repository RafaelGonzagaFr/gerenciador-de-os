from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from back_os.database import get_session
from back_os.models import User
from back_os.schemas import UserPublic, UserSchema
from back_os.security import get_current_user, get_password_hash

router = APIRouter(prefix='/users', tags=['users'])
T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: T_Session, current_user: T_CurrentUser):
    """Criar usuário"""
    if current_user.tipo == 'adm':
      db_user = session.scalar(
          select(User).where(
              (User.username == user.username)
          )
      )

      if db_user:
          if db_user.username == user.username:
              raise HTTPException(
                  status_code=HTTPStatus.BAD_REQUEST,
                  detail='Usuário já existe'
              )

      hashed_password = get_password_hash(user.password)

      db_user = User(
          username=user.username,
          password=hashed_password,
          tipo=user.tipo
      )

      session.add(db_user)
      session.commit()
      session.refresh(db_user)

      return db_user
    else:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Sem permissão para criar um usuário'
        )
