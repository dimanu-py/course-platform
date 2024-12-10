from src.contexts.platform.videos.application.create_video_command import (
    CreateVideoCommand,
)
from src.contexts.platform.shared.domain.event.event_bus import EventBus
from src.contexts.platform.videos.domain.video import Video
from src.contexts.platform.videos.domain.video_repository import VideoRepository


class VideoCreator:
    _event_bus: EventBus
    _repository: VideoRepository

    def __init__(self, repository: VideoRepository, event_bus: EventBus) -> None:
        self._event_bus = event_bus
        self._repository = repository

    def __call__(self, command: CreateVideoCommand) -> None:
        video = Video.create(
            id_=command.id, title=command.title, description=command.description
        )
        self._repository.save(video)
        self._event_bus.publish(video.pull_domain_events())
