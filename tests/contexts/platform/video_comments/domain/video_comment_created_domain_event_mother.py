from src.contexts.platform.video_comments.domain.video_comment_created_domain_event import (
    VideoCommentCreatedDomainEvent,
)
from tests.contexts.platform.students.domain.student_id_mother import StudentIdMother
from tests.contexts.platform.video_comments.domain.video_comment_id_mother import (
    VideoCommentIdMother,
)
from tests.contexts.platform.video_comments.domain.video_comment_title_mother import (
    VideoCommentTitleMother,
)
from tests.contexts.platform.videos.domain.video_id_mother import VideoIdMother


class VideoCommentCreatedDomainEventMother:
    @classmethod
    def create(cls, params: dict | None = None) -> VideoCommentCreatedDomainEvent:
        primitives = {
            "id": VideoCommentIdMother.create().value,
            "video_id": VideoIdMother.create().value,
            "author_id": StudentIdMother.create().value,
            "title": VideoCommentTitleMother.create().value,
            "content": VideoCommentTitleMother.create().value,
            **(params if params else {}),
        }

        return VideoCommentCreatedDomainEvent(**primitives)
