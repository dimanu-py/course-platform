from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.contexts.platform.shared.infra.persistence.sqlalchemy.base import (
    Base,
)
from src.contexts.platform.videos.domain.video import Video


class VideoModel(Base):
    __tablename__ = "videos"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    def to_aggregate(self) -> Video:
        return Video.from_primitives(
            id_=str(self.id),
            title=self.title,
            description=self.description,
        )
