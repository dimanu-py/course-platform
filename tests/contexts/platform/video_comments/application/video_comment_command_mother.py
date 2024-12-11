from src.contexts.platform.video_comments.application.video_comment_command import (
    VideoCommentCommand,
)
from tests.contexts.platform.students.domain.student_id_mother import StudentIdMother
from tests.contexts.platform.video_comments.domain.video_comment_content_mother import (
    VideoCommentContentMother,
)
from tests.contexts.platform.video_comments.domain.video_comment_id_mother import (
    VideoCommentIdMother,
)
from tests.contexts.platform.video_comments.domain.video_comment_title_mother import (
    VideoCommentTitleMother,
)
from tests.contexts.platform.videos.domain.video_id_mother import VideoIdMother


class VideoCommentCommandMother:
    @classmethod
    def with_valid_id(cls) -> VideoCommentCommand:
        return VideoCommentCommand(
            id=VideoCommentIdMother.create().value,
            video_id=VideoIdMother.create().value,
            author_id=StudentIdMother.create().value,
            title=VideoCommentTitleMother.create().value,
            content=VideoCommentContentMother.create().value,
        )
