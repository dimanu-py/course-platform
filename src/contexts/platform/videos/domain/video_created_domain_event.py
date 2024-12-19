from dataclasses import dataclass
from typing import override

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent


@dataclass(frozen=True, kw_only=True)
class VideoCreatedDomainEvent(DomainEvent):
    id: str
    title: str
    description: str

    @classmethod
    @override
    def name(cls) -> str:
        return "dimanu.platform.event.video.created"
