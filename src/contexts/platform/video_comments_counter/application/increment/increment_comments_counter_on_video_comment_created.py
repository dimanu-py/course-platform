from typing import Type

from src.contexts.platform.shared.domain.event.domain_event_subscriber import (
    DomainEventSubscriber,
)
from src.contexts.platform.video_comments.domain.video_comment_created_domain_event import (
    VideoCommentCreatedDomainEvent,
)
from src.contexts.platform.video_comments_counter.application.increment.comments_counter_incrementer import (
    CommentsCounterIncrementer,
)


class IncrementCommentsCounterOnVideoCommentCreated(
    DomainEventSubscriber[VideoCommentCreatedDomainEvent]
):
    _incrementer: CommentsCounterIncrementer

    def __init__(self, incrementer: CommentsCounterIncrementer) -> None:
        self._incrementer = incrementer

    @staticmethod
    def subscribed_to() -> list[Type[VideoCommentCreatedDomainEvent]]:
        return [VideoCommentCreatedDomainEvent]

    def on(self, event: VideoCommentCreatedDomainEvent) -> None:
        self._incrementer(
            video_id=event.video_id,
        )
