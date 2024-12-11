from src.contexts.platform.videos.domain.video_created_domain_event import (
    VideoCreatedDomainEvent,
)
from tests.contexts.platform.videos.domain.video_description_mother import (
    VideoDescriptionMother,
)
from tests.contexts.platform.videos.domain.video_id_mother import VideoIdMother
from tests.contexts.platform.videos.domain.video_title_mother import VideoTitleMother


class VideoCreatedDomainEventMother:
    @classmethod
    def create(cls, params: dict | None = None) -> VideoCreatedDomainEvent:
        primitives = {
            "id": VideoIdMother.create().value,
            "title": VideoTitleMother.create().value,
            "description": VideoDescriptionMother.create().value,
            **(params if params else {}),
        }

        return VideoCreatedDomainEvent(**primitives)
