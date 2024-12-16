from src.contexts.platform.video_comments_counter.domain.video_comment_counter_id import (
    VideoCommentCounterId,
)


class VideoCommentCounterIdMother:
    @classmethod
    def create(cls) -> VideoCommentCounterId:
        return VideoCommentCounterId.generate()
