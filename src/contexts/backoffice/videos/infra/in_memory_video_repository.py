from src.contexts.backoffice.videos.domain.video import Video
from src.contexts.backoffice.videos.domain.video_id import VideoId
from src.contexts.backoffice.videos.domain.video_repository import VideoRepository


class InMemoryVideoRepository(VideoRepository):
    _videos: dict[str, Video]

    def __init__(self) -> None:
        self._videos = {}

    def save(self, video: Video) -> None:
        self._videos[video.id.value] = video

    def search(self, video_id: VideoId) -> Video | None:
        return self._videos.get(video_id.value)
