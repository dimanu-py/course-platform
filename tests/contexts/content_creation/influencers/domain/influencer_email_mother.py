from src.contexts.content_creation.influencers.domain.influencer_email import (
    InfluencerEmail,
)
from tests.contexts.shared.domain.random_generator import RandomGenerator


class InfluencerEmailMother:
    @staticmethod
    def create() -> InfluencerEmail:
        return InfluencerEmail(RandomGenerator.email())
