from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_settings import (
    RabbitMqSettings,
)
from src.contexts.platform.shared.infra.persistence.sqlalchemy.session_maker import (
    SessionMaker,
)


def session_maker_provider() -> SessionMaker:
    return SessionMaker(url="postgresql://admin:admin@localhost:5432/course-platform")


def rabbit_mq_connection_provider() -> RabbitMqConnection:
    return RabbitMqConnection(
        connection_settings=RabbitMqSettings(
            user="admin", password="admin", host="localhost"
        )
    )
