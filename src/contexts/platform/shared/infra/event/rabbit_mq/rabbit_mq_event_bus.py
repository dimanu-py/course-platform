from src.contexts.platform.shared.domain.event.domain_event import DomainEvent
from src.contexts.platform.shared.domain.event.event_bus import EventBus
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)


class RabbitMqEventBus(EventBus):
    def __init__(self, client: RabbitMqConnection, exchange_name: str) -> None:
        self._client = client
        self._exchange_name = exchange_name
        self._define_exchange_to_publish()

    def publish(self, events: list[DomainEvent]) -> None:
        for event in events:
            self._client.publish(event=event, exchange=self._exchange_name)

    def _define_exchange_to_publish(self) -> None:
        self._client.create_exchange(self._exchange_name)
