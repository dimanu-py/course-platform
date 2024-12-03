import pytest
from expects import expect, equal

from src.contexts.backoffice.students.domain.student import Student
from src.contexts.backoffice.students.infra.in_memory_student_repository import (
    InMemoryStudentRepository,
)
from tests.contexts.backoffice.students.domain.student_mother import StudentMother


@pytest.mark.integration
class StudentsModuleIntegrationTestConfig:
    _NO_STUDENT = None
    student = StudentMother.create()

    def setup_method(self) -> None:
        self.repository = InMemoryStudentRepository()

    def _should_have(self, student: Student | None) -> None:
        expect(student).to(equal(self.student))

    def _should_not_have(self, student: Student | None) -> None:
        expect(student).to(equal(self._NO_STUDENT))
