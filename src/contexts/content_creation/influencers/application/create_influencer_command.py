from dataclasses import dataclass


@dataclass
class CreateInfluencerCommand:
    id_: str
    name: str
    username: str
    email: str
