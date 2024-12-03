from src.contexts.backoffice.students.domain.student_email import StudentEmail
from tests.contexts.shared.domain.random_generator import RandomGenerator


class StudentEmailMother:
    @staticmethod
    def create() -> StudentEmail:
        return StudentEmail(RandomGenerator.email())
