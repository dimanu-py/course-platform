from typing import override

from src.contexts.content_creation.influencers.domain.influencer_email import (
    InfluencerEmail,
)
from src.contexts.content_creation.influencers.domain.influencer_id import InfluencerId
from src.contexts.content_creation.influencers.domain.influencer_name import (
    InfluencerName,
)
from src.contexts.content_creation.influencers.domain.influencer_username import (
    InfluencerUsername,
)


class Influencer:
    _id: InfluencerId
    _name: InfluencerName
    _username: InfluencerUsername
    _email: InfluencerEmail

    def __init__(
        self,
        id_: InfluencerId,
        name: InfluencerName,
        username: InfluencerUsername,
        email: InfluencerEmail,
    ) -> None:
        self._email = email
        self._username = username
        self._name = name
        self._id = id_

    @classmethod
    def create(cls, id_: str, name: str, username: str, email: str) -> "Influencer":
        influencer_id = InfluencerId(id_)
        influencer_name = InfluencerName(name)
        influencer_username = InfluencerUsername(username)
        influencer_email = InfluencerEmail(email)
        return cls(
            influencer_id, influencer_name, influencer_username, influencer_email
        )

    @override
    def __eq__(self, other: "Influencer") -> bool:
        return self._id == other._id

    @property
    def id(self) -> InfluencerId:
        return self._id

    def to_dict(self) -> dict:
        return {
            "id": self._id.value,
            "name": self._name.value,
            "username": self._username.value,
            "email": self._email.value,
        }
