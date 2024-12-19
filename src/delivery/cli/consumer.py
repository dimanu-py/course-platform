import typer

from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_consumer import (
    RabbitMqConsumer,
)
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_configurer import (
    RabbitMqConfigurer,
)
from src.contexts.platform.shared.infra.event.rabbit_mq.rabbit_mq_queue_formatter import (
    RabbitMqQueueFormatter,
)
from src.contexts.platform.video_comments_counter.application.increment.comments_counter_incrementer import (
    CommentsCounterIncrementer,
)
from src.contexts.platform.video_comments_counter.application.increment.increment_comments_counter_on_video_comment_created import (
    IncrementCommentsCounterOnVideoCommentCreated,
)
from src.contexts.platform.video_comments_counter.infra.persistence.postgres_video_comment_counter_repository import (
    PostgresVideoCommentCounterRepository,
)
from src.delivery.api.dependency_provider import (
    rabbit_mq_connection_provider,
    session_maker_provider,
)

app = typer.Typer(name="cli_event_consumer")


@app.command()
def consume() -> None:
    """Consume events from the event bus."""
    subscribers = [
        IncrementCommentsCounterOnVideoCommentCreated(
            incrementer=CommentsCounterIncrementer(
                repository=PostgresVideoCommentCounterRepository(
                    session_maker=session_maker_provider()
                )
            )
        )
    ]
    queue_formatter = RabbitMqQueueFormatter(bounded_context="platform")
    configurer = RabbitMqConfigurer(
        connection=rabbit_mq_connection_provider(), queue_formatter=queue_formatter
    )
    configurer.configure("comments_events", subscribers=subscribers)  # type: ignore
    consumer = RabbitMqConsumer(
        client=rabbit_mq_connection_provider(),
        subscriber=subscribers[0],  # type: ignore
        queue_formatter=queue_formatter,
    )

    try:
        consumer.start_consuming()
    except KeyboardInterrupt:
        print("Exiting...")
        consumer.stop_consuming()
        print("Exited.")


if __name__ == "__main__":
    consume()
