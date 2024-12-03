from dataclasses import dataclass


@dataclass
class CreateVideoRequest:
    title: str
    description: str
