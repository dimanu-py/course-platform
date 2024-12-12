from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class CreateVideoCommand:
    id: str
    title: str
    description: str
