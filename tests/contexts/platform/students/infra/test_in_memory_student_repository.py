from tests.contexts.platform.students.domain.student_mother import (
    StudentMother,
)
from tests.contexts.platform.students.student_module_integration_test_config import (
    StudentModuleIntegrationTestConfig,
)


class TestInMemoryStudentRepository(StudentModuleIntegrationTestConfig):
    def test_should_save_a_student(self) -> None:
        student = StudentMother.create()

        self.in_memory_student_repository.save(student)

        saved_student = self.in_memory_student_repository.search(student.id)
        self.assert_students_match(student, saved_student)

    def test_should_find_an_existing_student(self) -> None:
        student = StudentMother.create()
        self.in_memory_student_repository.save(student)

        searched_student = self.in_memory_student_repository.search(student.id)

        self.assert_students_match(student, searched_student)

    def test_should_not_find_unregistered_student(self) -> None:
        student = StudentMother.create()

        searched_student = self.in_memory_student_repository.search(student.id)

        self.assert_has_not_found(searched_student)
