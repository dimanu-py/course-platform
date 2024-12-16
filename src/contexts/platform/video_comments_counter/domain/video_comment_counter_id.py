from src.contexts.platform.shared.domain.value_objects.uuid import Uuid


class VideoCommentCounterId(Uuid):
    @classmethod
    def generate(cls) -> "VideoCommentCounterId":
        return VideoCommentCounterId(Uuid.generate())
