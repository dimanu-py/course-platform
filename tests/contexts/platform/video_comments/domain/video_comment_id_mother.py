from src.contexts.platform.video_comments.domain.video_comment_id import VideoCommentId
from tests.contexts.shared.domain.random_generator import RandomGenerator


class VideoCommentIdMother:
    @classmethod
    def create(cls) -> VideoCommentId:
        return VideoCommentId(RandomGenerator.uuid())
