from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass


@dataclass(frozen=True, kw_only=True)
class DomainEvent(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    def serialize(self) -> dict:
        event_fields = asdict(self)
        event_fields["name"] = self.name
        return event_fields
