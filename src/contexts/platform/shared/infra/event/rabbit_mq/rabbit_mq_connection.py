import pika
from pika.adapters.blocking_connection import BlockingChannel

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
