from src.contexts.platform.shared.domain.value_objects.int_value_object import (
    IntValueObject,
)


class VideoCommentTotal(IntValueObject):
    START_VALUE: int = 0
    INCREMENT_VALUE: int = 1

    @classmethod
    def initialize(cls) -> "VideoCommentTotal":
        return VideoCommentTotal(cls.START_VALUE)

    def increment(self) -> "VideoCommentTotal":
        return VideoCommentTotal(self.value + self.INCREMENT_VALUE)
