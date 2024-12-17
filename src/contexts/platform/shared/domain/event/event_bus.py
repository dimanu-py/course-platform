from abc import ABC

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent


class EventBus(ABC):
    def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError
