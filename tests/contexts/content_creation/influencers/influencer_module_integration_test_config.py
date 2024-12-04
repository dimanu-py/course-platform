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
        self.repository = InMemoryInfluencerRepository()

    def _should_have(self, influencer: Influencer | None) -> None:
        expect(influencer).to(equal(self.influencer))

    def _should_not_have(self, influencer: Influencer | None) -> None:
        expect(influencer).to(equal(self._NO_INFLUENCER))
