from dataclasses import dataclass


@dataclass
class CreateInfluencerRequest:
    name: str
    username: str
    email: str
