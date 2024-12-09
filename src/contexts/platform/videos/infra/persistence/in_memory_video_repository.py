from typing import override

from src.contexts.platform.videos.domain.video import Video
from src.contexts.platform.videos.domain.video_id import VideoId
from src.contexts.platform.videos.domain.video_repository import VideoRepository


class InMemoryVideoRepository(VideoRepository):
    _videos: dict[str, Video]

    def __init__(self) -> None:
        self._videos = {}

    @override
    def save(self, video: Video) -> None:
        self._videos[video.id.value] = video

    @override
    def search(self, video_id: VideoId) -> Video | None:
        return self._videos.get(video_id.value)
