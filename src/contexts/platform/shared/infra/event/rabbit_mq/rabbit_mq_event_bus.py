import json

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent
from src.contexts.platform.shared.domain.event.event_bus import EventBus
from src.contexts.platform.shared.domain.exceptions.rabbit_mq_connection_not_established_error import (
    RabbitMqConnectionNotEstablishedError,
)
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)


class RabbitMqEventBus(EventBus):
    def __init__(self, client: RabbitMqConnection, exchange_name: str) -> None:
        self._client = client
        self._channel = self._client._channel
        self._exchange_name = exchange_name

    def publish(self, events: list[DomainEvent]) -> None:
        if self._channel is None:
            raise RabbitMqConnectionNotEstablishedError

        self._channel.exchange_declare(
            exchange=self._exchange_name, exchange_type="topic"
        )
        for event in events:
            self._channel.basic_publish(
                exchange=self._exchange_name,
                routing_key=event.name,
                body=json.dumps(event.serialize()),
            )
