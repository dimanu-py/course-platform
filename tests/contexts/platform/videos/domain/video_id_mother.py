from src.contexts.platform.videos.domain.video_id import VideoId
from tests.contexts.shared.domain.random_generator import RandomGenerator


class VideoIdMother:
    @classmethod
    def create(cls, value: str | None = None) -> VideoId:
        return VideoId(value if value else RandomGenerator.uuid())
