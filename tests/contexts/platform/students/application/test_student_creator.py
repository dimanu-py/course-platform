from expects import expect, raise_error

from src.contexts.platform.students.application.student_creator import (
    StudentCreator,
)
from src.contexts.platform.students.domain.invalid_email_format_error import (
    InvalidEmailFormatError,
)
from tests.contexts.platform.students.domain.create_student_command_mother import (
    CreateStudentCommandMother,
)
from tests.contexts.platform.students.domain.student_mother import (
    StudentMother,
)
from tests.contexts.platform.students.student_module_unit_test_config import (
    StudentModuleUnitTestConfig,
)


class TestStudentCreator(StudentModuleUnitTestConfig):
    def setup_method(self) -> None:
        self.student_creator = StudentCreator(self.repository)

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
