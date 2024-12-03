import pytest
from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.contexts.backoffice.students.application.student_creator import StudentCreator
from src.contexts.backoffice.students.domain.student_repository import StudentRepository


@pytest.mark.unit
class StudentsModuleUnitTestConfig:
    def setup_method(self) -> None:
        self.repository = Spy(StudentRepository)
        self.student_creator = StudentCreator(self.repository)

    def should_have_saved(self, student) -> None:
        expect(self.repository.save).to(have_been_called_with(student))
