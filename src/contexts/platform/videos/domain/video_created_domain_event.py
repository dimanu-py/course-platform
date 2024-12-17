from dataclasses import dataclass

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent


@dataclass(frozen=True, kw_only=True)
class VideoCreatedDomainEvent(DomainEvent):
    id: str
    title: str
    description: str

    @property
    def name(self) -> str:
        return "dimanu.platform.event.video.created"
