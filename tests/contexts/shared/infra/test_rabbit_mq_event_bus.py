from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_event_bus import (
    RabbitMqEventBus,
)
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_settings import (
    RabbitMqSettings,
)
from tests.contexts.platform.videos.domain.video_created_domain_event_mother import (
    VideoCreatedDomainEventMother,
)


class TestRabbitMqEventBus:
    def setup_method(self) -> None:
        self.client = RabbitMqConnection(
            connection_settings=RabbitMqSettings(
                user="admin", password="admin", host="localhost"
            )
        )

    def test_should_publish_events(self) -> None:
        event = VideoCreatedDomainEventMother.create()
        producer = RabbitMqEventBus(client=self.client, exchange_name="domain_events")

        producer.publish([event])
