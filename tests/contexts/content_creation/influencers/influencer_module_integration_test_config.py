import pytest
from expects import expect, equal

from src.contexts.content_creation.influencers.domain.influencer import Influencer
from src.contexts.content_creation.influencers.infra.persistence.in_memory_influencer_repository import (
    InMemoryInfluencerRepository,
)
from src.contexts.content_creation.influencers.infra.persistence.postgres_influencer_repository import (
    PostgresInfluencerRepository,
)
from src.contexts.content_creation.influencers.infra.persistence.sqlalchemy.influencer_model import (
    InfluencerModel,
)
from src.contexts.content_creation.shared.infra.sqlalchemy.session_maker import (
    SessionMaker,
)


@pytest.mark.integration
class InfluencerModuleIntegrationTestConfig:
    _NO_INFLUENCER = None

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
        with self.session_maker.get_session() as session:
            session.query(InfluencerModel).delete()
            session.commit()

    def assert_influencers_match(
        self, influencer: Influencer | None, expected_influencer: Influencer | None
    ) -> None:
        expect(influencer).to(equal(expected_influencer))

    def assert_has_not_found(self, influencer: Influencer | None) -> None:
        expect(influencer).to(equal(self._NO_INFLUENCER))
