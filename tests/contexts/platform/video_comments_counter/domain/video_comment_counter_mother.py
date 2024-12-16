from src.contexts.platform.video_comments_counter.domain.video_comment_counter import (
    VideoCommentCounter,
)
from tests.contexts.platform.video_comments_counter.domain.video_comment_counter_id_mother import (
    VideoCommentCounterIdMother,
)
from tests.contexts.platform.video_comments_counter.domain.video_comment_total_mother import (
    VideoCommentTotalMother,
)
from tests.contexts.platform.videos.domain.video_id_mother import VideoIdMother


class VideoCommentCounterMother:
    @classmethod
    def create(cls, video_id: str | None = None) -> VideoCommentCounter:
        return VideoCommentCounter(
            id_=VideoCommentCounterIdMother.create(),
            video_id=VideoIdMother.create(video_id),
            number_comments=VideoCommentTotalMother.create(),
        )
