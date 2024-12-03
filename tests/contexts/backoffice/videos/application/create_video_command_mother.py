from src.contexts.backoffice.videos.application.create_video_command import (
    CreateVideoCommand,
)


class CreateVideoCommandMother:
    _VALID_ID = "f847bd9c-cee0-4e14-996c-edaf13720c6c"

    @classmethod
    def with_valid_id(cls) -> CreateVideoCommand:
        return CreateVideoCommand(cls._VALID_ID, "title", "description")
