from abc import ABC, abstractmethod

from src.contexts.backoffice.videos.domain.video import Video


class VideoRepository(ABC):
    @abstractmethod
    def save(self, video: Video) -> None:
        raise NotImplementedError
