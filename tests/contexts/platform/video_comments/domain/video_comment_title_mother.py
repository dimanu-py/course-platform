from src.contexts.platform.video_comments.domain.video_comment_title import (
    VideoCommentTitle,
)
from tests.contexts.shared.domain.random_generator import RandomGenerator


class VideoCommentTitleMother:
    @classmethod
    def create(cls) -> VideoCommentTitle:
        return VideoCommentTitle(RandomGenerator.word())
