from src.contexts.platform.students.application.create_student_command import (
    CreateStudentCommand,
)
from src.contexts.platform.students.domain.student import Student
from tests.contexts.platform.students.domain.student_email_mother import (
    StudentEmailMother,
)
from tests.contexts.platform.students.domain.student_id_mother import (
    StudentIdMother,
)
from tests.contexts.platform.students.domain.student_name_mother import (
    StudentNameMother,
)
from tests.contexts.platform.students.domain.student_username_mother import (
    StudentUsernameMother,
)


class StudentMother:
    @classmethod
    def from_request(cls, command: CreateStudentCommand) -> Student:
        return Student.create(
            command.id_, command.name, command.username, command.email
        )

    @classmethod
    def create(cls) -> Student:
        return Student(
            StudentIdMother.create(),
            StudentNameMother.create(),
            StudentUsernameMother.create(),
            StudentEmailMother.create(),
        )
