from src.contexts.content_creation.videos.domain.video_description import (
    VideoDescription,
)
from tests.contexts.shared.domain.random_generator import RandomGenerator


class VideoDescriptionMother:
    @classmethod
    def create(cls) -> VideoDescription:
        return VideoDescription(RandomGenerator.sentence())
