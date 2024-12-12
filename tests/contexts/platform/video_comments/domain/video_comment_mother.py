from src.contexts.platform.video_comments.application.create.video_comment_command import (
    VideoCommentCommand,
)
from src.contexts.platform.video_comments.domain.video_comment import VideoComment


class VideoCommentMother:
    @classmethod
    def from_request(cls, command: VideoCommentCommand) -> VideoComment:
        return VideoComment.create(
            id_=command.id,
            video_id=command.video_id,
            author_id=command.author_id,
            title=command.title,
            content=command.content,
        )
