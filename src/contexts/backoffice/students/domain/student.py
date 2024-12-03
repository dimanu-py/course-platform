from typing import override

from src.contexts.backoffice.students.domain.student_email import StudentEmail
from src.contexts.backoffice.students.domain.student_id import StudentId
from src.contexts.backoffice.students.domain.student_name import StudentName
from src.contexts.backoffice.students.domain.student_username import StudentUsername


class Student:
    _id: StudentId
    _name: StudentName
    _username: StudentUsername
    _email: StudentEmail

    def __init__(
        self,
        id_: StudentId,
        name: StudentName,
        username: StudentUsername,
        email: StudentEmail,
    ) -> None:
        self._email = email
        self._username = username
        self._name = name
        self._id = id_

    @classmethod
    def create(cls, id_: str, name: str, username: str, email: str) -> "Student":
        student_id = StudentId(id_)
        student_name = StudentName(name)
        student_username = StudentUsername(username)
        student_email = StudentEmail(email)
        return cls(student_id, student_name, student_username, student_email)

    @override
    def __eq__(self, other: "Student") -> bool:
        return self._id == other._id

    @property
    def id(self) -> StudentId:
        return self._id
