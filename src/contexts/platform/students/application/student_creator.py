from src.contexts.platform.students.application.create_student_command import (
    CreateStudentCommand,
)
from src.contexts.platform.students.domain.student import Student
from src.contexts.platform.students.domain.student_repository import (
    StudentRepository,
)


class StudentCreator:
    _repository: StudentRepository

    def __init__(self, repository: StudentRepository) -> None:
        self._repository = repository

    def __call__(self, command: CreateStudentCommand) -> None:
        student = Student.create(
            id_=command.id_,
            name=command.name,
            username=command.username,
            email=command.email,
        )
        self._repository.save(student)
