import pytest
from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.contexts.content_creation.influencers.application.influencer_creator import (
    InfluencerCreator,
)
from src.contexts.content_creation.influencers.domain.influencer import Influencer
from src.contexts.content_creation.influencers.domain.influencer_repository import (
    InfluencerRepository,
)


@pytest.mark.unit
class InfluencerModuleUnitTestConfig:
    def setup_method(self) -> None:
        self.repository = Spy(InfluencerRepository)
        self.influencer_creator = InfluencerCreator(self.repository)

    def should_have_saved(self, influencer: Influencer) -> None:
        expect(self.repository.save).to(have_been_called_with(influencer))
