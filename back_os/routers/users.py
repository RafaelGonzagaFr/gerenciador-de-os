from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from back_os.database import get_session
from back_os.models import User
from back_os.schemas import Message, UserList, UserPublic, UserSchema
from back_os.security import get_current_user, get_password_hash

router = APIRouter(prefix='/users', tags['users'])
T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]