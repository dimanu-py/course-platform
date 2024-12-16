from src.contexts.platform.video_comments_counter.domain.video_comment_counter_repository import (
    VideoCommentCounterRepository,
)
from src.contexts.platform.videos.domain.video_id import VideoId


class CommentsCounterIncrementer:
    _repository: VideoCommentCounterRepository

    def __init__(self, repository: VideoCommentCounterRepository) -> None:
        self._repository = repository

    def __call__(self, video_id: str) -> None:
        counter = self._repository.search(VideoId(video_id))
        counter.increment()
        self._repository.save(counter)
