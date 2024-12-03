from src.contexts.backoffice.students.application.create_student_command import (
    CreateStudentCommand,
)
from src.contexts.backoffice.students.domain.student import Student


class StudentMother:
    @classmethod
    def from_request(cls, command: CreateStudentCommand) -> Student:
        return Student.create(
            command.id_, command.name, command.username, command.email
        )
