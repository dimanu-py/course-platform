import pytest
from expects import expect, equal

from src.contexts.content_creation.influencers.domain.influencer import Influencer
from src.contexts.content_creation.influencers.infra.in_memory_influencer_repository import (
    InMemoryInfluencerRepository,
)
from src.contexts.content_creation.influencers.infra.postgres_influencer_repository import (
    PostgresInfluencerRepository,
)
from src.contexts.shared.infra.persistence.session_maker import (
    SessionMaker,
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
        self.session_maker = SessionMaker(
            "postgresql://admin:admin@localhost:5432/influencer-platform"
        )
        self.session_maker.create_tables()
        self.postgres_influencer_repository = PostgresInfluencerRepository(
            self.session_maker
        )

    def teardown_method(self) -> None:
        self.session_maker.close_session()
        self.session_maker.drop_tables()

    def assert_influencer_matches(self, influencer: Influencer | None) -> None:
        expect(influencer).to(equal(self.influencer))

    def assert_has_not_found(self, influencer: Influencer | None) -> None:
        expect(influencer).to(equal(self._NO_INFLUENCER))
