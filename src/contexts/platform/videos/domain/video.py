from typing import override

from src.contexts.platform.shared.domain.aggregate_root import AggregateRoot
from src.contexts.platform.videos.domain.video_created_domain_event import (
    VideoCreatedDomainEvent,
)
from src.contexts.platform.videos.domain.video_description import (
    VideoDescription,
)
from src.contexts.platform.videos.domain.video_id import VideoId
from src.contexts.platform.videos.domain.video_title import VideoTitle


class Video(AggregateRoot):
    _id: VideoId
    _title: VideoTitle
    _description: VideoDescription

    def __init__(
        self,
        id_: VideoId,
        title: VideoTitle,
        description: VideoDescription,
    ) -> None:
        super().__init__()
        self._description = description
        self._title = title
        self._id = id_

    @classmethod
    def create(cls, id_: str, title: str, description: str) -> "Video":
        video = Video(
            id_=VideoId(id_),
            title=VideoTitle(title),
            description=VideoDescription(description),
        )

        video.record(
            VideoCreatedDomainEvent(id=id_, title=title, description=description)
        )

        return video

    @classmethod
    def from_primitives(cls, id_: str, title: str, description: str) -> "Video":
        return Video(
            id_=VideoId(id_),
            title=VideoTitle(title),
            description=VideoDescription(description),
        )

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
