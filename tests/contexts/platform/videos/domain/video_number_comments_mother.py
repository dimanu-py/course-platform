from src.contexts.platform.videos.domain.video_number_comments import (
    VideoNumberComments,
)
from tests.contexts.shared.domain.random_generator import RandomGenerator


class VideoNumberCommentsMother:
    @classmethod
    def create(cls) -> VideoNumberComments:
        return VideoNumberComments(RandomGenerator.number())
