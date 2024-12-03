import pytest
from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect, raise_error

from src.contexts.backoffice.videos.application.video_creator import VideoCreator
from src.contexts.backoffice.videos.domain.video_repository import VideoRepository
from tests.contexts.backoffice.videos.application.create_video_command_mother import (
    CreateVideoCommandMother,
)
from tests.contexts.backoffice.videos.domain.video_mother import VideoMother


@pytest.mark.unit
class TestVideoCreator:
    def setup_method(self) -> None:
        self.repository = Spy(VideoRepository)
        self.video_creator = VideoCreator(self.repository)

    def test_should_create_a_valid_video(self) -> None:
        command = CreateVideoCommandMother.with_valid_id()
        video_to_save = VideoMother.from_request(command)

        self.video_creator(command)

        expect(self.repository.save).to(have_been_called_with(video_to_save))

    def test_should_fail_to_create_video_with_invalid_id(self) -> None:
        command = CreateVideoCommandMother.with_invalid_id()

        expect(lambda: self.video_creator(command)).to(raise_error(ValueError))
