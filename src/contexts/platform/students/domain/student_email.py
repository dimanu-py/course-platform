import re

from src.contexts.platform.students.domain.invalid_email_format_error import (
    InvalidEmailFormatError,
)
from src.contexts.platform.shared.domain.value_objects.string_value_object import (
    StringValueObject,
)


class StudentEmail(StringValueObject):
    EMAIL_EXPRESSION = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    def _validate(self, value: str) -> None:
        super()._validate(value)
        if re.match(self.EMAIL_EXPRESSION, value) is None:
            raise InvalidEmailFormatError(value)
