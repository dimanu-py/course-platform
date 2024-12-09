from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.contexts.content_creation.shared.infra.sqlalchemy.postgres_base import (
    PostgresBase,
)
from src.contexts.content_creation.videos.domain.video import Video


class VideoModel(PostgresBase):
    __tablename__ = "videos"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    def to_aggregate(self) -> Video:
        return Video.create(
            str(self.id),
            self.title,
            self.description,
        )
