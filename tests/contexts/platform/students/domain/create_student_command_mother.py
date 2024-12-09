from src.contexts.platform.students.application.create_student_command import (
    CreateStudentCommand,
)


class CreateStudentCommandMother:
    _VALID_ID: str = "05fbc052-7c8e-4d99-824b-ae469f2bc80e"
    _VALID_EMAIL: str = "any_email@email.com"
    _INVALID_ID: str = "12345"
    _INVALID_EMAIL: str = "invalid_email"

    @classmethod
    def valid(cls) -> CreateStudentCommand:
        return CreateStudentCommand(
            cls._VALID_ID, "any_name", "any_username", cls._VALID_EMAIL
        )

    @classmethod
    def invalid_id(cls):
        return CreateStudentCommand(
            cls._INVALID_ID, "any_name", "any_username", cls._VALID_EMAIL
        )

    @classmethod
    def invalid_email(cls):
        return CreateStudentCommand(
            cls._VALID_ID, "any_name", "any_username", cls._INVALID_EMAIL
        )
