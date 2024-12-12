from src.contexts.platform.videos.application.create.create_video_command import (
    CreateVideoCommand,
)


class CreateVideoCommandMother:
    _INVALID_ID = "12345"
    _VALID_ID = "f847bd9c-cee0-4e14-996c-edaf13720c6c"

    @classmethod
    def with_valid_id(cls) -> CreateVideoCommand:
        return CreateVideoCommand(
            id=cls._VALID_ID, title="title", description="description"
        )

    @classmethod
    def with_invalid_id(cls) -> CreateVideoCommand:
        return CreateVideoCommand(
            id=cls._INVALID_ID, title="title", description="description"
        )
