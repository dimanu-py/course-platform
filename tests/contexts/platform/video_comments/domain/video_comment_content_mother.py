from src.contexts.platform.video_comments.domain.video_comment_content import (
    VideoCommentContent,
)
from tests.contexts.shared.domain.random_generator import RandomGenerator


class VideoCommentContentMother:
    @classmethod
    def create(cls) -> VideoCommentContent:
        return VideoCommentContent(RandomGenerator.sentence())
