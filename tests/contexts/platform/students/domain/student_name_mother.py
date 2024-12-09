from src.contexts.platform.students.domain.student_name import (
    StudentName,
)
from tests.contexts.shared.domain.random_generator import RandomGenerator


class StudentNameMother:
    @staticmethod
    def create() -> StudentName:
        return StudentName(RandomGenerator.name())
