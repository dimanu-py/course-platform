from src.contexts.platform.video_comments.application.video_comment_command import (
    VideoCommentCommand,
)
from src.contexts.platform.video_comments.domain.video_comment import VideoComment
from src.contexts.platform.video_comments.domain.video_comment_repository import (
    VideoCommentRepository,
)


class VideoCommenter:
    _repository: VideoCommentRepository

    def __init__(self, repository: VideoCommentRepository) -> None:
        self._repository = repository

    def __call__(self, command: VideoCommentCommand) -> None:
        video_comment = VideoComment.create(
            id_=command.id,
            video_id=command.video_id,
            author_id=command.author_id,
            title=command.title,
            content=command.content,
        )

        self._repository.save(video_comment)
