from expects import expect, raise_error

from src.contexts.backoffice.students.domain.invalid_email_format_error import (
    InvalidEmailFormatError,
)
from tests.contexts.backoffice.students.domain.create_student_command_mother import (
    CreateStudentCommandMother,
)
from tests.contexts.backoffice.students.domain.student_mother import StudentMother
from tests.contexts.backoffice.students.students_module_unit_test_config import (
    StudentsModuleUnitTestConfig,
)


class TestStudentCreator(StudentsModuleUnitTestConfig):
    def test_should_create_a_valid_student(self) -> None:
        command = CreateStudentCommandMother.valid()
        student_to_save = StudentMother.from_request(command)

        self.student_creator(command)

        self.should_have_saved(student_to_save)

    def test_should_fail_to_create_student_with_invalid_id(self) -> None:
        command = CreateStudentCommandMother.invalid_id()

        expect(lambda: self.student_creator(command)).to(raise_error(ValueError))

    def test_should_fail_to_create_student_with_invalid_email(self) -> None:
        command = CreateStudentCommandMother.invalid_email()

        expect(lambda: self.student_creator(command)).to(
            raise_error(InvalidEmailFormatError)
        )
