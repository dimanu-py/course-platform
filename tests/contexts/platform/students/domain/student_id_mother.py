from src.contexts.platform.students.domain.student_id import StudentId
from tests.contexts.shared.domain.random_generator import RandomGenerator


class StudentIdMother:
    @staticmethod
    def create() -> StudentId:
        return StudentId(RandomGenerator.uuid())
