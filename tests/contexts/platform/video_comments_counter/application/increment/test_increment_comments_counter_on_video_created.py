from src.contexts.platform.video_comments_counter.application.increment.comments_counter_incrementer import (
    CommentsCounterIncrementer,
)
from src.contexts.platform.video_comments_counter.application.increment.increment_comments_counter_on_video_comment_created import (
    IncrementCommentsCounterOnVideoCommentCreated,
)
from tests.contexts.platform.video_comments.domain.video_comment_created_domain_event_mother import (
    VideoCommentCreatedDomainEventMother,
)
from tests.contexts.platform.video_comments_counter.domain.video_comment_counter_mother import (
    VideoCommentCounterMother,
)
from tests.contexts.platform.video_comments_counter.video_comment_counter_module_unit_test_config import (
    VideoCommentCounterModuleUnitTestConfig,
)


class TestIncrementNumberCommentsOnVideoCreated(
    VideoCommentCounterModuleUnitTestConfig
):
    def setup_method(self) -> None:
        self.incrementer = CommentsCounterIncrementer(repository=self.repository)
        self.subscriber = IncrementCommentsCounterOnVideoCommentCreated(
            incrementer=self.incrementer
        )

    def test_should_increment_video_comment_counter_on_video_comment_created(
        self,
    ) -> None:
        event = VideoCommentCreatedDomainEventMother.create()
        counter = VideoCommentCounterMother.create(video_id=event.video_id)
        self.should_search(counter)
        self.should_save(counter)

        self.subscriber.on(event)

        self.should_have_saved()
