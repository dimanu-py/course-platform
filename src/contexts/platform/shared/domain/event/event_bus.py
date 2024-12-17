from abc import ABC, abstractmethod

from src.contexts.platform.shared.domain.event.domain_event import DomainEvent


class EventBus(ABC):
    @abstractmethod
    def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError
