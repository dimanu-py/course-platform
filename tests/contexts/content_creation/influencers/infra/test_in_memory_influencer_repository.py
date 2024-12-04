from tests.contexts.content_creation.influencers.influencer_module_integration_test_config import (
    InfluencerModuleIntegrationTestConfig,
)


class TestInMemoryInfluencerRepository(InfluencerModuleIntegrationTestConfig):
    def test_should_save_a_influencer(self) -> None:
        self.repository.save(self.influencer)

        saved_influencer = self.repository.search(self.influencer.id)
        self._should_have(saved_influencer)

    def test_should_find_an_existing_influencer(self) -> None:
        self.repository.save(self.influencer)

        searched_influencer = self.repository.search(self.influencer.id)

        self._should_have(searched_influencer)

    def test_should_not_find_unregistered_influencer(self) -> None:
        searched_influencer = self.repository.search(self.influencer.id)

        self._should_not_have(searched_influencer)
