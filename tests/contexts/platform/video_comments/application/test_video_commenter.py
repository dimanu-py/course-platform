from src.contexts.platform.video_comments.application.video_commenter import (
    VideoCommenter,
)
from tests.contexts.platform.video_comments.application.video_comment_command_mother import (
    VideoCommentCommandMother,
)
from tests.contexts.platform.video_comments.domain.video_comment_created_domain_event_mother import (
    VideoCommentCreatedDomainEventMother,
)
from tests.contexts.platform.video_comments.domain.video_comment_mother import (
    VideoCommentMother,
)
from tests.contexts.platform.video_comments.video_comment_module_unit_test_config import (
    VideoCommentModuleUnitTestConfig,
)


class TestVideoCommenter(VideoCommentModuleUnitTestConfig):
    def setup_method(self) -> None:
        self.video_commenter = VideoCommenter(
            repository=self.repository, event_bus=self.event_bus
        )

    def test_should_create_a_comment(self) -> None:
        command = VideoCommentCommandMother.with_valid_id()
        video_comment = VideoCommentMother.from_request(command)
        video_comment_created_event = VideoCommentCreatedDomainEventMother.create(
            video_comment.to_dict()
        )

        self.video_commenter(command)

        self.should_have_saved(video_comment)
        self.should_have_published([video_comment_created_event])
