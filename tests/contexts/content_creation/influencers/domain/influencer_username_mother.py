from src.contexts.content_creation.influencers.domain.influencer_username import (
    InfluencerUsername,
)
from tests.contexts.shared.domain.random_generator import RandomGenerator


class InfluencerUsernameMother:
    @staticmethod
    def create() -> InfluencerUsername:
        return InfluencerUsername(RandomGenerator.username())
