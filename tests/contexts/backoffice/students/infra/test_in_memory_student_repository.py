from tests.contexts.backoffice.students.students_module_integration_test_config import (
    StudentsModuleIntegrationTestConfig,
)


class TestInMemoryStudentRepository(StudentsModuleIntegrationTestConfig):
    def test_should_save_a_student(self) -> None:
        self.repository.save(self.student)

        saved_student = self.repository.search(self.student.id)
        self._should_have(saved_student)

    def test_should_find_an_existing_student(self) -> None:
        self.repository.save(self.student)

        searched_student = self.repository.search(self.student.id)

        self._should_have(searched_student)

    def test_should_not_find_unregistered_student(self) -> None:
        searched_student = self.repository.search(self.student.id)

        self._should_not_have(searched_student)
