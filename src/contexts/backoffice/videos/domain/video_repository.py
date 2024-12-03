from abc import ABC, abstractmethod

from src.contexts.backoffice.videos.domain.video import Video
from src.contexts.backoffice.videos.domain.video_id import VideoId


class VideoRepository(ABC):
    @abstractmethod
    def save(self, video: Video) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(self, video_id: VideoId) -> Video | None:
        raise NotImplementedError
