import json

import pika
from pika.adapters.blocking_connection import BlockingChannel

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent
from src.contexts.platform.shared.domain.exceptions.rabbit_mq_connection_not_established_error import (
    RabbitMqConnectionNotEstablishedError,
)
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_settings import (
    RabbitMqSettings,
)


class RabbitMqConnection:
    _channel: BlockingChannel | None
    _connection: pika.BlockingConnection | None
    _connection_settings: RabbitMqSettings

    def __init__(self, connection_settings: RabbitMqSettings) -> None:
        self._connection_settings = connection_settings
        self._connection = None
        self._channel = None
        self._establish_connection()

    def _establish_connection(self) -> None:
        credentials = pika.PlainCredentials(
            username=self._connection_settings.user,
            password=self._connection_settings.password,
        )
        self._connection = pika.BlockingConnection(
            parameters=pika.ConnectionParameters(
                host=self._connection_settings.host, credentials=credentials
            )
        )
        self._channel = self._connection.channel()

    def create_exchange(self, name: str) -> None:
        self._ensure_channel_exists()
        self._channel.exchange_declare(exchange=name, exchange_type="topic")  # type: ignore

    def publish(self, event: DomainEvent, exchange: str) -> None:
        self._ensure_channel_exists()
        self._channel.basic_publish(  # type: ignore
            exchange=exchange,
            routing_key=event.name,
            body=json.dumps(event.serialize()),
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )

    def _ensure_channel_exists(self) -> None:
        if self._channel is None:
            raise RabbitMqConnectionNotEstablishedError
