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
