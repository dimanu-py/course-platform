from src.contexts.content_creation.videos.domain.video_title import VideoTitle
from tests.contexts.shared.domain.random_generator import RandomGenerator


class VideoTitleMother:
    @classmethod
    def create(cls) -> VideoTitle:
        return VideoTitle(RandomGenerator.word())
