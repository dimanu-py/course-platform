from src.contexts.backoffice.students.domain.student_username import StudentUsername
from tests.contexts.shared.domain.random_generator import RandomGenerator


class StudentUsernameMother:
    @staticmethod
    def create() -> StudentUsername:
        return StudentUsername(RandomGenerator.username())
