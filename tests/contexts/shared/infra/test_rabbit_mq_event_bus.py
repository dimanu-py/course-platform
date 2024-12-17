from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_event_bus import (
    RabbitMqEventBus,
)
from tests.contexts.platform.videos.domain.video_created_domain_event_mother import (
    VideoCreatedDomainEventMother,
)


class TestRabbitMqEventBus:
    def test_should_publish_events(self) -> None:
        event = VideoCreatedDomainEventMother.create()
        producer = RabbitMqEventBus(
            url="amqp://admin:admin@localhost/", exchange_name="domain_events"
        )

        producer.publish([event])
