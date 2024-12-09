from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.contexts.content_creation.influencers.domain.influencer import Influencer
from src.contexts.content_creation.shared.infra.sqlalchemy.postgres_base import (
    PostgresBase,
)


class InfluencerModel(PostgresBase):
    __tablename__ = "influencers"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String, nullable=False)

    def to_aggregate(self) -> Influencer:
        return Influencer.create(
            str(self.id),
            self.name,
            self.username,
            self.email,
        )
