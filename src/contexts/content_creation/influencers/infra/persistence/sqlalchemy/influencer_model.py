from sqlalchemy import Column, UUID, String

from src.contexts.content_creation.shared.infra.sqlalchemy.postgres_base import (
    PostgresBase,
)


class InfluencerModel(PostgresBase):
    __tablename__ = "influencers"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)
