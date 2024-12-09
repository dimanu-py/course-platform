from src.contexts.content_creation.shared.infra.sqlalchemy.postgres_base import (
    PostgresBase,
)

from sqlalchemy import Column, UUID, String


class VideoModel(PostgresBase):
    __tablename__ = "videos"

    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
