from src.contexts.backoffice.videos.domain.video_id import VideoId
from tests.contexts.shared.domain.random_generator import RandomGenerator


class VideoIdMother:
    @classmethod
    def create(cls) -> VideoId:
        return VideoId(RandomGenerator.uuid())
