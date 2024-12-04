import pytest
from expects import expect, equal

from src.contexts.content_creation.influencers.domain.influencer import Influencer
from src.contexts.content_creation.influencers.infra.in_memory_influencer_repository import (
    InMemoryInfluencerRepository,
)
from tests.contexts.content_creation.influencers.domain.influencer_mother import (
    InfluencerMother,
)


@pytest.mark.integration
class InfluencerModuleIntegrationTestConfig:
    _NO_INFLUENCER = None
    influencer = InfluencerMother.create()

    def setup_method(self) -> None:
        self.in_memory_influencer_repository = InMemoryInfluencerRepository()

    def assert_influencer_matches(self, influencer: Influencer | None) -> None:
        expect(influencer).to(equal(self.influencer))

    def assert_has_not_found(self, influencer: Influencer | None) -> None:
        expect(influencer).to(equal(self._NO_INFLUENCER))
