from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.contexts.content_creation.shared.infra.sqlalchemy.base import (
    Base,
)


class SessionMaker:
    def __init__(self, url: str) -> None:
        self._engine = create_engine(url)
        self._session_maker = sessionmaker(bind=self._engine)

    def get_session(self) -> Session:
        return self._session_maker()

    def create_tables(self) -> None:
        Base.metadata.create_all(self._engine)
