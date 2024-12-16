import pytest
from expects import expect, equal

from src.contexts.platform.students.domain.student import Student
from src.contexts.platform.students.infra.persistence.in_memory_student_repository import (
    InMemoryStudentRepository,
)
from src.contexts.platform.students.infra.persistence.postgres_student_repository import (
    PostgresStudentRepository,
)
from src.contexts.platform.students.infra.persistence.sqlalchemy.student_model import (
    StudentModel,
)
from src.contexts.platform.shared.infra.persistence.sqlalchemy.session_maker import (
    SessionMaker,
)


@pytest.mark.integration
class StudentModuleIntegrationTestConfig:
    _NO_INFLUENCER = None

    def setup_method(self) -> None:
        self.in_memory_student_repository = InMemoryStudentRepository()
        self.session_maker = SessionMaker(
            "postgresql://admin:admin@localhost:5432/influencer-platform"
        )
        self.session_maker.create_tables()
        self.postgres_student_repository = PostgresStudentRepository(self.session_maker)

    def teardown_method(self) -> None:
        with self.session_maker.get_session() as session:
            session.query(StudentModel).delete()
            session.commit()

    def assert_students_match(
        self, student: Student | None, expected_student: Student | None
    ) -> None:
        expect(student).to(equal(expected_student))

    def assert_has_not_found(self, student: Student | None) -> None:
        expect(student).to(equal(self._NO_INFLUENCER))
