from src.contexts.backoffice.videos.application.create_video_command import (
    CreateVideoCommand,
)


class CreateVideoCommandMother:
    _VALID_ID = "8e197c6-0379-4142-acb7-9234f460ca6e"

    @classmethod
    def with_valid_id(cls) -> CreateVideoCommand:
        return CreateVideoCommand(cls._VALID_ID, "title", "description", 10)
