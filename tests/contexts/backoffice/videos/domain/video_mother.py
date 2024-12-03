from src.contexts.backoffice.videos.application.create_video_command import (
    CreateVideoCommand,
)
from src.contexts.backoffice.videos.domain.video import Video


class VideoMother:
    @classmethod
    def from_request(cls, command: CreateVideoCommand) -> Video:
        return Video(command.id, command.title, command.description, command.duration)
