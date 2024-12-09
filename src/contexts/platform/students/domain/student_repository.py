from abc import ABC, abstractmethod

from src.contexts.platform.students.domain.student import Student
from src.contexts.platform.students.domain.student_id import StudentId


class StudentRepository(ABC):
    @abstractmethod
    def save(self, student: Student) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(self, student_id: StudentId) -> Student | None:
        raise NotImplementedError
