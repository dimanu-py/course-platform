from tests.contexts.content_creation.videos.video_module_integration_test_config import (
    VideoModuleIntegrationTestConfig,
)


class TestPostgresVideoRepository(VideoModuleIntegrationTestConfig):
    def test_should_save_a_video(self) -> None:
        self.postgres_video_repository.save(self.video)

        saved_video = self.postgres_video_repository.search(self.video.id)
        self.assert_video_matches(saved_video)

    def test_should_find_existing_video(self) -> None:
        self.postgres_video_repository.save(self.video)

        searched_video = self.postgres_video_repository.search(self.video.id)

        self.assert_video_matches(searched_video)

    def test_should_not_find_non_existing_video(self) -> None:
        searched_video = self.postgres_video_repository.search(self.video.id)

        self.assert_has_not_found(searched_video)
