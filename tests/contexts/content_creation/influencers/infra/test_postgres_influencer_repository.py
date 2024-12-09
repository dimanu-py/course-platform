from tests.contexts.content_creation.influencers.domain.influencer_mother import (
    InfluencerMother,
)
from tests.contexts.content_creation.influencers.influencer_module_integration_test_config import (
    InfluencerModuleIntegrationTestConfig,
)


class TestPostgresInfluencerRepository(InfluencerModuleIntegrationTestConfig):
    def test_should_save_a_influencer(self) -> None:
        influencer = InfluencerMother.create()

        self.postgres_influencer_repository.save(influencer)

        saved_influencer = self.postgres_influencer_repository.search(influencer.id)
        self.assert_influencers_match(influencer, saved_influencer)

    def test_should_find_an_existing_influencer(self) -> None:
        influencer = InfluencerMother.create()
        self.postgres_influencer_repository.save(influencer)

        searched_influencer = self.postgres_influencer_repository.search(influencer.id)

        self.assert_influencers_match(influencer, searched_influencer)

    def test_should_not_find_unregistered_influencer(self) -> None:
        influencer = InfluencerMother.create()

        searched_influencer = self.postgres_influencer_repository.search(influencer.id)

        self.assert_has_not_found(searched_influencer)
