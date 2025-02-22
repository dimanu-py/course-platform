from typing import override

from src.contexts.platform.video_comments_counter.domain.video_comment_counter_id import (
    VideoCommentCounterId,
)
from src.contexts.platform.video_comments_counter.domain.video_comment_total import (
    VideoCommentTotal,
)
from src.contexts.platform.videos.domain.video_id import VideoId


class VideoCommentCounter:
    _number_comments: VideoCommentTotal
    _video_id: VideoId
    _id: VideoCommentCounterId

    def __init__(
        self,
        id_: VideoCommentCounterId,
        video_id: VideoId,
        number_comments: VideoCommentTotal,
    ) -> None:
        self._id = id_
        self._video_id = video_id
        self._number_comments = number_comments

    @classmethod
    def initialize(cls, video_id: str) -> "VideoCommentCounter":
        return VideoCommentCounter(
            video_id=VideoId(video_id),
            id_=VideoCommentCounterId.generate(),
            number_comments=VideoCommentTotal.initialize(),
        )

    @classmethod
    def from_primitives(
        cls, id_: str, video_id: str, comments_count: int
    ) -> "VideoCommentCounter":
        return VideoCommentCounter(
            id_=VideoCommentCounterId(id_),
            video_id=VideoId(video_id),
            number_comments=VideoCommentTotal(comments_count),
        )

    @override
    def __eq__(self, other: "VideoCommentCounter") -> bool:
        return self._id == other._id

    @property
    def id(self) -> VideoCommentCounterId:
        return self._id

    @property
    def video_id(self) -> VideoId:
        return self._video_id

    @property
    def number_comments(self) -> VideoCommentTotal:
        return self._number_comments

    def increment(self) -> None:
        self._number_comments = self._number_comments.increment()

    def to_dict(self) -> dict:
        return {
            "id": self._id.value,
            "video_id": self._video_id.value,
            "comments_count": self._number_comments.value,
        }
