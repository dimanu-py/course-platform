from src.contexts.backoffice.students.domain.student import Student


class StudentRepository:
    def save(self, student: Student) -> None:
        raise NotImplementedError
