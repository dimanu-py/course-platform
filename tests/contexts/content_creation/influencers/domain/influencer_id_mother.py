from src.contexts.content_creation.influencers.domain.influencer_id import InfluencerId
from tests.contexts.shared.domain.random_generator import RandomGenerator


class InfluencerIdMother:
    @staticmethod
    def create() -> InfluencerId:
        return InfluencerId(RandomGenerator.uuid())
