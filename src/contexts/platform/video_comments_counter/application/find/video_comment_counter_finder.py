from src.contexts.platform.video_comments_counter.application.find.find_video_comment_counter_query import (
    FindVideoCommentCounterQuery,
)
from src.contexts.platform.video_comments_counter.domain.video_comment_counter import (
    VideoCommentCounter,
)
from src.contexts.platform.video_comments_counter.domain.video_comment_counter_repository import (
    VideoCommentCounterRepository,
)
from src.contexts.platform.videos.domain.video_id import VideoId


class VideoCommentCounterFinder:
    def __init__(self, repository: VideoCommentCounterRepository) -> None:
        self._repository = repository

    def __call__(self, query: FindVideoCommentCounterQuery) -> int:
        counter = self._repository.search(VideoId(query.video_id))
        if not counter:
            counter = VideoCommentCounter.initialize(video_id=query.video_id)
        return counter.number_comments.value
