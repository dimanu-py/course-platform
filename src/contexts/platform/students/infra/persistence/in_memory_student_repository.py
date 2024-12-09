from typing import override

from src.contexts.platform.students.domain.student import Student
from src.contexts.platform.students.domain.student_id import StudentId
from src.contexts.platform.students.domain.student_repository import (
    StudentRepository,
)


class InMemoryStudentRepository(StudentRepository):
    _students: dict[str, Student]

    def __init__(self) -> None:
        self._students = {}

    @override
    def save(self, student: Student) -> None:
        self._students[student.id.value] = student

    @override
    def search(self, student_id: StudentId) -> Student | None:
        return self._students.get(student_id.value)
