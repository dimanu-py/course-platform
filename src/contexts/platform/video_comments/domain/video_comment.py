from typing import override

from src.contexts.platform.shared.domain.aggregate_root import AggregateRoot
from src.contexts.platform.students.domain.student_id import StudentId
from src.contexts.platform.video_comments.domain.video_comment_content import VideoCommentContent
from src.contexts.platform.video_comments.domain.video_comment_created_domain_event import (
    VideoCommentCreatedDomainEvent,
)
from src.contexts.platform.video_comments.domain.video_comment_id import VideoCommentId
from src.contexts.platform.video_comments.domain.video_comment_title import (
    VideoCommentTitle,
)
from src.contexts.platform.videos.domain.video_id import VideoId


class VideoComment(AggregateRoot):
    _content: VideoCommentContent
    _title: VideoCommentTitle
    _author_id: StudentId
    _video_id: VideoId
    _id: VideoCommentId

    def __init__(
        self,
        id_: VideoCommentId,
        video_id: VideoId,
        author_id: StudentId,
        title: VideoCommentTitle,
        content: VideoCommentContent,
    ) -> None:
        super().__init__()
        self._id = id_
        self._video_id = video_id
        self._author_id = author_id
        self._title = title
        self._content = content

    @classmethod
    def create(
        cls, id_: str, video_id: str, author_id: str, title: str, content: str
    ) -> "VideoComment":
        video_comment = VideoComment(
            id_=VideoCommentId(id_),
            video_id=VideoId(video_id),
            author_id=StudentId(author_id),
            title=VideoCommentTitle(title),
            content=VideoCommentContent(content),
        )

        video_comment.record(
            VideoCommentCreatedDomainEvent(
                id=id_,
                video_id=video_id,
                author_id=author_id,
                title=title,
                content=content,
            )
        )

        return video_comment

    @override
    def __eq__(self, other: "VideoComment") -> bool:
        return self._id == other._id

    @property
    def id(self) -> VideoCommentId:
        return self._id

    def to_dict(self) -> dict:
        return {
            "id": self._id.value,
            "video_id": self._video_id.value,
            "author_id": self._author_id.value,
            "title": self._title.value,
            "content": self._content.value,
        }
