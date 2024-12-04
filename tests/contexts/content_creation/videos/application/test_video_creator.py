from expects import expect, raise_error

from tests.contexts.content_creation.videos.application.create_video_command_mother import (
    CreateVideoCommandMother,
)
from tests.contexts.content_creation.videos.domain.video_mother import VideoMother
from tests.contexts.content_creation.videos.video_module_unit_test_config import (
    VideoModuleUnitTestConfig,
)


class TestVideoCreator(VideoModuleUnitTestConfig):
    def test_should_create_a_valid_video(self) -> None:
        command = CreateVideoCommandMother.with_valid_id()
        video_to_save = VideoMother.from_request(command)

        self.video_creator(command)

        self.should_have_saved(video_to_save)

    def test_should_fail_to_create_video_with_invalid_id(self) -> None:
        command = CreateVideoCommandMother.with_invalid_id()

        expect(lambda: self.video_creator(command)).to(raise_error(ValueError))
