import pytest

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_event_bus import (
    RabbitMqEventBus,
)
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_settings import (
    RabbitMqSettings,
)
from tests.contexts.platform.video_comments.domain.video_comment_created_domain_event_mother import (
    VideoCommentCreatedDomainEventMother,
)
from tests.delivery.api.acceptance_test_config import AcceptanceTestConfig


class TestVideoCommentsCounterRoute(AcceptanceTestConfig):
    def setup_method(self) -> None:
        super().setup_method()
        self.event_bus = RabbitMqEventBus(
            client=RabbitMqConnection(
                connection_settings=RabbitMqSettings(
                    user="admin", password="admin", host="localhost"
                )
            ),
            exchange_name="domain_events",
        )

    @pytest.mark.xfail
    def test_should_get_comments_counter(self) -> None:
        event = VideoCommentCreatedDomainEventMother.create()
        self.given_a_event_is_published([event])

        response = self.when_a_get_request_is_made_to(
            f"/comments_counter/{event.video_id}"
        )

        self.then_response_should_satisfy(200, {"total_comments": 1}, response)

    def given_a_event_is_published(self, events: list[DomainEvent]) -> None:
        self.event_bus.publish(events)
