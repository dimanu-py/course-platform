from src.contexts.platform.videos.application.create.create_video_command import (
    CreateVideoCommand,
)
from src.contexts.platform.videos.domain.video import Video
from tests.contexts.platform.videos.domain.video_description_mother import (
    VideoDescriptionMother,
)
from tests.contexts.platform.videos.domain.video_id_mother import VideoIdMother
from tests.contexts.platform.videos.domain.video_title_mother import (
    VideoTitleMother,
)


class VideoMother:
    @classmethod
    def from_request(cls, command: CreateVideoCommand) -> Video:
        return Video.from_primitives(
            id_=command.id, title=command.title, description=command.description
        )

    @classmethod
    def create(cls) -> Video:
        return Video(
            id_=VideoIdMother.create(),
            title=VideoTitleMother.create(),
            description=VideoDescriptionMother.create(),
        )
