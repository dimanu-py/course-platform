from src.contexts.content_creation.videos.application.create_video_command import (
    CreateVideoCommand,
)
from src.contexts.content_creation.videos.domain.video import Video
from tests.contexts.content_creation.videos.domain.video_description_mother import (
    VideoDescriptionMother,
)
from tests.contexts.content_creation.videos.domain.video_id_mother import VideoIdMother
from tests.contexts.content_creation.videos.domain.video_title_mother import (
    VideoTitleMother,
)


class VideoMother:
    @classmethod
    def from_request(cls, command: CreateVideoCommand) -> Video:
        return Video.create(command.id, command.title, command.description)

    @classmethod
    def create(cls) -> Video:
        return Video(
            VideoIdMother.create(),
            VideoTitleMother.create(),
            VideoDescriptionMother.create(),
        )
