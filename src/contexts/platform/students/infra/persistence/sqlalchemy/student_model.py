from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.contexts.platform.students.domain.student import Student
from src.contexts.platform.shared.infra.persistence.sqlalchemy.base import (
    Base,
)


class StudentModel(Base):
    __tablename__ = "students"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String, nullable=False)

    def to_aggregate(self) -> Student:
        return Student.create(
            id_=str(self.id),
            name=self.name,
            username=self.username,
            email=self.email,
        )
