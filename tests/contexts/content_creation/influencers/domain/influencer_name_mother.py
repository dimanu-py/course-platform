from src.contexts.content_creation.influencers.domain.influencer_name import (
    InfluencerName,
)
from tests.contexts.shared.domain.random_generator import RandomGenerator


class InfluencerNameMother:
    @staticmethod
    def create() -> InfluencerName:
        return InfluencerName(RandomGenerator.name())
