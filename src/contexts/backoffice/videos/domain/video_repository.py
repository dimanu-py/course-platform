from src.contexts.backoffice.videos.domain.video import Video


class VideoRepository:
    def save(self, video: Video) -> None:
        raise NotImplementedError
