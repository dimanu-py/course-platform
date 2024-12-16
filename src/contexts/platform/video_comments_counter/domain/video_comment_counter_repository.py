from abc import ABC, abstractmethod

from src.contexts.platform.video_comments_counter.domain.video_comment_counter import (
    VideoCommentCounter,
)
from src.contexts.platform.videos.domain.video_id import VideoId


class VideoCommentCounterRepository(ABC):
    @abstractmethod
    def save(self, counter: VideoCommentCounter) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(self, video_id: VideoId) -> VideoCommentCounter:
        raise NotImplementedError
