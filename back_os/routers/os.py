from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from back_os.database import get_session
from back_os.models import Os, User
from back_os.schemas import OsSchema, OsList, OsPublic, Message
from back_os.security import get_current_user, get_password_hash

router = APIRouter(prefix='/os', tags=['os'])
T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]

@router.post('/', status_code=HTTPStatus.CREATED, response_model=OsSchema)
def create_os(os: OsSchema, session: T_Session, current_user: T_CurrentUser):
    """Criar nova OS"""
    db_os = Os(
        cliente=os.cliente,
        titulo=os.titulo,
        descricao=os.descricao,
        status='pendente'
    )

    session.add(db_os)
    session.commit()
    session.refresh(db_os)

    return db_os

@router.get('/', status_code=HTTPStatus.OK, response_model=OsList)
def listar_os(session: T_Session, current_user: T_CurrentUser):
    """Lista todas as OS"""
    ordens = session.scalars(select(Os))
    return {'ordens': ordens}

@router.put('/alterar/{os_id}', status_code=HTTPStatus.OK, response_model=OsPublic)
def alterar_os(session: T_Session, current_user: T_CurrentUser, os_id: int, os: OsSchema):
    db_os = session.query(Os).where(Os.id == os_id).first()
    if not db_os:
        raise HTTPException(status_code=404, detail='Os Não encontrada')
    db_os.cliente = os.cliente
    db_os.titulo = os.titulo
    db_os.descricao = os.descricao
    session.commit()
    session.refresh(db_os)

    return db_os

@router.put('/{os_id}', status_code=HTTPStatus.OK, response_model=OsPublic)
def alterar_status_os_concluida(session: T_Session, current_user: T_CurrentUser, os_id: int):
    db_os = session.query(Os).where(Os.id == os_id).first()
    if not db_os:
        raise HTTPException(status_code=404, detail='Os Não encontrada')
    db_os.status = 'concluida'
    session.commit()
    session.refresh(db_os)

    return db_os
    
