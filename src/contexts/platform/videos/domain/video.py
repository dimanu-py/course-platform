from typing import override

from src.contexts.platform.videos.domain.video_description import (
    VideoDescription,
)
from src.contexts.platform.videos.domain.video_id import VideoId
from src.contexts.platform.videos.domain.video_title import VideoTitle


class Video:
    _id: VideoId
    _title: VideoTitle
    _description: VideoDescription

    def __init__(
        self,
        id_: VideoId,
        title: VideoTitle,
        description: VideoDescription,
    ) -> None:
        self._description = description
        self._title = title
        self._id = id_

    @classmethod
    def create(cls, id_: str, title: str, description: str) -> "Video":
        video_id = VideoId(id_)
        video_title = VideoTitle(title)
        video_description = VideoDescription(description)
        return Video(video_id, video_title, video_description)

    @override
    def __eq__(self, other: "Video") -> bool:
        return self.id == other.id

    @property
    def id(self) -> VideoId:
        return self._id

    def to_dict(self) -> dict:
        return {
            "id": self._id.value,
            "title": self._title.value,
            "description": self._description.value,
        }
