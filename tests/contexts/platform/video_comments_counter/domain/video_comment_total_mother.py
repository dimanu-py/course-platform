from src.contexts.platform.video_comments_counter.domain.video_comment_total import (
    VideoCommentTotal,
)
from tests.contexts.shared.domain.random_generator import RandomGenerator


class VideoCommentTotalMother:
    @classmethod
    def create(cls) -> VideoCommentTotal:
        return VideoCommentTotal(RandomGenerator.number())
