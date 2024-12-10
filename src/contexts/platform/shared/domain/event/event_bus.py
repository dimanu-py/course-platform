from src.contexts.platform.shared.domain.event.domain_event import DomainEvent


class EventBus:
    def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError
