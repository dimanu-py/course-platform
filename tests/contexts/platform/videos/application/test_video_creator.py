from expects import expect, raise_error

from src.contexts.platform.videos.application.video_creator import VideoCreator
from tests.contexts.platform.videos.application.create_video_command_mother import (
    CreateVideoCommandMother,
)
from tests.contexts.platform.videos.domain.video_created_domain_event_mother import (
    VideoCreatedDomainEventMother,
)
from tests.contexts.platform.videos.domain.video_mother import VideoMother
from tests.contexts.platform.videos.video_module_unit_test_config import (
    VideoModuleUnitTestConfig,
)


class TestVideoCreator(VideoModuleUnitTestConfig):
    def setup_method(self) -> None:
        self.video_creator = VideoCreator(self.repository, self.event_bus)

    def test_should_create_a_valid_video(self) -> None:
        command = CreateVideoCommandMother.with_valid_id()
        video_to_save = VideoMother.from_request(command)
        domain_event = VideoCreatedDomainEventMother.create(video_to_save.to_dict())

        self.video_creator(command)

        self.should_have_saved(video_to_save)
        self.should_have_published([domain_event])

    def test_should_fail_to_create_video_with_invalid_id(self) -> None:
        command = CreateVideoCommandMother.with_invalid_id()

        expect(lambda: self.video_creator(command)).to(raise_error(ValueError))
