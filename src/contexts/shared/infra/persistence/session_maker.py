from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.contexts.shared.infra.persistence.sqlalchemy.postgres_base import (
    PostgresBase,
)


class SessionMaker:
    def __init__(self, url: str) -> None:
        self._engine = create_engine(url)
        self._session_maker = sessionmaker(bind=self._engine)

    def get_session(self) -> Session:
        return self._session_maker()

    def close_session(self) -> None:
        self._engine.dispose()

    def create_tables(self) -> None:
        PostgresBase.metadata.create_all(self._engine)

    def drop_tables(self) -> None:
        PostgresBase.metadata.drop_all(self._engine)
