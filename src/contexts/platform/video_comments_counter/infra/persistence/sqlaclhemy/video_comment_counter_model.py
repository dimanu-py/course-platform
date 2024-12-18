from sqlalchemy import UUID, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.contexts.platform.shared.infra.persistence.sqlalchemy.base import Base
from src.contexts.platform.video_comments_counter.domain.video_comment_counter import (
    VideoCommentCounter,
)


class VideoCommentCounterModel(Base):
    __tablename__ = "video_comments_counters"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    video_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    comments_count: Mapped[int] = mapped_column(Integer, nullable=False)

    def to_aggregate(self) -> VideoCommentCounter:
        return VideoCommentCounter.from_primitives(
            id_=str(self.id),
            video_id=str(self.video_id),
            comments_count=self.comments_count,
        )
