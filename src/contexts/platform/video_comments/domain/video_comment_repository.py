from abc import ABC, abstractmethod

from src.contexts.platform.video_comments.domain.video_comment import VideoComment


class VideoCommentRepository(ABC):
    @abstractmethod
    def save(self, comment: VideoComment) -> None:
        raise NotImplementedError
