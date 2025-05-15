from datetime import datetime
from enum import Enum

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


class TipoDeUsuario(str, Enum):
    adm = 'adm'
    tecnico = 'tecnico'

class StatusDaOs(str, Enum):
    pendente = 'pendente'
    concluida = 'concluida'


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    tipo: Mapped[TipoDeUsuario]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False,
        onupdate=func.now(),
        nullable=True,
        server_default=func.now(),
    )

@table_registry.mapped_as_dataclass
class Os:
    __tablename__ = 'os'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    cliente: Mapped[str]
    titulo: Mapped[str]
    descricao: Mapped[str]
    status: Mapped[StatusDaOs]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False,
        onupdate=func.now(),
        nullable=True,
        server_default=func.now(),
    )