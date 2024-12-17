import json

import pika

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent
from src.contexts.platform.shared.domain.event.event_bus import EventBus


class RabbitMqEventBus(EventBus):
    def __init__(self, url: str, exchange_name: str) -> None:
        self._connection = pika.BlockingConnection(
            parameters=pika.URLParameters(url=url)
        )
        self._channel = self._connection.channel()
        self._exchange_name = exchange_name

    def publish(self, events: list[DomainEvent]) -> None:
        self._channel.exchange_declare(
            exchange=self._exchange_name, exchange_type="topic"
        )
        for event in events:
            self._channel.basic_publish(
                exchange=self._exchange_name,
                routing_key=event.name,
                body=json.dumps(event.serialize()),
            )
