from dataclasses import dataclass

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent


@dataclass(frozen=True, kw_only=True)
class VideoCommentCreatedDomainEvent(DomainEvent):
    id: str
    video_id: str
    author_id: str
    title: str
    content: str
