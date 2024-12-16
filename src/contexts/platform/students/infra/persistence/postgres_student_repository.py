from typing import override

from src.contexts.platform.students.domain.student import Student
from src.contexts.platform.students.domain.student_id import StudentId
from src.contexts.platform.students.domain.student_repository import (
    StudentRepository,
)
from src.contexts.platform.students.infra.persistence.sqlalchemy.student_model import (
    StudentModel,
)
from src.contexts.platform.shared.infra.persistence.sqlalchemy.session_maker import (
    SessionMaker,
)
from src.contexts.platform.shared.infra.persistence.sqlalchemy.sqlalchemy_repository import (
    SqlAlchemyRepository,
)


class PostgresStudentRepository(SqlAlchemyRepository[StudentModel], StudentRepository):
    _session_maker: SessionMaker

    def __init__(self, session_maker: SessionMaker) -> None:
        super().__init__(session_maker=session_maker, model_class=StudentModel)

    @override
    def save(self, student: Student) -> None:
        self.persist(student)

    @override
    def search(self, student_id: StudentId) -> Student | None:
        return self.search_by_id(student_id)
