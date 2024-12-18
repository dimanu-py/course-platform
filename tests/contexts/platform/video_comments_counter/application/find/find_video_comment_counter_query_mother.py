from src.contexts.platform.video_comments_counter.application.find.find_video_comment_counter_query import (
    FindVideoCommentCounterQuery,
)
from tests.contexts.platform.videos.domain.video_id_mother import VideoIdMother


class FindVideoCommentCounterQueryMother:
    @classmethod
    def create(cls) -> FindVideoCommentCounterQuery:
        return FindVideoCommentCounterQuery(video_id=VideoIdMother.create().value)
