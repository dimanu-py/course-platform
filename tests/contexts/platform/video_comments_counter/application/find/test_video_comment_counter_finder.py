from expects import expect, equal

from src.contexts.platform.video_comments_counter.application.find.video_comment_counter_finder import (
    VideoCommentCounterFinder,
)
from tests.contexts.platform.video_comments_counter.application.find.find_video_comment_counter_query_mother import (
    FindVideoCommentCounterQueryMother,
)
from tests.contexts.platform.video_comments_counter.domain.video_comment_counter_mother import (
    VideoCommentCounterMother,
)
from tests.contexts.platform.video_comments_counter.video_comment_counter_module_unit_test_config import (
    VideoCommentCounterModuleUnitTestConfig,
)


class TestVideoCommentCounterFinder(VideoCommentCounterModuleUnitTestConfig):
    def setup_method(self) -> None:
        self.video_comment_counter_finder = VideoCommentCounterFinder(self.repository)

    def test_should_find_existing_video_comment_counter(self) -> None:
        query = FindVideoCommentCounterQueryMother.create()
        video_comment_counter_found = VideoCommentCounterMother.create(query.video_id)
        self.should_search(video_comment_counter_found)

        number_comments = self.video_comment_counter_finder(query)

        expect(number_comments).to(
            equal(video_comment_counter_found.number_comments.value)
        )
