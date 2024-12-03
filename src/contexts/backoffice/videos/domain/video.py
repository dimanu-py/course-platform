from typing import override

from src.contexts.backoffice.videos.domain.video_description import VideoDescription
from src.contexts.backoffice.videos.domain.video_id import VideoId
from src.contexts.backoffice.videos.domain.video_title import VideoTitle


class Video:
    id: VideoId
    title: VideoTitle
    description: VideoDescription

    def __init__(
        self,
        id: VideoId,
        title: VideoTitle,
        description: VideoDescription,
    ) -> None:
        self.description = description
        self.title = title
        self.id = id

    @classmethod
    def create(cls, id: str, title: str, description: str) -> "Video":
        video_id = VideoId(id)
        video_title = VideoTitle(title)
        video_description = VideoDescription(description)
        return Video(video_id, video_title, video_description)

    @override
    def __eq__(self, other: "Video") -> bool:
        return self.id == other.id
