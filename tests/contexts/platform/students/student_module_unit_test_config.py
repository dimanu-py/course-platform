import pytest
from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.contexts.platform.students.domain.student import Student
from src.contexts.platform.students.domain.student_repository import (
    StudentRepository,
)


@pytest.mark.unit
class StudentModuleUnitTestConfig:
    repository = Spy(StudentRepository)

    def should_have_saved(self, student: Student) -> None:
        expect(self.repository.save).to(have_been_called_with(student))
