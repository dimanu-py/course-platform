from typing import override

from src.contexts.content_creation.influencers.domain.influencer import Influencer
from src.contexts.content_creation.influencers.domain.influencer_id import InfluencerId
from src.contexts.content_creation.influencers.domain.influencer_repository import (
    InfluencerRepository,
)


class InMemoryInfluencerRepository(InfluencerRepository):
    _influencers: dict[str, Influencer]

    def __init__(self) -> None:
        self._influencers = {}

    @override
    def save(self, influencer: Influencer) -> None:
        self._influencers[influencer.id.value] = influencer

    @override
    def search(self, influencer_id: InfluencerId) -> Influencer | None:
        return self._influencers.get(influencer_id.value)
