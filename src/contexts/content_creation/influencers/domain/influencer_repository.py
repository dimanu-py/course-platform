from abc import ABC, abstractmethod

from src.contexts.content_creation.influencers.domain.influencer import Influencer
from src.contexts.content_creation.influencers.domain.influencer_id import InfluencerId


class InfluencerRepository(ABC):
    @abstractmethod
    def save(self, influencer: Influencer) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(self, influencer_id: InfluencerId) -> Influencer | None:
        raise NotImplementedError
