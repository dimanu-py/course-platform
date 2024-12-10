from src.contexts.platform.videos.domain.video import Video
from src.contexts.platform.videos.domain.video_created_domain_event import (
    VideoCreatedDomainEvent,
)


class VideoCreatedDomainEventMother:
    @classmethod
    def from_video(cls, video: Video) -> VideoCreatedDomainEvent:
        return VideoCreatedDomainEvent(**video.to_dict())
