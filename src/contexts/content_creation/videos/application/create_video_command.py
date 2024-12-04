from dataclasses import dataclass


@dataclass(frozen=True)
class CreateVideoCommand:
    id: str
    title: str
    description: str
